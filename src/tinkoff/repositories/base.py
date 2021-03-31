from typing import Protocol


class BaseRepository(Protocol):
    def get_required_budget(self):
        ...
