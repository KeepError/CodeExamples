import uuid

from pydantic import BaseModel


class UserBaseSchema(BaseModel):
    pass


class UserSchema(UserBaseSchema):
    user_id: uuid.UUID
    email: str
