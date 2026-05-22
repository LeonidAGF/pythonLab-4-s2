import pytest

from src.SourceFromFile import SourceFromFile


@pytest.mark.asyncio
async def test_source_from_file():
    """
    Тесты для SourceFromFile
    """
    sff1: SourceFromFile = SourceFromFile("./tests/test_cat_function.py")
    sff2: SourceFromFile = SourceFromFile("./tests/test_cat_function.py")
    sff3: SourceFromFile = SourceFromFile("./tests/test_cat_function.py")

    assert len([task async for task in sff1.get_tasks()]) != 0
    assert len([task async for task in sff2.get_tasks()]) != 0
    assert [task async for task in sff1.get_tasks()][0] == [
        task async for task in sff2.get_tasks()
    ][0]
    assert len([task async for task in sff3.get_tasks()]) != 0
