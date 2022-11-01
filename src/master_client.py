import grpc
from google.protobuf import empty_pb2

import log_pb2
import log_pb2_grpc


def run():
    message_id = 1
    while True:
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = log_pb2_grpc.LogStub(channel)
            command = input("Input command (append or list): ")

            match command:
                case "append":
                    message = input("Input your message: ")
                    if message:
                        response = stub.send_message(log_pb2.LogRequest(id=message_id, message=message))
                        print(f"Message received: {response}")
                        message_id += 1

                case "list":
                    response = stub.list_messages(empty_pb2.Empty())
                    print(f"List of messages: {response.messages}")


if __name__ == "__main__":
    run()
