from typing import Callable, Generator, Iterator

from src.Source import TaskSource
from src.task import Task
from task import Task


class TaskQueue:
    """
        очередь задач
    """

    def __init__(self, source: TaskSource) -> None:
        """
            ункция для инициализации атрибутов
        """
        self.source: TaskSource = source

    def __iter__(self) -> Iterator[Task]:
        """
            функция для итерации по задачам из источника
        """
        itr = iter(self.source.get_tasks())
        while True:
            try:
                item = next(itr)
                yield item
            except StopIteration:
                break

    def filtration(self, func: Callable[[Task], bool]) -> Generator[Task]:
        """
            функция реализующая ленивый фильтр
        """
        for task in self:
            if func(task):
                yield task
