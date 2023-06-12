from typing import Annotated

from fastapi import Depends
from fastapi.security import APIKeyHeader

from api.v1.auth.dependencies import get_auth_api_keys_service
from api.v1.auth.errors import InvalidApiKeyApiError, NotAuthorizedApiError
from api.v1.user.dependencies import get_users_service
from infrastructure.services.auth.api_keys import UserApiKeyAuthService, InvalidApiKeyError, NotAuthorizedError
from infrastructure.services.users.users import User, UsersService

api_key = APIKeyHeader(name="Authorization", auto_error=False)


def get_current_user(
        users_service: Annotated[UsersService, Depends(get_users_service)],
        auth_api_keys_service: Annotated[UserApiKeyAuthService, Depends(get_auth_api_keys_service)],
        access_token: str = Depends(api_key),
) -> User:
    if not access_token:
        raise NotAuthorizedApiError()
    try:
        user_id = auth_api_keys_service.authenticate_user(access_token)
    except InvalidApiKeyError:
        raise InvalidApiKeyApiError()
    except NotAuthorizedError:
        raise NotAuthorizedApiError()
    user = users_service.get_by_id(user_id)
    return user
