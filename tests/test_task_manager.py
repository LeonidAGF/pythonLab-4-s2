import pytest

from src.client import ClientGet as Client
from src.task import Task
from src.SourceFromFile import SourceFromFile
from src.SourceFromGenerator import SourceFromGenerator
from src.SourceFromWeb import SourceFromWeb
from src.task_manager import task_manager


@pytest.mark.asyncio
async def test_task_manager():
    """
    Тесты для task_manager
    """
    client = Client("https://ru.wikipedia.org/wiki/Python")

    source_from_web = SourceFromWeb(client)
    source_from_file = SourceFromFile("text")
    source_from_generators = SourceFromGenerator(1)
    task: Task = Task(1, "", {}, 1)

    try:
        for _el in await task_manager(source_from_web):
            pass
        for _el in await task_manager(source_from_file):
            pass
        for _el in await task_manager(source_from_generators):
            pass
        assert True
    except Exception:
        assert False

    try:
        for _el in await task_manager(task):
            pass
        assert False
    except Exception:
        assert True
