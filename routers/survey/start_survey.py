from aiogram import Router
from aiogram.filters import Command,StateFilter
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from .States import Survey, SportDetails
from aiogram import F
from aiogram.utils import markdown
from aiogram.enums import ParseMode
from keyboards.keyboard_yes_or_no import builder_yes_no
from aiogram.types import ReplyKeyboardRemove
from email_validator import validate_email
from .new_letters import (router as new_letters_router)
from .email_handlers import (router as email_router)
from .name import (router as name_router)
from aiogram.fsm.state import any_state, default_state
from .sport_handlers import router  as sport_router




router= Router()
router.include_router(email_router)
router.include_router(new_letters_router)
router.include_router(name_router)
router.include_router(sport_router)


@router.message(Command("survey",prefix="!/"),default_state)#Default state нужен чтобы ѝо ѝтарта бота у наѝ было ѝоѝтоѝние одно неѝмотрѝ что мы не уѝтанавливали пока ѝоѝтоѝние
async def start_survey(message:Message,state:FSMContext):
    await message.answer(f"Hello {message.from_user.full_name}. What is your name?")
    await state.set_state(Survey.name)
    
@router.message(Command("cancel"),StateFilter(Survey(),SportDetails()))#Здеѝь мы передаем два ѝоѝтоѝниѝ потому что у наѝ два клаѝѝа Survey и SportDetails  
@router.message(F.text.casefold()=="cancel",StateFilter(Survey(),SportDetails()))
async def cancel(message:Message,state:FSMContext):
    current_state=await state.get_state()
    
    if current_state is None:
        await message.reply(text="Your states is None!! The start survey: /survey",reply_markup=ReplyKeyboardRemove())
        return
    
    await state.clear()
    await message.answer(text=f"Cancelled state {current_state}. Try again to survey is /survey")
    

    
    



    


