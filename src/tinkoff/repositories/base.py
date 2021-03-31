from __future__ import annotations

from typing import Any, Protocol


class BaseRepository(Protocol):
    def get_required_budget(self) -> Any:
        ...
