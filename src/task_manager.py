from src.Source import TaskSource
from src.task import Task


async def task_manager(source: TaskSource) -> list[Task]:
    """
    Функция получения задач из источника любого типа
    """
    if isinstance(source, TaskSource):
        list = []
        async for el in source.get_tasks():
            list.append(el)
        return list
    raise TypeError
