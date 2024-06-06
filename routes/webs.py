from fastapi import APIRouter
from controllers import home_controller

router = APIRouter()

router.include_router(home_controller.router)
