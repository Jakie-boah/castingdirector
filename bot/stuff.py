from config import dp, bot
from aiogram.types import Message, CallbackQuery
from handlers.InlineButtons import InlineButtons
from handlers.filter import SuperAdmin
from aiogram.dispatcher.filters import Command
from Database.Database import Database


buttons = InlineButtons()


@dp.callback_query_handler(text='drugs')
async def inline_kb_answer_callback_handler(query: CallbackQuery):

    answer_data = query.data

    if answer_data == 'drugs':

        info = Database().get_chats()

        await query.message.edit_text(text=f'{info[0][5]}', disable_web_page_preview=True, reply_markup=buttons.common())











