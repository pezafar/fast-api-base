from loguru import logger

from app.models.user import User


class ItemService:
    """Item processing service.
    Handles business logic for item operations.
    """

    def __init__(self):
        pass

    @staticmethod
    def process_item(data: str, user: User) -> str:
        logger.info(f"Processing item for user {user.name}")
        return f"Processed data: {data} for user {user.name}"

    @staticmethod
    def get_item(item_id: int, user: User) -> str:
        logger.info(f"Getting item {item_id} for user {user.name}")
        return f"Item {item_id} retrieved for user {user.name}"
