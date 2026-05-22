from src.SourceFromFile import SourceFromFile


def test_source_from_file():
    """
        Тесты для SourceFromFile
    """
    sff1:SourceFromFile = SourceFromFile("./tests/test_cat_function.py")
    sff2:SourceFromFile = SourceFromFile("./tests/test_cat_function.py")
    sff3:SourceFromFile = SourceFromFile("./tests/test_cat_function.py")

    assert len(list(sff1.get_tasks()))!=0
    assert len(list(sff2.get_tasks()))!=0
    assert list(sff1.get_tasks())[0].id==list(sff2.get_tasks())[0].id
    assert len(list(sff3.get_tasks()))!=0
