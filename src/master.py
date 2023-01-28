import concurrent
import logging
import logging.config
from pathlib import Path

import yaml
import grpc
import asyncio

import log_pb2
import log_pb2_grpc

import msg_replication_pb2
import msg_replication_pb2_grpc

with Path(__file__).resolve().parent.joinpath('logging.yaml').open('r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

logger = logging.getLogger(__name__)


class LogServicer(log_pb2_grpc.LogServicer):
    MESSAGE_LIST = []
    CHANNELS = {
        1: 'secondary-one:50052',
        2: 'secondary-two:50053'
    }

    async def replicate_to_secondary(self, id: int, message: str, secondary_number: int):
        channel_address = self.CHANNELS[secondary_number]

        async with grpc.aio.insecure_channel(channel_address) as channel:
            logger.info(f"Replicating the message to the secondary-{secondary_number}...")
            stub = msg_replication_pb2_grpc.SecondaryLogStub(channel)
            response = msg_replication_pb2.MessageReplicationResponse()
            try:
                response = await stub.replicate_message(
                    msg_replication_pb2.MessageReplicationRequest(id=id, message=message)
                )
            except grpc.aio.AioRpcError as rpc_error:
                if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
                    logger.error(f"{channel_address} is UNAVAILABLE! Details: {rpc_error.details()}")
                    response.received = False
                    response.message = message

            return response

    async def send_message(self, request, context):
        logger.info(f"Got request for sending message...\nRequest info:\n{request}")
        msg_text = request.message
        req_id = request.id


        if write_concern := request.write_concern:
            logger.info(f"Got write concern: {write_concern}")
        else:
            write_concern = 1
        
        replicated = False

        match write_concern:
            case 1:
                asyncio.create_task(self.replicate_to_secondary(req_id, msg_text, 1)),
                asyncio.create_task(self.replicate_to_secondary(req_id, msg_text, 2))
                replicated = True
            case 2:
                tasks = [
                    asyncio.create_task(self.replicate_to_secondary(req_id, msg_text, 1)),
                    asyncio.create_task(self.replicate_to_secondary(req_id, msg_text, 2))
                ]
                finished, _ = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
                results = [task.result() for task in finished]
                for resp in results:
                    if resp.received:
                        replicated = True       
            case 3:
                s1_response, s2_response = await asyncio.gather(
                    self.replicate_to_secondary(req_id, msg_text, 1),
                    self.replicate_to_secondary(req_id, msg_text, 2)
                )
                if s1_response.received and s2_response.received:
                    replicated = True

        response = log_pb2.LogResponse()
        response.message = msg_text
        response.received = True if replicated else False

        if response.received:
            if msg_text not in self.MESSAGE_LIST:
                self.MESSAGE_LIST.append(msg_text)
            logger.info(f"The message {msg_text} was received and successfully replicated!")
        else:
            logger.info(f"The message {msg_text} wasn't successfully replicated!")

        return response

    def list_messages(self, request, context):
        logger.info(f"Got request for list messages...")
        response = log_pb2.MessageList(messages=self.MESSAGE_LIST)

        return response


async def serve():
    server = grpc.aio.server()
    log_pb2_grpc.add_LogServicer_to_server(LogServicer(), server)
    listen_addr = '[::]:50051'
    server.add_insecure_port(listen_addr)
    logging.info(f"Starting server on {listen_addr}")
    await server.start()
    await server.wait_for_termination()

if __name__ == "__main__":
    asyncio.run(serve())
