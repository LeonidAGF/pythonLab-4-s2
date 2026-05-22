from src.client import ClientGet as Client
from src.SourceFromWeb import SourceFromWeb


def test_source_from_web():
    """
        Тесты для SourceFromWeb
    """

    client1 = Client("https://ru.wikipedia.org/wiki/Python")
    client2 = Client("fcghvjbknjlm;")

    sff1:SourceFromWeb = SourceFromWeb(client1)
    sff2:SourceFromWeb = SourceFromWeb(client1)
    sff3:SourceFromWeb = SourceFromWeb(client2)

    assert len(list(sff1.get_tasks()))!=0
    assert len(list(sff2.get_tasks()))!=0
    assert list(sff1.get_tasks())[0].id==list(sff2.get_tasks())[0].id
    assert None in sff3.get_tasks()
