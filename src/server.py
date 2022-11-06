from concurrent import futures
import logging
import logging.config
from pathlib import Path

import yaml
import grpc

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

    def send_message(self, request, context):
        logger.info(f"Got request for sending message...\nRequest info:\n{request}")

        # replicate the message to the secondaries
        with grpc.insecure_channel('secondary-one:50052') as channel:
            logger.info(f"Replicating the message to the secondary-one...")
            stub = msg_replication_pb2_grpc.SecondaryLogStub(channel)
            s1_response = stub.replicate_message(
                msg_replication_pb2.MessageReplicationRequest(id=request.id, message=request.message)
            )
        
        with grpc.insecure_channel('secondary-two:50053') as channel:
            logger.info(f"Replicate message to secondary-two...")
            stub = msg_replication_pb2_grpc.SecondaryLogStub(channel)
            s2_response = stub.replicate_message(
                msg_replication_pb2.MessageReplicationRequest(id=request.id, message=request.message)
            )

        response = log_pb2.LogResponse()
        if s1_response.received and s2_response.received:
            response.received = True
        else:
            response.received = False

        if response.received:
            self.MESSAGE_LIST.append(request.message)

        response.message = request.message
        return response
    
    def list_messages(self, request, context):
        logger.info(f"Got request for list messages...")
        response = log_pb2.MessageList(messages=self.MESSAGE_LIST)

        return response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    log_pb2_grpc.add_LogServicer_to_server(LogServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    logger.info("Server started!")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
