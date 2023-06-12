from typing import Iterator

from config import Config
from infrastructure.services.auth.api_keys import UserApiKeyAuthService


def get_auth_api_keys_service() -> Iterator[UserApiKeyAuthService]:
    yield UserApiKeyAuthService(Config.AUTH_SERVICE_URL)
