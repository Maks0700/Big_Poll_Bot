from aiogram import Router,types,F
from aiogram.types import Message
from aiogram.enums import ChatAction
import asyncio
from magic_filter import RegexpMode



router=Router()


@router.message(F.photo,F.caption)
async def handle_message_photo(message:Message):
    await message.reply("I can't see, sorry. Could you describe it please?")
    

       

@router.message(F.photo,~F.caption)
async def send_photo(message:Message):
    capt="I can't see, sorry."
    await message.bot.send_chat_action(message.chat.id,ChatAction.UPLOAD_PHOTO)
    await message.reply_photo(message.photo[-1].file_id,
                              caption=capt)
    


    