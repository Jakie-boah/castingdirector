from aiogram import Bot, Dispatcher
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()


BOT_TOKEN = os.getenv('BOT_TOKEN')
USER = os.getenv('USER')
PORT = os.getenv('PORT')
Host = os.getenv('Host')
DATABASE = os.getenv('DATABASE')
PASSWORD = os.getenv("PASSWORD")
list_super_admins = os.getenv('list_super_admins')


loop = asyncio.new_event_loop()
bot = Bot(BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, loop=loop)



