from typing import Protocol, runtime_checkable
from src.task import Task

@runtime_checkable
class TaskSource(Protocol):
    """
        Шаблон источника задачи
    """
    def get_tasks(self) -> list[Task] | None:
        """
            функция необходимая для получения задач
        """
        pass
