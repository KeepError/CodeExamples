from domain.errors import DomainError


class NotAuthorizedError(DomainError):
    pass


class InvalidApiKeyError(DomainError):
    pass


class ApiKeyNotFoundError(DomainError):
    pass
