import argparse
import logging
import logging.config
from pathlib import Path

import yaml
import grpc
import asyncio

import msg_replication_pb2
import msg_replication_pb2_grpc

with Path(__file__).resolve().parent.joinpath('logging.yaml').open('r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

logger = logging.getLogger(__name__)


class SecondaryLogServicer(msg_replication_pb2_grpc.SecondaryLogServicer):
    MESSAGES_INFO = []

    def _get_msgs(self):
        return [x[1] for x in sorted(self.MESSAGES_INFO, key=lambda k: k[0])]

    def _get_args(self):
        parser = argparse.ArgumentParser(description='Process delays.')
        parser.add_argument('-d', '--delay', type=int, default=None)
        return parser.parse_args()

    async def replicate_message(self, request, context):
        logger.info(f"Got request for replicating message...\nRequest info:\n{request}")
   
        args = self._get_args()
        delay = args.delay
        if delay:
            logger.info(f"Sleeping for {delay}s...")
            await asyncio.sleep(delay)
        
        msg_text = request.message

        response = msg_replication_pb2.MessageReplicationResponse()
        response.message = msg_text
        response.received = True

        if msg_text not in self._get_msgs():
            self.MESSAGES_INFO.append((request.id, msg_text))

        logger.info(f"The message {msg_text} was successfully replicated!")

        return response

    async def get_messages(self, request, context):
        logger.info(f"Got request for list messages...")
        response = msg_replication_pb2.ReplicatedMessageList(messages=self._get_msgs())

        return response


async def serve():
    server = grpc.aio.server()
    msg_replication_pb2_grpc.add_SecondaryLogServicer_to_server(SecondaryLogServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.add_insecure_port("[::]:50052")
    server.add_insecure_port("[::]:50053")
    logging.info(f"Starting secondary server!")
    await server.start()
    await server.wait_for_termination()


if __name__ == "__main__":
    asyncio.run(serve())
