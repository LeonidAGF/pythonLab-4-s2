import random

def rand_int_array(n: int, lo: int, hi: int, *, distinct=False, seed=None) -> list[int]:
    """
    Функция генерирующая массив случайных чисел
    :return: Возвращает массив случайных чисел
    """
    random.seed(None)
    if seed is not None:
        random.seed(seed)
    rand_array: list[int] = [0] * n
    for pos in range(0, n):
        rand_value: int = random.randint(lo, hi)
        if distinct and rand_value in rand_array:
            while rand_value in rand_array:
                rand_value = random.randint(lo, hi)
        rand_array[pos] = rand_value
    return rand_array


def nearly_sorted(n: int, swaps: int, *, seed=None) -> list[int]:
    """
    Функция генерирующая массив чисел от 1 до n и меняющая числа местами в нём случайно swaps раз
    :return: Массив чисел
    """
    random.seed(None)
    array: list[int] = [int(i) for i in range(1, n + 1)]
    if seed is not None:
        random.seed(seed)
    for i in range(swaps):
        first_pos_for_swap: int = random.randint(0, n - 1)
        second_pos_for_swap: int = random.randint(0, n - 1)
        while first_pos_for_swap == second_pos_for_swap:
            first_pos_for_swap = random.randint(0, n - 1)
            second_pos_for_swap = random.randint(0, n - 1)
        array[first_pos_for_swap], array[second_pos_for_swap] = array[second_pos_for_swap], array[first_pos_for_swap]
    return array


def many_duplicates(n: int, k_unique=5, *, seed=None) -> list[int]:
    """
    Функция генерирующая массив с k_unique количеством уникальных элементов
    :return: Массив чисел
    """
    random.seed(None)
    if seed is not None:
        random.seed(seed)

    not_unique_el: int = random.randint(1, n + 1)
    array: list[int] = [not_unique_el] * (n - k_unique)
    for i in range(k_unique):
        rand_value: int = random.randint(1, n + 1)
        if rand_value in array:
            while rand_value in array:
                rand_value = random.randint(1, n + 1)
        array += [rand_value]

    for i in range(n):
        first_pos_for_swap: int = random.randint(0, n - 1)
        second_pos_for_swap: int = random.randint(0, n - 1)
        while first_pos_for_swap == second_pos_for_swap:
            first_pos_for_swap = random.randint(0, n - 1)
            second_pos_for_swap = random.randint(0, n - 1)
        array[first_pos_for_swap], array[second_pos_for_swap] = array[second_pos_for_swap], array[first_pos_for_swap]

    return array


def reverse_sorted(n: int) -> list[int]:
    """
    Функция возвращающая массив с числами отсортированными в обратном порядке
    :return: Массив с числами
    """

    rand_array: list[int] = [int(i) for i in range(1, n + 1)]
    rand_array.sort(reverse=True)
    return rand_array


def rand_float_array(n: int, lo=0.0, hi=1.0, *, seed=None) -> list[float]:
    """
    Функция генерирующая массив случайных нецелвх чисел
    :return: Массив с нецелыми числами
    """
    random.seed(None)
    if seed is not None:
        random.seed(seed)
    rand_array: list[float] = [0] * n
    for pos in range(0, n):
        rand_value: float = random.uniform(lo, hi)
        rand_array[pos] = rand_value
    return rand_array
