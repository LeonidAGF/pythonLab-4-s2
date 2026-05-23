from src.task import Task
from src.task_queue import AsyncTaskQueue
from src.task_async_manager import TaskAsyncManager

class AsyncTaskRunner:
    """
    шаблон async runnerа задач
    """

    def __init__(self, queue: AsyncTaskQueue, manager: TaskAsyncManager) -> None:

        self.queue = queue
        if isinstance(manager, TaskAsyncManager):
            self.manager = manager
        else:
            raise TypeError

    async def run(self, col: int) -> None:
        """
        функция необходимая для обработки задач
        """
        col_of_itr = 0
        while col_of_itr < col:
            task: Task = await self.queue.get()
            try:
                res: Task = await self.manager.do(task)
                if res:
                    print(res)
                else:
                    raise ValueError
                col_of_itr += 1

            except Exception as e:
                print(e, "error")
                break
