import pytest

from src.task import Task
from src.task_async_manager import TaskStringManager


@pytest.mark.asyncio
async def test_async_manager():
    """
        Тесты для SourceFromFile
    """
    tm = TaskStringManager()
    task = Task(1,'',{"task":'0'},1)
    res = await tm.do(task)
    assert res >0 == 1
