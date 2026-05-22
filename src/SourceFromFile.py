from typing import Dict, Iterator
from src.task import Task
from src.cat_function import cat


class SourceFromFile:
    """
        Источник задач из файла
    """

    def __init__(self, path: str) -> None:
        """
            Инициализатор для источника задач из файла
        """
        self.path = path

    def get_tasks(self) -> Iterator[Task | None]:
        """
            функция получения задач
        """
        try:
            data: Dict[str, str] = {}
            data["text"] = cat(self.path)
            task: Task = Task(489652,'description', data,1)
            yield task
        except Exception:
            yield None
