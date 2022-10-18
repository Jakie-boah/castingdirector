from config import dp
from aiogram.dispatcher.filters import Command
from handlers.InlineButtons import InlineButtons
from Database.Database import Database
from aiogram.types import Message, CallbackQuery

buttons = InlineButtons()


@dp.message_handler(Command(['start', 'help'], prefixes='!/'))
async def start(message: Message):

    info = Database().get_chats()

    await message.answer(f'{info[0][0]}', reply_markup=buttons.introduce())

    await message.delete()


@dp.callback_query_handler(text='start')
async def inline_kb_answer_callback_handler(query: CallbackQuery):

    answer_data = query.data

    if answer_data == 'start':

        info = Database().get_chats()

        await query.message.edit_text(f'{info[0][0]}', reply_markup=buttons.introduce())








