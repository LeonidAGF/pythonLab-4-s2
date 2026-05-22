from src.errors import ValidationError


class IdAttribute:
    """
        дескриптор для поля id
    """

    def __set_name__(self, owner, name) -> None:
        """
            функция для того чтобы задать имя будущему атрибуту
        """
        self.name = '_' + name

    def __get__(self, instance, owner) -> int:
        """
            функция для получения атрибута
        """
        return getattr(instance, self.name, None)

    def __set__(self, instance, value: int) -> None:
        """
            функция для того чтобы задать значение атрибуту id
        """
        if isinstance(value, int):
            setattr(instance, self.name, value)
        else:
            raise ValidationError


class PriorityAttribute:
    """
        дескриптор для поля Priority
    """

    def __set_name__(self, owner, name) -> None:
        """
            функция для того чтобы задать имя будущему атрибуту
        """
        self.name = '_' + name

    def __get__(self, instance, owner) -> int:
        """
            функция для получения атрибута
        """
        return getattr(instance, self.name, None)

    def __set__(self, instance, value: int) -> None:
        """
            функция для того чтобы задать значение атрибуту Priority
        """
        if isinstance(value, int) and (value == 1 or value == 2):
            setattr(instance, self.name, value)
        else:
            raise ValidationError


class StatusAttribute:
    """
        дескриптор для поля Status
    """

    def __set_name__(self, owner, name) -> None:
        """
            функция для того чтобы задать имя будущему атрибуту
        """
        self.name = '_' + name

    def __get__(self, instance, owner) -> str:
        """
            функция для получения атрибута
        """
        return getattr(instance, self.name, None)

    def __set__(self, instance, value: str) -> None:
        """
            функция для того чтобы задать значение атрибуту Status
        """
        if isinstance(value, str) and (value == 'ready' or value == 'in processing'):
            setattr(instance, self.name, value)
        else:
            raise ValidationError
