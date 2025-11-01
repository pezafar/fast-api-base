from app.core.security import get_current_user
from app.models.completion import DataInputModel, DataOutputModel
from app.services.completion import MockService
from fastapi import APIRouter
from fastapi import Depends


# Dummy "database" of tokens
VALID_TOKENS = {
    "user1_token_123": {"user_id": 1, "name": "Alice"},
    "user2_token_456": {"user_id": 2, "name": "Bob"},
}


router = APIRouter()


@router.post(
    "/completion",
    response_model=DataOutputModel,
    name="predict:get-data",
)
async def complete(data_input: DataInputModel, user=Depends(get_current_user)):

    text_response = MockService.hello(data_input.prompt, user=user)
    response = DataOutputModel(response=text_response)
    return response
