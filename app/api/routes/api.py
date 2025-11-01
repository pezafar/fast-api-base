from fastapi import APIRouter

from app.api.routes import completion

router = APIRouter()
router.include_router(completion.router, tags=["predictor"], prefix="/v1")
