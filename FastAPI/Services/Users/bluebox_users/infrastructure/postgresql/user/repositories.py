import uuid
from typing import Optional

from sqlalchemy.orm.session import Session

from domain.user.entities import User
from domain.user.repositories import IUserRepository
from .data_mappers import UserDataMapper
from .models import UserModel


class UserRepository(IUserRepository):
    session: Session

    def __init__(self, session: Session):
        self.session = session

    def create(self, user: User) -> User:
        user_model = UserDataMapper.entity_to_model(user)
        self.session.add(user_model)
        self.session.commit()
        return UserDataMapper.model_to_entity(user_model)

    def get_list(self, offset: int, limit: int) -> list[User]:
        user_models = self.session.query(UserModel).offset(offset).limit(limit).all()
        return list(map(UserDataMapper.model_to_entity, user_models))

    def get_by_id(self, user_id: uuid.UUID) -> Optional[User]:
        user_model = self.session.query(UserModel).filter_by(user_id=user_id).one_or_none()
        if user_model:
            return UserDataMapper.model_to_entity(user_model)
        return None

    def next_user_id(self) -> uuid.UUID:
        return User.next_id()
