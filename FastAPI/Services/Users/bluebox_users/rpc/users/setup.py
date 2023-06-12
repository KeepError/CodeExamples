import grpc


def setup_users(server: grpc.Server):
    from rpc.users.implementation import UsersService
    from rpc.users.proto import users_services_pb2_grpc
    users_services_pb2_grpc.add_UsersServiceServicer_to_server(UsersService(), server)
