from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton

def builder_yes_no()->ReplyKeyboardBuilder:
    builder=ReplyKeyboardBuilder()
    builder.button(text="Yes")
    builder.button(text="No")
    
    return builder.as_markup(resize_keyboard=True)
