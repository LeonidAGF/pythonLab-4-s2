import os

from src.cat_function import cat

def test_cat_function():
    """
        Тесты для  cat
    """
    assert cat('./tests/test_cat_function.py') != 'error'
    assert cat('requirements.txt') != 'error'
    assert cat(os.path.abspath('requirements.txt')) != 'error'
    assert cat(os.path.abspath('./tests/test_cat_function.py')) != 'error'
