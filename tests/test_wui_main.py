import pytest

from volosti_server_sanic.app import app


@pytest.mark.asyncio
async def test_main_page() -> None:
    request, response = await app.asgi_client.get("/")

    assert request.method.lower() == "get"
    assert response.status == 200
    assert response.text == 'volosti-server-sanic'
