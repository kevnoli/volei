from fastapi import APIRouter
from .event import router as event_router
from .player import router as player_router
from .settings import router as settings_router

router = APIRouter()

router.include_router(event_router)
router.include_router(player_router)
router.include_router(settings_router)
