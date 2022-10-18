from config import dp, bot
from aiogram.types import Message, CallbackQuery
from handlers.InlineButtons import InlineButtons
from handlers.filter import SuperAdmin
from aiogram.dispatcher.filters import Command
from Database.Database import Database

import bot.welcome
import bot.reviews
import bot.admin
import bot.stuff

buttons = InlineButtons()


@dp.callback_query_handler(text='menu')
async def inline_kb_answer_callback_handler(query: CallbackQuery):

    answer_data = query.data

    if answer_data == 'menu':

        info = Database().get_chats()

        await query.message.edit_text(text=f'{info[0][1]}', disable_web_page_preview=True, reply_markup=buttons.common())

