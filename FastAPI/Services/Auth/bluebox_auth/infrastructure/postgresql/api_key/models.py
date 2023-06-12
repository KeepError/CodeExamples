from datetime import datetime
from typing import Union
import uuid

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.postgresql import UUID

from ..database import Base


class ApiKeyModel(Base):
    __tablename__ = "api_keys"
    key_id: Union[str, Column] = Column(String(10), primary_key=True)
    name: Union[str, Column] = Column(String(64))
    description: Union[str, Column] = Column(String(256))
    hashed_value: Union[str, Column] = Column(String(128))
    created_at: Union[datetime, Column] = Column(DateTime)


class UserApiKeyModel(Base):
    __tablename__ = "user_api_keys"
    key_id: Union[str, Column] = Column(String(10), ForeignKey("api_keys.key_id"), primary_key=True)
    user_id: Union[uuid.UUID, Column] = Column(UUID(as_uuid=True))
