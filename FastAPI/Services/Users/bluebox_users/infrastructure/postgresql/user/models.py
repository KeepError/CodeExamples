import uuid
from typing import Union

from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import UUID

from ..database import Base


class UserModel(Base):
    __tablename__ = "users"
    user_id: Union[uuid.UUID, Column] = Column(UUID(as_uuid=True), primary_key=True)
    email: Union[str, Column] = Column(String)
    balance: Union[int, Column] = Column(Integer)
