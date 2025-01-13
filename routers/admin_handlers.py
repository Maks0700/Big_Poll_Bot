from aiogram import Router,F
from magic_filter import RegexpMode
from aiogram.types import Message

router=Router()


@router.message(F.text.regexp(r"(\d+)",mode=RegexpMode.SEARCH).as_("code"))
async def handle_code(messsage:Message,code):
    await messsage.reply(f"Your code: {code.group()}") 