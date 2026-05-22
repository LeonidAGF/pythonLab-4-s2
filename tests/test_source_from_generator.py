from src.SourceFromGenerator import SourceFromGenerator


def test_source_from_generator():
    """
        Тесты для SourceFromGenerator
    """
    sfg1: SourceFromGenerator = SourceFromGenerator(1)
    sfg3: SourceFromGenerator = SourceFromGenerator(2)
    sfg4: SourceFromGenerator = SourceFromGenerator(3)
    sfg5: SourceFromGenerator = SourceFromGenerator(4)
    sfg6: SourceFromGenerator = SourceFromGenerator(5)

    try:
        SourceFromGenerator(6)
        assert False
    except Exception:
        assert True

    assert len(list(sfg1.get_tasks())[0].payload.get('numbers',[])) != 0
    assert len(list(sfg3.get_tasks())[0].payload.get('numbers',[])) != 0
    assert len(list(sfg4.get_tasks())[0].payload.get('numbers',[])) != 0
    assert len(list(sfg5.get_tasks())[0].payload.get('numbers',[])) != 0
    assert len(list(sfg6.get_tasks())[0].payload.get('numbers',[])) != 0
