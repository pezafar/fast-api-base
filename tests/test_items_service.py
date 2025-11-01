from app.models.user import User
from app.services.items import ItemService


def test_process_item():
    """Test item processing"""
    user = User(id=1, name="Test User")
    result = ItemService.process_item("test data", user)

    assert "test data" in result
    assert "Test User" in result


def test_get_item():
    """Test getting item"""
    user = User(id=1, name="Test User")
    result = ItemService.get_item(123, user)

    assert "Item 123" in result
    assert "Test User" in result
