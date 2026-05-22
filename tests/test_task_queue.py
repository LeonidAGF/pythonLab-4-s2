from src.client import ClientGet as Client
from src.SourceFromWeb import SourceFromWeb
from src.task import Task
from src.task_queue import TaskQueue


def filter_by_status(task: Task):
    if task.status == 'ready':
        return True
    return False


def test_task_queue():
    """
        Тесты для task_queue
    """

    cclient1 = Client("https://my.meteoblue.com/packages/basic-1h_basic-day?apikey=bOico7hWTVAzPQYM&lat=55.752&lon=37.6178&asl=155&format=json")

    source_from_web1 = SourceFromWeb(cclient1)

    tq = TaskQueue(source_from_web1)

    assert list(tq)[0].id==list(tq)[0].id
    assert len(list(tq.filtration(filter_by_status)))==0

    sum_of_priority: int = sum(el.priority for el in tq)
    sum_of_priority1: int = sum(el.priority for el in tq)

    assert sum_of_priority==sum_of_priority1
