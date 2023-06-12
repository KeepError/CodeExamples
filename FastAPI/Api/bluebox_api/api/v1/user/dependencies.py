from typing import Iterator

from config import Config
from infrastructure.services.users.users import UsersService


def get_users_service() -> Iterator[UsersService]:
    yield UsersService(Config.USERS_SERVICE_URL)
