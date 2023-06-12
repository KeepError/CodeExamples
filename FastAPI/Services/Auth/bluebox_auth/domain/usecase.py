from dataclasses import dataclass
from typing import Generic, TypeVar

from .errors import DomainError

T = TypeVar("T")


@dataclass
class UseCaseResult(Generic[T]):
    payload: T = None
    error: DomainError = None

    def is_success(self) -> bool:
        return self.error is None

    @classmethod
    def success(cls, payload: T = None) -> "UseCaseResult":
        return UseCaseResult(payload=payload)

    @classmethod
    def failure(cls, error: DomainError) -> "UseCaseResult":
        return UseCaseResult(error=error)
