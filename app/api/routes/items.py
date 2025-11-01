from fastapi import APIRouter, Depends

from app.core.security import get_current_user
from app.models.items import ItemInput, ItemOutput
from app.services.items import ItemService

router = APIRouter()


@router.post(
    "/items",
    response_model=ItemOutput,
    name="items:create-item",
)
async def create_item(item_input: ItemInput, user=Depends(get_current_user)):
    """Create a new item"""
    response = ItemService.process_item(item_input.data, user=user)
    return ItemOutput(result=response)


@router.get(
    "/items/{item_id}",
    response_model=ItemOutput,
    name="items:get-item",
)
async def get_item(item_id: int, user=Depends(get_current_user)):
    """Get an item by ID"""
    response = ItemService.get_item(item_id, user=user)
    return ItemOutput(result=response)
