import uuid
from abc import ABC, abstractmethod
from typing import Optional

from domain.api_key.entities import UserApiKey


class IUserApiKeyRepository(ABC):
    @abstractmethod
    def add(self, user_api_key: UserApiKey) -> UserApiKey:
        raise NotImplementedError

    @abstractmethod
    def get_user_api_keys(self, user_id: uuid.UUID) -> list[UserApiKey]:
        raise NotImplementedError

    @abstractmethod
    def get_by_key_id(self, key_id: str) -> Optional[UserApiKey]:
        raise NotImplementedError

    @abstractmethod
    def delete(self, key_id: str) -> Optional[UserApiKey]:
        raise NotImplementedError

    @abstractmethod
    def next_api_key_id(self) -> str:
        raise NotImplementedError
