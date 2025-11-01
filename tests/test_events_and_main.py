from fastapi import FastAPI

from app.__main__ import get_application
from app.core import events


def test_get_application():
    """Test that the application is created correctly"""
    app = get_application()
    assert isinstance(app, FastAPI)
    assert app.title == "FastAPI Template"


def test_create_start_app_handler():
    """Test the startup handler creation"""
    app = FastAPI()
    handler = events.create_start_app_handler(app)
    assert callable(handler)
