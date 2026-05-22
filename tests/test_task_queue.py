import pytest
from src.task import Task
from src.task_queue import AsyncTaskQueue
import asyncio

@pytest.mark.asyncio
async def test_queue() -> None:
    """
       тесты на  AsyncTaskQueue
    """
    queue = AsyncTaskQueue()
    task = Task(45612, 'description', {"to": "a@b.com"}, (1%2)+1)

    await queue.put(task)
    result = await queue.get()

    assert result is task
    assert result.payload == {"to": "a@b.com"}

    task1 = Task(45612, 'description', {"delayed": "delayed"}, (1%2)+1)

    async def delayed_put():
        await asyncio.sleep(0.1)
        await queue.put(task1)

    asyncio.create_task(delayed_put())
    result = await queue.get()
    assert result is task1