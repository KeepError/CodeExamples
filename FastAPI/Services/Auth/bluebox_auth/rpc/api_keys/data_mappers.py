from google.protobuf.timestamp_pb2 import Timestamp

from domain.api_key.entities import ApiKey
from .proto import api_keys_objects_pb2


class ApiKeyNoHashedValueDataMapper:
    @staticmethod
    def entity_to_proto_model(entity: ApiKey) -> api_keys_objects_pb2.ApiKey:
        created_at = Timestamp()
        created_at.FromDatetime(entity.created_at)
        return api_keys_objects_pb2.ApiKey(
            key_id=entity.key_id,
            name=entity.name,
            description=entity.description,
            created_at=created_at,
        )
