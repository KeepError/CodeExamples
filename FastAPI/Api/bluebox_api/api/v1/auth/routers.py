from typing import Annotated

from fastapi import APIRouter, Depends

from infrastructure.services.auth.api_keys import UserApiKeyAuthService
from .dependencies import get_auth_api_keys_service
from .schemas import ApiKeySchema, UserApiKeyDetailsSchema, ApiKeyIdSchema, ApiKeyDetailsSchema

auth_router = APIRouter(prefix="/auth", tags=["auth"])


@auth_router.post("", response_model=ApiKeySchema)
def create_user_api_key(
        auth_api_keys_service: Annotated[UserApiKeyAuthService, Depends(get_auth_api_keys_service)],
        user_api_key: UserApiKeyDetailsSchema
):
    api_key = auth_api_keys_service.create_user_api_key(
        user_id=user_api_key.user_id,
        name=user_api_key.name,
        description=user_api_key.description
    )
    return ApiKeySchema(api_key=api_key)


@auth_router.put("", response_model=ApiKeyDetailsSchema)
def get_user_api_key(
        auth_api_keys_service: Annotated[UserApiKeyAuthService, Depends(get_auth_api_keys_service)],
        api_key_id: ApiKeyIdSchema
):
    api_key = auth_api_keys_service.get_user_api_key(
        key_id=api_key_id.key_id
    )
    return ApiKeyDetailsSchema(name=api_key.name, description=api_key.description)
