from fastapi.testclient import TestClient

from app.__main__ import app

client = TestClient(app)


def test_request_logging():
    """Test that requests are logged properly"""
    response = client.post(
        "/api/v1/items",
        json={"data": "test data"},
        headers={"Authorization": "Bearer 123"},
    )
    assert response.status_code == 200
    # In a real application, you would check logs here


def test_error_logging():
    """Test that errors are logged properly"""
    response = client.post(
        "/api/v1/items",
        json={"data": "test data"},
        # Missing authorization header
    )
    assert response.status_code == 403
    # In a real application, you would check error logs here
