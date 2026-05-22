from asyncio import Queue

from src.task import Task


class AsyncTaskQueue:
    """
    Асинхронная очередь задач
    """

    def __init__(self) -> None:
        self._queue: Queue[Task] = Queue()

    async def put(self, task: Task) -> None:
        """
        Добавить задачу в очередь
        """
        await self._queue.put(task)

    async def get(self) -> Task:
        """
        получить задачу из очереди
        """
        return await self._queue.get()
