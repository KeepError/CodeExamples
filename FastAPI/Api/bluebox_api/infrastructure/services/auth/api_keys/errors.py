class Error(Exception):
    pass


class UnknownError(Error):
    pass


class NotAuthorizedError(Error):
    pass


class InvalidApiKeyError(Error):
    pass


class ApiKeyNotFoundError(Error):
    pass
