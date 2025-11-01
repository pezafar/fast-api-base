from loguru import logger
from app.models.completion import User


class MockService:
    """GPT API completion call service.
    Calls the gpt api to get completions for a given prompt.
    """

    def __init__(self):
        pass

    @staticmethod
    def hello(text_input: str, user: User) -> str:
        logger.info("Hello")

        return f"Hello, {user.name}. You said: {text_input} and got answer."
