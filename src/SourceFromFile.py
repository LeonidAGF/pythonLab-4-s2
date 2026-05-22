import asyncio
from typing import Dict, Any, AsyncGenerator
from src.task import Task
import aiofiles


class SourceFromFile:
    """
    Источник задач из файла
    """

    def __init__(self, path: str) -> None:
        """
        Инициализатор для источника задач из файла
        """
        self.path = path

    async def get_tasks(self) -> AsyncGenerator[Task | None, Any]:
        """
        функция получения задач
        """
        try:
            data: Dict[str, str] = {}
            async with aiofiles.open(self.path, "r") as f:
                data["text"] = await f.read()
            task: Task = Task(489652, "description", data, 1)
            await asyncio.sleep(0.5)
            yield task
        except Exception:
            await asyncio.sleep(0.5)
            yield None
