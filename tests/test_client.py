import pytest

from src.client import ClientGet as Client, ClientPost, ClientBase


@pytest.mark.asyncio
async def test_client():
    """
    Тесты для AsyncTaskRunner
    """
    try:
        _client1 = Client(
            "https://my.meteoblue.com/packages/basic-1h_basic-day?apikey=bOico7hWTVAzPQYM&lat=55.752&lon=37.6178&asl=155&format=json"
        )
        _client3 = ClientPost(
            "https://jsonplaceholder.typicode.com/posts",
            message={"prompt": "{title: 'foo',body: 'bar',userId: 1}"},
        )

        await _client1.get_task()
        await _client3.get_task()

        try:
            _client4 = ClientBase()
            await _client4.get_task()
            assert False
        except Exception:
            assert True
        assert True
    except Exception:
        assert False
