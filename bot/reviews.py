from config import dp, bot
from aiogram.types import Message, CallbackQuery
from handlers.InlineButtons import InlineButtons
from handlers.filter import SuperAdmin
from aiogram.dispatcher.filters import Command
from Database.Database import Database

buttons = InlineButtons()


@dp.callback_query_handler(text='reviews')
async def inline_kb_answer_callback_handler(query: CallbackQuery):

    answer_data = query.data

    if answer_data == 'reviews':

        info = Database().get_chats()

        await query.message.edit_text(text=f'{info[0][2]}', disable_web_page_preview=True, reply_markup=buttons.reviews_buttons())


@dp.callback_query_handler(text='video_review')
async def inline_kb_answer_callback_handler(query: CallbackQuery):

    answer_data = query.data

    if answer_data == 'video_review':

        info = Database().get_chats()

        await query.message.edit_text(text=f'{info[0][3]}', disable_web_page_preview=True, reply_markup=buttons.common())


@dp.callback_query_handler(text='hand_review')
async def inline_kb_answer_callback_handler(query: CallbackQuery):

    answer_data = query.data

    if answer_data == 'hand_review':

        info = Database().get_chats()

        await query.message.edit_text(text=f'{info[0][4]}', disable_web_page_preview=True, reply_markup=buttons.common())









