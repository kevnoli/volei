from fastapi import APIRouter
from .group import router as group_router
from .event import router as event_router
from .player import router as player_router

router = APIRouter()

router.include_router(group_router)
router.include_router(event_router)
router.include_router(player_router)
