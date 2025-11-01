from fastapi import APIRouter

from app.api.routes import items

router = APIRouter()
router.include_router(items.router, tags=["items"], prefix="/v1")
