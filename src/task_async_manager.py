from typing import Protocol, runtime_checkable
from src.task import Task


@runtime_checkable
class TaskAsyncManager(Protocol):
    """
        шаблон async менеджера задач
    """

    async def do(self, task: Task) -> Task | None:
        """
            функция необходимая для обработки задач
        """
        pass


class TaskStringManager:
    """
        менеджера задач работающий с text задачи
    """

    async def do(self, task: Task) -> Task | None:
        """
            функция необходимая для обработки задач
            находит количество слов task которое можно составить из букв из payload
        """
        task.status = "ready"
        if task.is_ready:
            res = 0
            s = str(task.payload)
            for i in range(0, len(s)):
                for j in range(0, len(s)):
                    for k in range(0, len(s)):
                        for l in range(0, len(s)):
                            if i != j and i != k and i != l and j != k and j != l and l != k:
                                ns = s[i] + s[j] + s[k] + s[l]
                                if ns == 'task':
                                    res += 1

            task.payload = {'col_of_word_task_in_payload': res, 'last_content': task.payload}
            return task
        return None
