from keyboards.keyboard_yes_or_no import builder_yes_no
from keyboards.keyboards_sport import build_select_keyboard
from routers.survey.States import KnownSports, Survey
from aiogram import F,Router
from aiogram.types import Message,ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.utils import markdown
from email_validator import validate_email

router=Router(name="email")

@router.message(Survey.email,F.text.cast(validate_email).normalized.as_("email"))
async def handle_survey_email(message:Message,state:FSMContext,email:str):
    await state.update_data(email=email)
    await message.answer(f"Good.Your valide email is {markdown.hbold(email)}. Which sport would you prefer?",reply_markup=build_select_keyboard(KnownSports))
    await state.set_state(Survey.sport)
     
@router.message(Survey.email)
async def handle_survey_invalid_email_message(message:Message):
    await message.answer(text="Invalid email,please try again!!Cancel survey? Tap to /cancel")
    