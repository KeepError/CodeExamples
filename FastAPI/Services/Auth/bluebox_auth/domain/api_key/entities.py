import secrets
import uuid
from dataclasses import dataclass
from datetime import datetime


@dataclass
class ApiKey:
    key_id: str
    name: str
    description: str
    hashed_value: str
    created_at: datetime

    @staticmethod
    def next_id() -> str:
        return secrets.token_hex(5)


@dataclass
class UserApiKey:
    user_id: uuid.UUID
    api_key: ApiKey


@dataclass
class ApplicationApiKey:
    application_id: uuid.UUID
    api_key: ApiKey
