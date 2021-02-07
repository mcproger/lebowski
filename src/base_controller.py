from abc import abstractmethod
from typing import Protocol, Optional


class BaseController(Protocol):
    """Interface for business-logic containers"""
    @abstractmethod
    def run(self) -> Optional[str]:
        raise NotImplementedError
