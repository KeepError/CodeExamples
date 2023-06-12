from fastapi import status

from ..errors import ApiError


class InvalidApiKeyApiError(ApiError):
    error_message = "Invalid API key"
    error_code = 2
    http_status_code = status.HTTP_403_FORBIDDEN


class NotAuthorizedApiError(ApiError):
    error_message = "Not authorized"
    error_code = 3
    http_status_code = status.HTTP_403_FORBIDDEN
