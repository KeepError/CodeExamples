from contextlib import contextmanager
from typing import Generator

from domain.api_key.usecase import UserApiKeyUseCase
from infrastructure.postgresql.api_key.repositories import UserApiKeyRepository
from infrastructure.postgresql.database import get_session


@contextmanager
def get_user_use_case() -> Generator[UserApiKeyUseCase, None, None]:
    with get_session() as session:
        yield UserApiKeyUseCase(UserApiKeyRepository(session))
