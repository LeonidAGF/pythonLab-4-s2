
from typing import Dict, Iterator
from src.task import Task
from src.generator import rand_int_array, nearly_sorted, many_duplicates, reverse_sorted, rand_float_array


class SourceFromGenerator:
    """
        Источник задач из генераоров массивов
    """

    def __init__(self, type: int) -> None:
        """
            Инициализатор источника задач из файлов
        """
        if type < 1 or type > 5:
            raise Exception
        self.type = type

    def get_tasks(self) -> Iterator[Task | None]:
        """
            Функция получения задач из генераторов
        """

        for col in range(0, 10):

            data: Dict[str, list] = {}
            match self.type:
                case 1:
                    data["numbers"] = rand_int_array(10, 1, 50)
                case 2:
                    data["numbers"] = nearly_sorted(20, 5)
                case 3:
                    data["numbers"] = many_duplicates(5)
                case 4:
                    data["numbers"] = reverse_sorted(10)
                case 5:
                    data["numbers"] = rand_float_array(20)

            el: Task = Task(col+45612, 'description', data, (col%2)+1)
            yield el
