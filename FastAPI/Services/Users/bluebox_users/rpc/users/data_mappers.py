from domain.user.entities import User
from .proto import users_objects_pb2


class UserDataMapper:
    @staticmethod
    def entity_to_proto_model(entity: User) -> users_objects_pb2.User:
        return users_objects_pb2.User(
            user_id=str(entity.user_id),
            email=entity.email,
            balance=entity.balance,
        )
