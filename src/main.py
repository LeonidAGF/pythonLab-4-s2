from SourceFromFile import SourceFromFile
from SourceFromGenerator import SourceFromGenerator
from SourceFromWeb import SourceFromWeb
from client import ClientGet as Client, ClientPost
from task import Task
from task_manager import task_manager
from task_queue import TaskQueue


def filter_by_status(task: Task):
    if task.status == 'ready':
        return True
    return False


def main() -> None:
    """
    Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """
    client1 = Client(
        "https://my.meteoblue.com/packages/basic-1h_basic-day?apikey=bOico7hWTVAzPQYM&lat=55.752&lon=37.6178&asl=155&format=json")
    client2 = Client("https://ru.wikipedia.org/wiki/Python")
    client3 = ClientPost("https://jsonplaceholder.typicode.com/posts",
                         message={"prompt": "{title: 'foo',body: 'bar',userId: 1}"})

    source_from_web1 = SourceFromWeb(client1)
    source_from_web2 = SourceFromWeb(client2)
    source_from_web3 = SourceFromWeb(client3)
    source_from_file = SourceFromFile("text")
    source_from_generators = SourceFromGenerator(1)

    print("Tasks from web queue:")

    tq = TaskQueue(source_from_web1)

    for el in list(tq):
        print(el)
    print('second time')
    for el in list(tq):
        print(el)
    for el in list(tq.filtration(filter_by_status)):
        print(el)

    sum_of_priority: int = sum(el.priority for el in tq)
    sum_of_priority1: int = sum(el.priority for el in tq)

    print(sum_of_priority,sum_of_priority1)

    print("Tasks from web:")

    for el in task_manager(source_from_web2):
        print(el)

    for el in task_manager(source_from_web3):
        print(el)

    print("\n", "Tasks from file:")

    for el in task_manager(source_from_file):
        print(el)

    print("\n", "Tasks from generators:")

    for el in task_manager(source_from_generators):
        print(el)


if __name__ == "__main__":
    main()
