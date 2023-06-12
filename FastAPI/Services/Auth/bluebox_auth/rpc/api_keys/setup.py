import grpc


def setup_api_key(server: grpc.Server):
    from rpc.api_keys.implementation import UserApiKeyAuthService
    from rpc.api_keys.proto import api_keys_services_pb2_grpc
    api_keys_services_pb2_grpc.add_UserApiKeyAuthServiceServicer_to_server(UserApiKeyAuthService(), server)
