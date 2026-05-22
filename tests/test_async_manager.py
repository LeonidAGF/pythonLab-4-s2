import pytest

from src.task import Task
from src.task_async_manager import TaskStringManager


@pytest.mark.asyncio
async def test_async_manager():
    """
    Тесты для TaskStringManager
    """
    tm = TaskStringManager()
    task = Task(1, "", {"task": "0"}, 1)
    res = (await tm.do(task)).payload["last_content"] is not None
    assert res == 1
