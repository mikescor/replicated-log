import grpc
from google.protobuf import empty_pb2

import msg_replication_pb2_grpc


def run_secondary_client():
    while True:
        client = input("Input client (one or two): ")

        match client:
            case "one":
                port = "50052"
            case "two":
                port = "50053"
            case _:
                raise NotImplementedError("Only two options are allowed (one or two)!")

        with grpc.insecure_channel(f'localhost:{port}') as channel:
            stub = msg_replication_pb2_grpc.SecondaryLogStub(channel)
            response = stub.get_messages(empty_pb2.Empty())
            print(f"List of messages: {response.messages}")


if __name__ == "__main__":
    run_secondary_client()
