from __future__ import annotations

from typing import Any, Protocol


class BaseNotifier(Protocol):
    def notify(self, *args: Any, **kwargs: Any) -> None:
        ...
