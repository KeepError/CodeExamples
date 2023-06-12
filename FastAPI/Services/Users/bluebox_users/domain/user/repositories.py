import uuid
from abc import ABC, abstractmethod
from typing import Optional

from domain.user.entities import User


class IUserRepository(ABC):
    @abstractmethod
    def create(self, user: User) -> User:
        raise NotImplementedError

    @abstractmethod
    def get_list(self, offset: int, limit: int) -> list[User]:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, user_id: uuid.UUID) -> Optional[User]:
        raise NotImplementedError

    @abstractmethod
    def next_user_id(self) -> uuid.UUID:
        raise NotImplementedError
