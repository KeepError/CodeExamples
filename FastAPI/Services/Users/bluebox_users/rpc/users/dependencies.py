from typing import Generator
from contextlib import contextmanager

from domain.user.usecase import UserUseCase
from infrastructure.postgresql.database import get_session
from infrastructure.postgresql.user.repositories import UserRepository


@contextmanager
def get_user_use_case() -> Generator[UserUseCase, None, None]:
    with get_session() as session:
        yield UserUseCase(UserRepository(session))
