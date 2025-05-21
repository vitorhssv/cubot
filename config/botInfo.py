from dotenv import load_dotenv
from os import environ
from aiogram import Bot

load_dotenv(override=True)
bot = Bot(environ["BOT_TOKEN"])