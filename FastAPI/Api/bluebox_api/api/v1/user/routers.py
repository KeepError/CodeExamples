import uuid
from typing import Annotated

from fastapi import APIRouter, Depends

from api.v1.dependencies import get_current_user
from infrastructure.services.users.users import UserNotFoundError
from infrastructure.services.users.users import UsersService
from .dependencies import get_users_service
from .errors import UserNotFoundApiError
from .schemas import UserSchema

users_router = APIRouter(prefix="/users", tags=["users"])


@users_router.get("/me", response_model=UserSchema)
def me(
        user: UserSchema = Depends(get_current_user)
):
    return UserSchema(user_id=user.user_id, email=user.email)


@users_router.get("/{user_id}", response_model=UserSchema)
def get_user(
        users_service: Annotated[UsersService, Depends(get_users_service)],
        user_id: uuid.UUID
):
    try:
        user = users_service.get_by_id(user_id)
        return UserSchema(user_id=user.user_id, email=user.email)
    except UserNotFoundError:
        raise UserNotFoundApiError()
