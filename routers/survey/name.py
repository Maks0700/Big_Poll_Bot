from keyboards.keyboard_yes_or_no import builder_yes_no
from routers.survey.States import Survey
from aiogram import F,Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.utils import markdown
from aiogram.enums import ParseMode

router = Router()


@router.message(Survey.name, F.text)
async def enter_name(message: Message, state: FSMContext):
    await message.answer(f"Hello, {markdown.hbold(message.text)}.Please to share your email!",parse_mode=ParseMode.HTML)
    await state.update_data(name=message.text)
    await state.set_state(Survey.email)
    
    

@router.message(Survey.name)
async def invalid_name(message: Message):
    await message.reply("Try again enter name!!")