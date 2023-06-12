from rpc.users.proto import users_objects_pb2
from rpc.users.proto import users_services_pb2
from rpc.users.proto import users_services_pb2_grpc
from rpc.users.dependencies import get_user_use_case
from domain.user.errors import UserNotFoundError
from rpc.users.data_mappers import UserDataMapper


class UsersService(users_services_pb2_grpc.UsersServiceServicer):
    def GetById(self, request, context):
        user_id = request.user_id
        with get_user_use_case() as user_use_case:
            result = user_use_case.get_by_id(user_id)

        if not result.is_success():
            error = users_objects_pb2.UsersError.UNKNOWN_USERS_ERROR
            if isinstance(result.error, UserNotFoundError):
                error = users_objects_pb2.UsersError.USER_NOT_FOUND
            return users_services_pb2.GetByIdResponse(error=error)

        user = UserDataMapper.entity_to_proto_model(result.payload)
        return users_services_pb2.GetByIdResponse(user=user)

    def Create(self, request, context):
        with get_user_use_case() as user_use_case:
            result = user_use_case.create()

        if not result.is_success():
            error = users_objects_pb2.UsersError.UNKNOWN_USERS_ERROR
            return users_services_pb2.CreateResponse(error=error)

        user = UserDataMapper.entity_to_proto_model(result.payload)
        return users_services_pb2.CreateResponse(user=user)
