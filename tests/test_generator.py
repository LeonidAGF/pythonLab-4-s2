from src.generator import rand_int_array, nearly_sorted, many_duplicates, reverse_sorted, rand_float_array

def test_case_generators():
    """
        Тесты для reverse_sorted,many_duplicates,nearly_sorted,rand_int_array,rand_float_array
    """

    test_arr1: list[int] = rand_int_array(5, 0, 10, distinct=True)
    test_arr2: list[int] = rand_int_array(5, 0, 10)
    test_arr3: list[int] = rand_int_array(5, 0, 10, seed=66)
    test_arr4: list[int] = rand_int_array(5, 0, 10, seed=66)
    col_not_dublecats = 0
    for element in test_arr1:
        if test_arr1.count(element) == 1:
            col_not_dublecats += 1

    test_arr5: list[int] = nearly_sorted(5, 2, seed=42)
    test_arr6: list[int] = nearly_sorted(5, 2, seed=42)

    test_arr8: list[int] = many_duplicates(6, 2)
    test_arr9: list[int] = many_duplicates(6, 2, seed=88)
    test_arr10: list[int] = many_duplicates(6, 2, seed=88)
    col_dublecats = 0
    for element in test_arr8:
        if test_arr8.count(element) > 1:
            col_dublecats += 1

    test_arr11: list[int] = reverse_sorted(6)
    res_arr: list[int] = [int(i) for i in range(1, 7)]
    res_arr.sort(reverse=True)

    test_arr12: list[float] = rand_float_array(5, 0.0, 10)
    test_arr13: list[float] = rand_float_array(5, 0.0, 10, seed=77)
    test_arr14: list[float] = rand_float_array(5, 0.0, 10, seed=77)

    assert test_arr13 == test_arr14
    assert test_arr10 == test_arr9
    assert test_arr6 == test_arr5
    assert test_arr3 == test_arr4
    assert test_arr3 == test_arr4
    assert res_arr == test_arr11
    assert min(test_arr12) >= 0.0
    assert max(test_arr12) <= 10
    assert type(test_arr12[0]) is float
    assert col_dublecats == 4
    assert col_not_dublecats == 5
    assert min(test_arr1) >= 0
    assert max(test_arr1) <= 10
    assert type(test_arr1[0]) is int
    assert min(test_arr2) >= 0
    assert max(test_arr2) <= 10
    assert type(test_arr2[0]) is int
