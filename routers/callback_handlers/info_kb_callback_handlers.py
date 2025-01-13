from aiogram import Router,F
from aiogram.types import Message,CallbackQuery
from keyboards.Keyboards import action_keyboard
from random import randint
from aiogram.filters import Command 
from keyboards.Keyboards import (FixedRandomNumCbData,RandomNumaction,RandomNumCbData)

router=Router()
user_data={}


@router.callback_query(F.data=="text")

async def process_callback_test(callback:CallbackQuery):
    bot_me=await callback.bot.get_me()
    await callback.answer(url="t.me/{}?start={}".format(bot_me.username,randint(1,100)),
                        text=callback.data)
    

@router.callback_query(RandomNumCbData.filter(F.action==RandomNumaction.dice))
async def handle_random_num_dice(callback_query:CallbackQuery):
    await callback_query.answer(text=f"Your random dice {randint(1,1000)}",cache_time=10)
    

@router.callback_query(RandomNumCbData.filter(F.action==RandomNumaction.modal))
async def  handle_random_model_number(callback_query:CallbackQuery):
    await callback_query.answer(text=f"Your random dice {randint(1,1000)}",show_alert=True)

@router.callback_query(F.data=="random_edited_text")
async def handle_random_edited_text(callback_query:CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text(text=f"Random number {randint(1,100)}",reply_markup=action_keyboard("Generate text"))





@router.callback_query(FixedRandomNumCbData.filter(F.number==18))
async def handle_fixed_random_num(callback_query:CallbackQuery,callback_data:FixedRandomNumCbData):
    await callback_query.message.answer("Good jackpot")


