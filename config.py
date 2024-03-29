from aiogram import Bot, Dispatcher
import asyncio
import os
from dotenv import load_dotenv
from aiogram.contrib.fsm_storage.memory import MemoryStorage
load_dotenv()


BOT_TOKEN = os.getenv('BOT_TOKEN')
USER = os.getenv('USER1')
PORT = os.getenv('PORT')
Host = os.getenv('Host')
DATABASE = os.getenv('DATABASE')
PASSWORD = os.getenv("PASSWORD1")
list_super_admins = os.getenv('list_super_admins')
DB_URI = os.getenv('DB_URI')


loop = asyncio.new_event_loop()
bot = Bot(BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, loop=loop, storage=MemoryStorage())



