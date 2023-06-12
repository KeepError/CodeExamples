from typing import Optional

from sqlalchemy.orm.session import Session

from domain.api_key.entities import ApiKey, UserApiKey
from domain.api_key.repositories import IUserApiKeyRepository
from .data_mappers import ApiKeyDataMapper, UserApiKeyDataMapper
from .models import ApiKeyModel, UserApiKeyModel


class ApiKeyRepository:
    session: Session

    def __init__(self, session: Session):
        self.session = session

    def add(self, api_key: ApiKey):
        api_key_model = ApiKeyDataMapper.entity_to_model(api_key)
        self.session.add(api_key_model)
        self.session.commit()

    def get_by_key_id(self, key_id: str) -> Optional[ApiKey]:
        api_key_model = self.session.query(ApiKeyModel).filter_by(key_id=key_id).one_or_none()
        if api_key_model:
            return ApiKeyDataMapper.model_to_entity(api_key_model)
        return None

    def delete(self, key_id: str) -> Optional[ApiKey]:
        api_key_model = self.session.query(ApiKeyModel).filter_by(key_id=key_id).one_or_none()
        if not api_key_model:
            return None
        api_key = ApiKeyDataMapper.model_to_entity(api_key_model)
        self.session.delete(api_key_model)
        self.session.commit()
        return api_key

    def next_api_key_id(self) -> str:
        api_key_id = None
        while not api_key_id or self.session.query(ApiKeyModel).filter_by(key_id=api_key_id).one_or_none() is not None:
            api_key_id = ApiKey.next_id()
        return api_key_id


class UserApiKeyRepository(IUserApiKeyRepository):
    session: Session

    def __init__(self, session: Session):
        self.session = session
        self.api_key_repository = ApiKeyRepository(session)

    def add(self, user_api_key: UserApiKey) -> UserApiKey:
        self.api_key_repository.add(user_api_key.api_key)
        user_api_key_model = UserApiKeyDataMapper.entity_to_model(user_api_key)
        self.session.add(user_api_key_model)
        self.session.commit()
        return user_api_key

    def get_user_api_keys(self, user_id: int) -> list[UserApiKey]:
        user_api_key_models = self.session.query(UserApiKeyModel).filter_by(user_id=user_id).all()
        result = []
        for user_api_key_model in user_api_key_models:
            api_key = self.api_key_repository.get_by_key_id(user_api_key_model.key_id)
            result.append(UserApiKeyDataMapper.model_to_entity(user_api_key_model, api_key))
        return result

    def get_by_key_id(self, key_id: str) -> Optional[UserApiKey]:
        user_api_key_model = self.session.query(UserApiKeyModel).filter_by(key_id=key_id).one_or_none()
        if not user_api_key_model:
            return None
        api_key = self.api_key_repository.get_by_key_id(key_id)
        return UserApiKeyDataMapper.model_to_entity(user_api_key_model, api_key)

    def delete(self, key_id: str) -> Optional[UserApiKey]:
        user_api_key_model = self.session.query(UserApiKeyModel).filter_by(key_id=key_id).one_or_none()
        if not user_api_key_model:
            return None

        self.session.delete(user_api_key_model)
        self.session.commit()

        api_key = self.api_key_repository.delete(key_id)

        user_api_key = UserApiKeyDataMapper.model_to_entity(user_api_key_model, api_key)
        return user_api_key

    def next_api_key_id(self) -> str:
        return self.api_key_repository.next_api_key_id()
