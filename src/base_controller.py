from __future__ import annotations

from abc import abstractmethod
from typing import Optional, Protocol


class BaseController(Protocol):
    """Interface for business-logic containers"""

    @abstractmethod
    def run(self) -> Optional[str]:
        raise NotImplementedError
