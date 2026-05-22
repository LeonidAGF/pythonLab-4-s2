import pytest
from src.client import ClientGet as Client
from src.SourceFromWeb import SourceFromWeb

@pytest.mark.asyncio
async def test_source_from_web():
    """
    Тесты для SourceFromWeb.
    """

    client_ok = Client("https://ru.wikipedia.org/wiki/Python")
    client_bad = Client("fcghvjbknjlm;")

    source_ok1 = SourceFromWeb(client_ok)
    source_ok2 = SourceFromWeb(client_ok)
    source_bad = SourceFromWeb(client_bad)

    tasks1 = [task async for task in source_ok1.get_tasks()]
    tasks2 = [task async for task in source_ok2.get_tasks()]
    assert len(tasks1) > 0
    assert tasks1[0] is not None
    assert tasks1[0].payload == tasks2[0].payload
    bad_tasks = [task async for task in source_bad.get_tasks()]
    assert len(bad_tasks) == 2
    assert bad_tasks[0] is None