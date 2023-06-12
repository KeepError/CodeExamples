# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import users_services_pb2 as users__services__pb2


class UsersServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetById = channel.unary_unary(
                '/UsersService/GetById',
                request_serializer=users__services__pb2.GetByIdRequest.SerializeToString,
                response_deserializer=users__services__pb2.GetByIdResponse.FromString,
                )
        self.Create = channel.unary_unary(
                '/UsersService/Create',
                request_serializer=users__services__pb2.CreateRequest.SerializeToString,
                response_deserializer=users__services__pb2.CreateResponse.FromString,
                )


class UsersServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UsersServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetById': grpc.unary_unary_rpc_method_handler(
                    servicer.GetById,
                    request_deserializer=users__services__pb2.GetByIdRequest.FromString,
                    response_serializer=users__services__pb2.GetByIdResponse.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=users__services__pb2.CreateRequest.FromString,
                    response_serializer=users__services__pb2.CreateResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'UsersService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class UsersService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/UsersService/GetById',
            users__services__pb2.GetByIdRequest.SerializeToString,
            users__services__pb2.GetByIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/UsersService/Create',
            users__services__pb2.CreateRequest.SerializeToString,
            users__services__pb2.CreateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
