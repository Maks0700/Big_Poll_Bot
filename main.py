import io
from aiogram import Bot,types,Dispatcher,F
import asyncio
import logging
from aiogram.utils import markdown
from aiogram.enums import ParseMode
from magic_filter import RegexpMode
from config import settings
from re import Match
from aiogram.filters import Command,CommandStart
from aiogram.types import Message
from re import Match
from aiogram.enums import ChatAction
import csv


from aiogram import F,Router
 
from routers import router as main_routers 



async def main():
    dp=Dispatcher()
    
    dp.include_router(main_routers)
    logging.basicConfig(level=logging.INFO)
    
    bot=Bot(token=settings.bot_token,parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())                                                   
    