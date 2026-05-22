import pytest

from src.SourceFromWeb import SourceFromWeb
from src.client import ClientGet as Client
from src.async_task_runner import AsyncTaskRunner
from src.task_async_manager import TaskStringManager
from src.task_queue import AsyncTaskQueue


@pytest.mark.asyncio
async def test_runner():
    """
    Тесты для AsyncTaskRunner
    """
    try:
        client1 = Client(
            "https://my.meteoblue.com/packages/basic-1h_basic-day?apikey=bOico7hWTVAzPQYM&lat=55.752&lon=37.6178&asl=155&format=json"
        )
        source_from_web1 = SourceFromWeb(client1)

        tq = AsyncTaskQueue()
        async for el in source_from_web1.get_tasks():
            await tq.put(el)

        runnner: AsyncTaskRunner = AsyncTaskRunner(tq, TaskStringManager())
        await runnner.run(2)

        assert True
    except Exception:
        assert False
