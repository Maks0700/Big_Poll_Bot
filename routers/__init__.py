from aiogram import Router
from .commands import router as router_commands
from .common import router as router_common
from .media_handlers import router as router_media_handlers
from .admin_handlers import router as router_admin_handlers
from .callback_handlers import router as router_callbacks
from .survey import router as survey_router

router=Router()


router.include_routers(router_callbacks,
                       router_commands,
                       survey_router,
                       router_media_handlers,
                       router_admin_handlers)

router.include_router(router_common)
