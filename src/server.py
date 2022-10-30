from concurrent import futures
import grpc

import log_pb2
import log_pb2_grpc

class LogServicer(log_pb2_grpc.LogServicer):
    MESSAGE_LIST = []

    def send_message(self, request, context):
        print(f"Got request for sending message...\nRequest info:\n{request}")
        response = log_pb2.LogResponse()
        response.message = request.message
        response.received = True
        self.MESSAGE_LIST.append(request.message)

        return response
    
    def list_messages(self, request, context):
        print(f"Got request for list messages...")
        response = log_pb2.MessageList(messages=self.MESSAGE_LIST)

        return response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    log_pb2_grpc.add_LogServicer_to_server(LogServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("Server started!")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()