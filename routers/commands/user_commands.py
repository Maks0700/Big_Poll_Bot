from aiogram import Router,types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart,Command
from aiogram.utils import markdown
import csv
import io
from aiogram.utils.chat_action import ChatActionSender
from aiogram.enums import ChatAction
import asyncio
import  aiohttp
from aiogram.types import Message
from keyboards.Keyboards import action_keyboard, create_request,build_actions_kb
from keyboards.keyboard_shop import create_builder_shop


router=Router()

@router.message(Command("pic"))
async def handle_com_pic(message:types.Message):
    file_path="test.png"
    await message.bot.send_chat_action(
        chat_id=message.chat.id,action=ChatAction.UPLOAD_DOCUMENT
    )
    await message.reply_document(document=types.FSInputFile(file_path),caption="Thiis is a test")





@router.message(Command("csv"))
async def send_csv_file(message:types.Message):
    file=io.StringIO()
    writer=csv.writer(file)
    writer.writerows([
        ["Name","Age","City"],
        ["John","28","New York"],
        ["Maks","45","Moscow"]
    ])
    await message.reply_document(
        document=types.BufferedInputFile(
            file.getvalue().encode("utf-8"),#getValue() for amount bytes
            filename="test.csv",
        )
    )
    


async def big_file(message:Message):
    file=io.BytesIO()
    await asyncio.sleep(4)
    url="https://avatars.mds.yandex.net/i?id=f64710d1da958f2fc884be6cb109e1faa58442e8ddd00328-5268818-images-thumbs&n=13"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            result_bytes=await response.read()
    
    file.write(result_bytes)
    await message.reply_document(
        document=types.BufferedInputFile(
            file=file.getvalue(),
            filename="cat.jpeg"
        )
    )


    

@router.message(Command("pic_file"))
async def send_pic_file_buffered(message:Message):
    await message.bot.send_chat_action(message.chat.id,action=ChatAction.UPLOAD_DOCUMENT)
    
    async with ChatActionSender.upload_document(bot=message.bot,chat_id=message.chat.id):
        await big_file(message)
        
        

@router.message(Command("action",prefix="!/"))
async def send_actions_message_w_kb(message:Message):
    await message.answer(text="Your actions",reply_markup=action_keyboard())



@router.message(Command("actions",prefix="!/"))
async def send_actions(message:Message):
    await message.answer(text="Your actions",reply_markup=build_actions_kb())

        
@router.message(Command("req",prefix="!/"))
async def send_req(message:Message):
    await message.answer(text="Test requests!!",reply_markup=create_request())


@router.message(Command("shop",prefix="!/"))
async def send_shop(message:Message):
    await message.answer("Your shop action:",reply_markup=create_builder_shop())
    
