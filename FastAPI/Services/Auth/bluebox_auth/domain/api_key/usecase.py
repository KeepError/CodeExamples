import secrets
import uuid
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Optional

from passlib.hash import pbkdf2_sha256

from domain.usecase import UseCaseResult
from .entities import ApiKey, UserApiKey
from .errors import NotAuthorizedError, InvalidApiKeyError, ApiKeyNotFoundError
from .repositories import IUserApiKeyRepository


class ApiKeyType(Enum):
    UserApiKey = "bbp"
    ApplicationApiKey = "bba"


@dataclass
class ApiKeyData:
    key_type: ApiKeyType
    key_id: str
    key_value: str

    def check_type(self, key_type: ApiKeyType) -> bool:
        return self.key_type == key_type

    def hashed_value(self) -> str:
        return pbkdf2_sha256.hash(self.key_value)

    def verify(self, hashed_value: str) -> bool:
        return pbkdf2_sha256.verify(self.key_value, hashed_value)

    @staticmethod
    def create(key_type: ApiKeyType, key_id: str) -> "ApiKeyData":
        key_value = secrets.token_hex(10)
        return ApiKeyData(key_type=key_type, key_id=key_id, key_value=key_value)

    @staticmethod
    def from_string(api_key: str) -> Optional["ApiKeyData"]:
        key_parts = api_key.split("_")
        if len(key_parts) != 3:
            return

        try:
            key_type = ApiKeyType(key_parts[0])
        except ValueError:
            return
        key_id = key_parts[1]
        key_value = key_parts[2]
        return ApiKeyData(key_type=key_type, key_id=key_id, key_value=key_value)

    def to_string(self) -> str:
        return f"{self.key_type.value}_{self.key_id}_{self.key_value}"


class UserApiKeyUseCase:
    user_api_key_repository: IUserApiKeyRepository

    def __init__(self, user_api_key_repository: IUserApiKeyRepository):
        self.user_api_key_repository = user_api_key_repository

    def authenticate_user(self, api_key: str) -> UseCaseResult[uuid.UUID]:
        api_key_data = ApiKeyData.from_string(api_key)
        if not api_key_data or not api_key_data.check_type(ApiKeyType.UserApiKey):
            return UseCaseResult.failure(InvalidApiKeyError())

        user_api_key = self.user_api_key_repository.get_by_key_id(api_key_data.key_id)
        if not user_api_key:
            return UseCaseResult.failure(NotAuthorizedError())

        if not api_key_data.verify(user_api_key.api_key.hashed_value):
            return UseCaseResult.failure(NotAuthorizedError())

        return UseCaseResult.success(user_api_key.user_id)

    def create_api_key(self, user_id: uuid.UUID, name: str, description: str) -> UseCaseResult[str]:
        api_key_id = self.user_api_key_repository.next_api_key_id()
        api_key_data = ApiKeyData.create(ApiKeyType.UserApiKey, api_key_id)
        api_key = ApiKey(
            key_id=api_key_id,
            name=name,
            description=description,
            hashed_value=api_key_data.hashed_value(),
            created_at=datetime.now()
        )
        user_api_key = UserApiKey(
            user_id=user_id,
            api_key=api_key
        )
        self.user_api_key_repository.add(user_api_key)

        return UseCaseResult.success(api_key_data.to_string())

    def get_user_api_keys(self, user_id: uuid.UUID) -> UseCaseResult[list[UserApiKey]]:
        user_api_keys = self.user_api_key_repository.get_user_api_keys(user_id)
        return UseCaseResult.success(user_api_keys)

    def get_api_key(self, key_id: str) -> UseCaseResult[UserApiKey]:
        user_api_key = self.user_api_key_repository.get_by_key_id(key_id)
        if not user_api_key:
            return UseCaseResult.failure(ApiKeyNotFoundError())
        return UseCaseResult.success(user_api_key)

    def delete_api_key(self, key_id: str) -> UseCaseResult[UserApiKey]:
        user_api_key = self.user_api_key_repository.delete(key_id)
        if not user_api_key:
            return UseCaseResult.failure(ApiKeyNotFoundError())
        return UseCaseResult.success(user_api_key)
