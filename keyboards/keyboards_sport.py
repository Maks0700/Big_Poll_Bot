from typing import Iterable
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def build_select_keyboard(options:Iterable[str])->ReplyKeyboardBuilder:
    builder=ReplyKeyboardBuilder()
    for option in options:
        builder.button(text=option)
    builder.adjust(1)
    return builder.as_markup(resize_keyboard=True)
   
    