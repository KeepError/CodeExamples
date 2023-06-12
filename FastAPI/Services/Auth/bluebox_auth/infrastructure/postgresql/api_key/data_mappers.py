from domain.api_key.entities import ApiKey, UserApiKey
from .models import ApiKeyModel, UserApiKeyModel


class ApiKeyDataMapper:
    @staticmethod
    def model_to_entity(model: ApiKeyModel) -> ApiKey:
        return ApiKey(
            key_id=model.key_id,
            name=model.name,
            description=model.description,
            hashed_value=model.hashed_value,
            created_at=model.created_at
        )

    @staticmethod
    def entity_to_model(entity: ApiKey) -> ApiKeyModel:
        return ApiKeyModel(
            key_id=entity.key_id,
            name=entity.name,
            description=entity.description,
            hashed_value=entity.hashed_value,
            created_at=entity.created_at
        )


class UserApiKeyDataMapper:
    @staticmethod
    def model_to_entity(model: UserApiKeyModel, api_key_entity: ApiKey) -> UserApiKey:
        return UserApiKey(
            api_key=api_key_entity,
            user_id=model.user_id
        )

    @staticmethod
    def entity_to_model(entity: UserApiKey) -> UserApiKeyModel:
        return UserApiKeyModel(
            key_id=entity.api_key.key_id,
            user_id=entity.user_id
        )
