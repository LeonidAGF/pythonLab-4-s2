import asyncio

from SourceFromFile import SourceFromFile
from SourceFromGenerator import SourceFromGenerator
from SourceFromWeb import SourceFromWeb
from async_task_runner import AsyncTaskRunner
from client import ClientGet as Client, ClientPost
from task_async_manager import TaskStringManager
from task_manager import task_manager
from task_queue import AsyncTaskQueue

async def main() -> None:

    client1 = Client("https://my.meteoblue.com/packages/basic-1h_basic-day?apikey=bOico7hWTVAzPQYM&lat=55.752&lon=37.6178&asl=155&format=json")
    client3 = ClientPost("https://jsonplaceholder.typicode.com/posts",message={"prompt": "{title: 'foo',body: 'bar',userId: 1}"})

    source_from_web1 = SourceFromWeb(client1)
    source_from_web3 = SourceFromWeb(client3)
    source_from_file = SourceFromFile("text")
    source_from_generators = SourceFromGenerator(1)

    print("Tasks from web:")

    tq = AsyncTaskQueue()
    async for el in source_from_web1.get_tasks():
        await tq.put(el)

    runnner:AsyncTaskRunner = AsyncTaskRunner(tq,TaskStringManager())
    await runnner.run(2)

    tq2 = AsyncTaskQueue()
    async for el in source_from_web3.get_tasks():
        await tq2.put(el)

    runnner2:AsyncTaskRunner = AsyncTaskRunner(tq2,TaskStringManager())
    await runnner2.run(2)

    print("\n", "Tasks from file:")

    tq3 = AsyncTaskQueue()
    async for el in source_from_file.get_tasks():
        await tq3.put(el)

    runnner3:AsyncTaskRunner = AsyncTaskRunner(tq3,TaskStringManager())
    await runnner3.run(1)

    print("\n", "Tasks from generators:")

    for el in await task_manager(source_from_generators):
        print(el)


if __name__ == "__main__":
    asyncio.run(main())
