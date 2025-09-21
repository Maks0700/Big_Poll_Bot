from aiogram import Router,F
from magic_filter import RegexpMode
from aiogram.types import Message
from middlewares.rate_limit import RateLimitInfo
from aiogram.utils.markdown import text
from re import Match
router=Router()


@router.message(F.text.regexp(r"(\d+)", mode=RegexpMode.SEARCH).as_("code"))
async def handle_code(messsage: Message, code: Match[str], rate_limit_info: RateLimitInfo):
    count = rate_limit_info.message_count
    first_message = rate_limit_info.first_message
    text_send = text(
        f"Your code: {code.group()}\n",
        f"RL message count: {count}",
        f"RL first message: {first_message}",
        sep = "\n",)
        
    await messsage.reply(text = text_send) 