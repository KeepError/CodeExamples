from rpc.api_keys.proto import api_keys_objects_pb2
from rpc.api_keys.proto import api_keys_services_pb2
from rpc.api_keys.proto import api_keys_services_pb2_grpc
from domain.api_key.errors import NotAuthorizedError, InvalidApiKeyError, ApiKeyNotFoundError
from rpc.api_keys.dependencies import get_user_use_case
from rpc.api_keys.data_mappers import ApiKeyNoHashedValueDataMapper


class UserApiKeyAuthService(api_keys_services_pb2_grpc.UserApiKeyAuthServiceServicer):
    def AuthenticateUser(self, request, context):
        with get_user_use_case() as user_api_key_use_case:
            result = user_api_key_use_case.authenticate_user(request.api_key_string)

        if not result.is_success():
            error = api_keys_objects_pb2.AuthApiKeysError.UNKNOWN_AUTH_API_KEYS_ERROR
            if isinstance(result.error, InvalidApiKeyError):
                error = api_keys_objects_pb2.AuthApiKeysError.INVALID_API_KEY
            if isinstance(result.error, NotAuthorizedError):
                error = api_keys_objects_pb2.AuthApiKeysError.NOT_AUTHORIZED
            return api_keys_services_pb2.AuthenticateUserResponse(error=error)

        return api_keys_services_pb2.AuthenticateUserResponse(user_id=str(result.payload))

    def CreateUserApiKey(self, request, context):
        with get_user_use_case() as user_api_key_use_case:
            result = user_api_key_use_case.create_api_key(
                user_id=request.user_id,
                name=request.name,
                description=request.description
            )
        api_key_string = result.payload

        return api_keys_services_pb2.CreateUserApiKeyResponse(
            api_key_string=api_key_string
        )

    def DeleteUserApiKey(self, request, context):
        with get_user_use_case() as user_api_key_use_case:
            result = user_api_key_use_case.delete_api_key(
                key_id=request.key_id
            )

        if not result.is_success():
            error = api_keys_objects_pb2.AuthApiKeysError.UNKNOWN_AUTH_API_KEYS_ERROR
            if isinstance(result.error, ApiKeyNotFoundError):
                error = api_keys_objects_pb2.AuthApiKeysError.API_KEY_NOT_FOUND
            return api_keys_services_pb2.DeleteUserApiKeyResponse(error=error)

        user_api_key_entity = result.payload
        api_key = ApiKeyNoHashedValueDataMapper.entity_to_proto_model(user_api_key_entity.api_key)
        return api_keys_services_pb2.DeleteUserApiKeyResponse(api_key=api_key)

    def GetUserApiKeysList(self, request, context):
        with get_user_use_case() as user_api_key_use_case:
            result = user_api_key_use_case.get_user_api_keys(
                user_id=request.user_id
            )

        user_api_key_entities = result.payload
        api_keys = []
        for user_api_key_entity in user_api_key_entities:
            api_keys.append(ApiKeyNoHashedValueDataMapper.entity_to_proto_model(user_api_key_entity.api_key))
        return api_keys_services_pb2.GetUserApiKeysListResponse(api_keys=api_keys)

    def GetUserApiKey(self, request, context):
        with get_user_use_case() as user_api_key_use_case:
            result = user_api_key_use_case.get_api_key(
                key_id=request.key_id
            )

        if not result.is_success():
            error = api_keys_objects_pb2.AuthApiKeysError.UNKNOWN_AUTH_API_KEYS_ERROR
            if isinstance(result.error, ApiKeyNotFoundError):
                error = api_keys_objects_pb2.AuthApiKeysError.API_KEY_NOT_FOUND
            return api_keys_services_pb2.GetUserApiKeyResponse(error=error)

        user_api_key_entity = result.payload
        api_key = ApiKeyNoHashedValueDataMapper.entity_to_proto_model(user_api_key_entity.api_key)
        return api_keys_services_pb2.GetUserApiKeyResponse(api_key=api_key)
