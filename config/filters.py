import logging
from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import Update

### MIDDLEWARES
# Middleware that filters if the user is allowed to use the bot
class FilterAllowedUsers(BaseMiddleware):
    def __init__(self) -> None:
        pass

    async def __call__(
        self,
        handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
        event: Update,
        data: Dict[str, Any]
    ) -> Any:
        if event.message.from_user.id not in [0]:
            logging.warning(f"User @{event.message.from_user.username} ({event.message.from_user.id}) isn't allowed to use the bot")
            return await handler(event, data)