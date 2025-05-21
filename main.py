import asyncio, logging, sys
from config.botInfo import bot
from aiogram import Dispatcher

# Starting the bot
async def main() -> None:
    dp = Dispatcher()
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())