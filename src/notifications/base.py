import abc
from typing import Any


class BaseNotifier(abc.ABC):
    @abc.abstractmethod
    def notify(self, *args: Any, **kwargs: Any) -> None:
        raise NotImplementedError
