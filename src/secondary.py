from concurrent import futures
import grpc

import msg_replication_pb2
import msg_replication_pb2_grpc


class SecondaryLogServicer(msg_replication_pb2_grpc.SecondaryLogServicer):
    MESSAGE_LIST = []

    def replicate_message(self, request, context):
        print(f"Got request for replicating message...\nRequest info:\n{request}")
        response = msg_replication_pb2.MessageReplicationResponse()
        response.message = request.message
        response.received = True
        self.MESSAGE_LIST.append(request.message)

        return response
    
    def get_messages(self, request, context):
        print(f"Got request for list messages...")
        response = msg_replication_pb2.ReplicatedMessageList(messages=self.MESSAGE_LIST)

        return response



def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    msg_replication_pb2_grpc.add_SecondaryLogServicer_to_server(SecondaryLogServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.add_insecure_port("[::]:50052")
    server.add_insecure_port("[::]:50053")
    server.start()
    print("Server started!")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
