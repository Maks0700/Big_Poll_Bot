from aiogram import BaseMiddleware, types
from datetime import timedelta
from typing import Callable, Any, Awaitable
from aiogram.types import TelegramObject
from datetime import datetime
from collections import defaultdict
from utils.async_time_que import AsyncTimeQue
import logging
from dataclasses import dataclass

logger: logging = logging.getLogger(__name__) 
print(logging.__path__)


@dataclass
class RateLimitInfo:
    message_count: int
    first_message: datetime | None


class RateLimit(BaseMiddleware):
    def __init__(self, rate_limit: int = 5, time_interval: timedelta = timedelta(seconds = 30)):
        self.rate_limit = rate_limit
        self.time_interval = time_interval
        self.last_messages_ts = defaultdict[int, AsyncTimeQue[datetime]](
            lambda: AsyncTimeQue(max_age = time_interval)
        )
        
    async def __call__(self, handler: Callable[[types.TelegramObject, dict[str, Any]], Awaitable[Any]],
                       event: types.Message,
                       data: dict[str, Any],) -> Any:
        
            user_id = event.from_user.id
            current_dt = datetime.now()
            
            last_messages = self.last_messages_ts[user_id]
            
            
            count: int = await last_messages.get_len()
            
            if count > self.rate_limit:
                logger.info("Skip user %s message", user_id)
                return
            
            await last_messages.put(current_dt)
            count = await last_messages.get_len()
            if count > self.rate_limit:
                logger.info("Skip another user %s message (new)", user_id)
                return
                
            if count == self.rate_limit:
                logger.info("Sending message to user %s before rate limit", user_id)
                
                await event.reply(
                    text = "You are sending too many messages."
                )
                return
            data.update(
                rate_limit_info = RateLimitInfo(
                    message_count = count,
                    first_message = await last_messages.peek()
                )
            )
            
            return await handler(event, data)
        