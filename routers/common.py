from aiogram import Router,types,F
from aiogram.types import Message
from aiogram.enums import ChatAction
import asyncio
from keyboards.Keyboards import Button_Text
from aiogram.types import ReplyKeyboardRemove
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
router=Router()



@router.message(F.text==Button_Text.BYE)
async def bye_bye(message:Message):
    await message.answer("Bye.Please press to command /start !!",reply_markup=ReplyKeyboardRemove())


@router.message(Command("cancel"))
@router.message(F.text.casefold()=="cancel")
async def cancel(message:Message,state:FSMContext):
    current_state=await state.get_state()
    if current_state is None:
        await message.reply(text="Ok, but nothing is going on!!")
        return
    
   
    await state.clear()
    await message.answer(text=f"Cancelled state {current_state}.")
    




@router.message()
async def echo(message:Message):
    
    await message.answer(text="Wait the couple seconds...",parse_mode=None)
    
    if message.sticker:
        await message.bot.send_chat_action(
            chat_id=message.chat.id,action=ChatAction.CHOOSE_STICKER
        )
    
    asyncio.sleep(2)
    
    await message.copy_to(message.chat.id)
