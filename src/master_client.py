import grpc
from google.protobuf import empty_pb2

import log_pb2
import log_pb2_grpc


def run():
    message_id = 1
    while True:
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = log_pb2_grpc.LogStub(channel)
            try:
                command = int(input("\n 1. Append msg\n 2. List msgs\n 3. Append msg with write concern:\n\nInput a number of the command: "))

                match command:
                    case 1:
                        message = input("Input your message: ")
                        if message:
                            response = stub.send_message(log_pb2.LogRequest(id=message_id, message=message))
                            message_id += 1
                            if response.received:
                                print(f"\nMessage received: {response.message}")                            
                            else:
                                print(f"\nMessage wasn't received: {response.message}")
                    case 2:
                        response = stub.list_messages(empty_pb2.Empty())
                        print(f"List of messages: {response.messages}")
                    case 3:
                        message = input("Input your message: ")
                        write_concern = int(input("Input a write concern: "))
                        if message and write_concern:
                            response = stub.send_message(log_pb2.LogRequest(id=message_id, message=message, write_concern=write_concern))
                            message_id += 1
                            if response.received:
                                print(f"\nMessage received: {response.message}")                            
                            else:
                                print(f"\nMessage wasn't received: {response.message}")
            except KeyboardInterrupt:
                print("\nKeyboardInterrupt\n")
                channel.unsubscribe(close)
                exit()


def close(channel):
    "Close the channel"
    channel.close()


if __name__ == "__main__":
    run()
