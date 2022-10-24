from config import dp, bot
from aiogram.dispatcher.filters import Command
from handlers.InlineButtons import InlineButtons
from aiogram.types import Message, CallbackQuery

buttons = InlineButtons()


@dp.message_handler(Command(['start', 'help'], prefixes='!/'))
async def start(message: Message):

    await message.answer(f'Навигация', reply_markup=buttons.introduce())

    await message.delete()


@dp.callback_query_handler(text='start')
async def inline_kb_answer_callback_handler(query: CallbackQuery):

    answer_data = query.data

    if answer_data == 'start':

        await query.message.edit_text(f'Навигация', reply_markup=buttons.introduce())


@dp.message_handler(commands=['start_bot'])
async def start():
    await bot.send_message(-1001707361135, 'Навигация', reply_markup=buttons.introduce())


