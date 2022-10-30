# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import log_pb2 as log__pb2


class LogStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.send_message = channel.unary_unary(
                '/Log/send_message',
                request_serializer=log__pb2.LogRequest.SerializeToString,
                response_deserializer=log__pb2.LogResponse.FromString,
                )
        self.list_messages = channel.unary_unary(
                '/Log/list_messages',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=log__pb2.MessageList.FromString,
                )


class LogServicer(object):
    """Missing associated documentation comment in .proto file."""

    def send_message(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def list_messages(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LogServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'send_message': grpc.unary_unary_rpc_method_handler(
                    servicer.send_message,
                    request_deserializer=log__pb2.LogRequest.FromString,
                    response_serializer=log__pb2.LogResponse.SerializeToString,
            ),
            'list_messages': grpc.unary_unary_rpc_method_handler(
                    servicer.list_messages,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=log__pb2.MessageList.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Log', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Log(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def send_message(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Log/send_message',
            log__pb2.LogRequest.SerializeToString,
            log__pb2.LogResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def list_messages(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Log/list_messages',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            log__pb2.MessageList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)