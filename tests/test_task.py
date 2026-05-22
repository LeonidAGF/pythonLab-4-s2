from src.task import Task


def test_task():
    """
        Тесты для task
    """

    t = Task(1, "dgfgjhbknjlm", {},1)
    try:
        t.status = 'ready1'
        assert 1 == 0
    except Exception:
        assert 1 == 1

    t.status = 'ready'
    assert t.status == 'ready'

    try:
        t.payload = 'ready1'
        assert 1 == 0
    except Exception:
        assert 1 == 1

    try:
        t.payload = {'something':'else'}
        assert 1 == 1
    except Exception:
        assert 1 == 0

    try:
        t.id = 'ready1'
        assert 1 == 0
    except Exception:
        assert 1 == 1

    try:
        t.id = 2
        assert 1 == 1
    except Exception:
        assert 1 == 0

    try:
        t.description = 'ready1'
        assert 1 == 1
    except Exception:
        assert 1 == 0
    assert isinstance(t.is_ready,bool)== True
