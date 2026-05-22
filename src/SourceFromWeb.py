from typing import Iterator

from src.client import ClientBase
from src.task import Task


class SourceFromWeb:
    """
        Источник задач из интернета
    """

    def __init__(self, client: ClientBase) -> None:
        """
            Инициализатор источника задач из интернета
        """
        self.client = client

    def get_tasks(self) -> Iterator[Task | None]:
        """
            Функция получения задач из интернета
        """

        try:
            if isinstance(self.client, ClientBase):
                for col in range(0, 2):
                    el: Task = self.client.get_task()
                    yield el
            else:
                raise TypeError
        except Exception:
            yield None
