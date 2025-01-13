from keyboards.keyboard_yes_or_no import builder_yes_no
from routers.survey.States import Survey
from aiogram import F,Router
from aiogram.types import Message,ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.utils import markdown

router=Router(name=__name__)


async def send_survey_result(message:Message,data: dict):
    text=markdown.text("Your survey is results:",
                       "",
                       markdown.text("Name: ",markdown.hbold(data["name"])),
                       markdown.text("Email: ",markdown.hbold(data["email"])),
                       "",
                       markdown.text("Preferred sport: ",markdown.hbold(data["sport"])),
                       markdown.text("Q: ",markdown.hitalic(data["sport_question"])),
                       markdown.text("A: ",markdown.hitalic(data["sport_details"])),
                       (
                           "Cool, we are send you our news!!"
                           if data["news_letter"]
                           else "And won't bother you again!!"
                       ),
                       sep="\n")
    await message.answer(text=text,reply_markup=ReplyKeyboardRemove())



@router.message(Survey.news_letter,F.text.casefold()=="yes")
async def handle_survey_email(message:Message,state:FSMContext):
    data=await state.update_data(news_letter=True)
    await state.clear()
    await send_survey_result(message,data)

@router.message(Survey.news_letter,F.text.casefold()=="no")
async def handle_survey_email(message:Message,state:FSMContext):
    
    data=await state.update_data(news_letter=False)
    await state.clear()
    await send_survey_result(message,data)  


@router.message(Survey.news_letter)
async def handle_survey_newsletter_could_not(message:Message,state:FSMContext):
    await message.reply("Use the keyboard to answer,yes or no!!!",reply_markup=builder_yes_no())