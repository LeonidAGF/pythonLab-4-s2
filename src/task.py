from datetime import datetime
from typing import Any
from src.descriptors import IdAttribute, PriorityAttribute, StatusAttribute
from src.errors import ValidationError


class Task:
    """
        класс задачи
    """

    id:int = IdAttribute()
    priority:int = PriorityAttribute()
    status:str = StatusAttribute()

    def __init__(self, id:int, description:str,payload:dict[str, Any], priority:int):
        """
            функция для инициализации атрибутов
        """
        if not isinstance(id, int):
            raise ValidationError
        if not isinstance(description, str):
            raise ValidationError
        if not isinstance(payload, dict):
            raise ValidationError
        if not isinstance(priority, int) or (priority!= 1 and priority !=2):
            raise ValidationError

        self.id = id
        self.description = description
        self.payload = payload
        self.priority = priority
        self.status = 'in processing'
        self.create_time = str(datetime.now())

    @property
    def description(self) -> str:
        """
            функция для получения описания задачи
        """
        return self._description

    @description.setter
    def description(self, value) -> None:
        """
            функуия для установки описания задачи
        """
        if isinstance(value, str):
            self._description = value
        else:
            raise ValidationError

    @property
    def payload(self) -> dict:
        """
            функция для получения payload
        """
        return self._payload

    @payload.setter
    def payload(self, value) -> None:
        """
            функция для утановки payload
        """
        if isinstance(value, dict):
            self._payload = value
        else:
            raise ValidationError

    @property
    def is_ready(self) -> bool:
        """
            функция для получения is_ready
        """
        return self.status=='ready'

    def __repr__(self):
        """
            функция для преобразования объекта в строку
        """
        return "id = " + str(self.id) + ", description = " + self.description + ", payload = " + str(self.payload) + ", priority = " + str(self.priority) + ", status = " + self.status