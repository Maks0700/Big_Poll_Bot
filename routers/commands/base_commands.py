from aiogram import Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart,Command
from aiogram.utils import markdown
from keyboards.Keyboards import create_keyboard,Button_Text,code_command, get_actions_keyboard
from aiogram import F
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from keyboards.Keyboards import inline_keyboard_create

router=Router()
    



@router.message(CommandStart())
async def handle_start(message:types.Message):
    print(repr(message.text))
    
    url="https://w7.pngwing.com/pngs/547/380/png-transparent-robot-waving-hand-bot-ai-robot-thumbnail.png"
    await message.answer(
        text=f"{markdown.hide_link(url)}Hello, {markdown.hbold(message.from_user.full_name)}",
        parse_mode=ParseMode.HTML,reply_markup=create_keyboard()
    )
    

@router.message(F.text==Button_Text.WHATS_NEXT)
@router.message(Command("code", prefix="/!%"))
async def handle_command_code(message:types.Message):
    text=markdown.text("Here Python code")
    await message.answer(text=text,reply_markup=code_command())
    

@router.message(Command("more",prefix="!/"))
async def more_commands(message:types.Message):
    await message.answer(text="Choose action...",reply_markup=get_actions_keyboard())



@router.message(Command("info",prefix="!/"))
async def handle_info_command(message:types.Message):
    
    await message.answer("Other links",reply_markup=inline_keyboard_create())
    