import uuid

from pydantic import BaseModel


class ApiKeySchema(BaseModel):
    api_key: str


class ApiKeyIdSchema(BaseModel):
    key_id: str


class ApiKeyDetailsSchema(BaseModel):
    name: str
    description: str


class UserApiKeyDetailsSchema(ApiKeyDetailsSchema):
    user_id: uuid.UUID
