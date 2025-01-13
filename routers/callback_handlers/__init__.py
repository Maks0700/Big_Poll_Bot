from aiogram import Router
from .info_kb_callback_handlers import router as info_callback_routers
from .shop_keyboard_callback import router as shop_callback_routers

router=Router(name=__name__)
router.include_routers(
    info_callback_routers,shop_callback_routers
    )