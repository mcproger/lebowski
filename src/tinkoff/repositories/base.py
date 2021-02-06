import abc
from typing import Protocol


class BaseRepository(Protocol):
    @abc.abstractclassmethod
    def get_required_budget(self):
        raise NotImplementedError
