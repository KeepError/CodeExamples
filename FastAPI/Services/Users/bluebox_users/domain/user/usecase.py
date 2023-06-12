import uuid

from domain.usecase import UseCaseResult
from .entities import User
from .errors import UserNotFoundError
from .repositories import IUserRepository


class UserUseCase:
    user_repository: IUserRepository

    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    def get_list(self, offset: int, limit: int) -> UseCaseResult[list[User]]:
        return UseCaseResult.success(self.user_repository.get_list(offset, limit))

    def get_by_id(self, user_id: uuid.UUID) -> UseCaseResult[User]:
        user = self.user_repository.get_by_id(user_id)
        if not user:
            return UseCaseResult.failure(UserNotFoundError())
        return UseCaseResult.success(user)

    def create(self) -> UseCaseResult[User]:
        user = User(
            user_id=self.user_repository.next_user_id(),
            email="",
            balance=0,
        )
        user = self.user_repository.create(user)
        return UseCaseResult.success(user)
