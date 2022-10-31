# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import msg_replication_pb2 as msg__replication__pb2


class SecondaryLogStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.replicate_message = channel.unary_unary(
                '/SecondaryLog/replicate_message',
                request_serializer=msg__replication__pb2.MessageReplicationRequest.SerializeToString,
                response_deserializer=msg__replication__pb2.MessageReplicationResponse.FromString,
                )
        self.get_messages = channel.unary_unary(
                '/SecondaryLog/get_messages',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=msg__replication__pb2.ReplicatedMessageList.FromString,
                )


class SecondaryLogServicer(object):
    """Missing associated documentation comment in .proto file."""

    def replicate_message(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_messages(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SecondaryLogServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'replicate_message': grpc.unary_unary_rpc_method_handler(
                    servicer.replicate_message,
                    request_deserializer=msg__replication__pb2.MessageReplicationRequest.FromString,
                    response_serializer=msg__replication__pb2.MessageReplicationResponse.SerializeToString,
            ),
            'get_messages': grpc.unary_unary_rpc_method_handler(
                    servicer.get_messages,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=msg__replication__pb2.ReplicatedMessageList.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'SecondaryLog', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SecondaryLog(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def replicate_message(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SecondaryLog/replicate_message',
            msg__replication__pb2.MessageReplicationRequest.SerializeToString,
            msg__replication__pb2.MessageReplicationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get_messages(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SecondaryLog/get_messages',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            msg__replication__pb2.ReplicatedMessageList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
