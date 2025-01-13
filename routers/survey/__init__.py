from aiogram import Router
from .start_survey import router as handlers_router




router=Router(name="survey")
router.include_router(handlers_router)


