from aiogram import Router,types,F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State

from keyboards.keyboard_yes_or_no import builder_yes_no
from .States import Survey,KnownSports,SportDetails,KnownF1Tracks
from aiogram.filters import StateFilter
from aiogram.types import ReplyKeyboardRemove

from keyboards.keyboards_sport import build_select_keyboard

router=Router(name=__name__)

knonws_sport_to_next_state:dict[KnownSports: str, tuple[SportDetails:State | str,str]]={
    KnownSports.football:(SportDetails.football,"What is your favourite football team?"),
    KnownSports.tennis:(SportDetails.tennis,"What is your favourite tennis player?"),
    KnownSports.formula_one:(SportDetails.formula_one,"What is your favourite F1 track, pointed below?")
}

formula_one_kb_res=build_select_keyboard(KnownF1Tracks)
formula_one_kb:dict={
    KnownSports.formula_one:formula_one_kb_res
}

@router.message(F.text.cast(KnownSports),Survey.sport)
async def select_sports(message:types.Message,state:FSMContext):
    next_state,question_next=knonws_sport_to_next_state[message.text]
    await state.update_data(sport=message.text,sport_question=question_next)# обновляем наш словарь с значением для вопроса следующего
    kb=ReplyKeyboardRemove()
    if message.text in formula_one_kb:
        kb=formula_one_kb[message.text]
    
    
    await state.set_state(next_state)
    await message.answer(text=question_next,reply_markup=kb)
    
    
@router.message(Survey.sport)
async def error_sports(message:types.Message):
    await message.reply(text="Enter the available sort of the sport, below pointed selection.",reply_markup=build_select_keyboard(KnownSports))
    


@router.message(F.text,StateFilter(SportDetails.football,SportDetails.tennis))#Здесь  мы работаем с состояниями для футбола и тенниса по отдельности   
@router.message(F.text.cast(KnownF1Tracks),SportDetails.formula_one)
async def handle_selected_sport_details_options(message:types.Message,state:FSMContext):
        await state.update_data(sport_details=message.text)
        await state.set_state(Survey.news_letter)
        await message.answer("Are you send me news_letter? This is last step before the end survey, but you can /cancel any time!!",reply_markup=builder_yes_no())
        

@router.message(SportDetails.tennis)
async def handle_tennis_player(message:types.Message):
    await message.reply(text="Please name tennis player using text!!")

@router.message(SportDetails.football)
async def handle_football_player(message:types.Message):
    await message.reply(text="Please name football team using text!!")
    

@router.message(SportDetails.formula_one)
async def handle_formula_one_not_one_of_text(message:types.Message):
    await message.reply(text="Please select one of known F1 tracks!!",reply_markup=formula_one_kb_res)
    
    
