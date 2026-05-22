import json
from typing import Dict, Any, Protocol, runtime_checkable
from requests import Response
from src.task import Task
import requests

@runtime_checkable
class ClientBase(Protocol):
    """
        шаблон клиента
    """

    def get_task(self) -> Task | None:
        """
            функция необходимая для получения задач
        """
        pass


class ClientGet:
    """
        клиент дял получения задач задач из интернета с помощью метода гет
    """

    def __init__(self, path: str) -> None:
        """
            Инициализатор клиента задач из интернета
        """
        self.path = path

    def get_task(self) -> Task | None:
        """
            Функция получения задач из интернета
        """
        try:
            data: Dict[str, Any] = {}
            response: Response = requests.get(self.path)
            try:
                data["data"] = response.json().get('metadata').get('timezone_abbrevation')
            except Exception:
                data["data"] = response.text
            task: Task = Task(len(str(data["data"])),'description',data, (len(str(data["data"]))%2)+1)
            return task
        except Exception:
            return None


class ClientPost:
    """
        клиент дял получения задач задач из интернета с помощью метода гет
    """

    def __init__(self, path: str, message: Dict = None) -> None:
        """
            Инициализатор клиента задач из интернета
        """
        self.path = path
        self.message = message

    def get_task(self) -> Task | None:
        """
            Функция получения задач из интернета
        """
        try:
            data: Dict[str, Any] = {}
            response = requests.post(self.path, data=json.dumps(self.message))
            try:
                data["data"] = response.json().get('metadata').get('timezone_abbrevation')
            except Exception:
                data["data"] = response.text
            task: Task = Task( (len(str(data["data"]))),'description',data, ((len(str(data["data"]))%2)+1))
            return task
        except Exception:
            return None
