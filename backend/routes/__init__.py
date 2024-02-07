from fastapi import APIRouter
from .group import router as group_router
from .event import router as event_router

router = APIRouter()

router.include_router(group_router)
router.include_router(event_router)
