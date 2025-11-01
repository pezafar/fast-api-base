from fastapi.testclient import TestClient

from app.__main__ import app

client = TestClient(app)


def test_create_item():
    """Test creating an item"""
    response = client.post(
        "/api/v1/items",
        json={"data": "test data"},
        headers={"Authorization": "Bearer 123"},
    )
    assert response.status_code == 200
    data = response.json()
    assert "result" in data
    assert "test data" in data["result"]


def test_get_item():
    """Test getting an item"""
    response = client.get("/api/v1/items/1", headers={"Authorization": "Bearer 123"})
    assert response.status_code == 200
    data = response.json()
    assert "result" in data
    assert "Item 1" in data["result"]


def test_unauthorized_access():
    """Test unauthorized access"""
    response = client.post("/api/v1/items", json={"data": "test data"})
    assert response.status_code == 403
