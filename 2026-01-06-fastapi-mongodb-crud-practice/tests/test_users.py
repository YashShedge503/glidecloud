import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_create_user():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post(
            "/users/",
            json={
                "name": "Test User",
                "email": "test@example.com",
                "age": 25
            }
        )

    assert response.status_code == 200
    assert response.json()["email"] == "test@example.com"
