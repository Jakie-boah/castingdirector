from config import dp
from handlers.junk import numbers, admin_beg
from aiogram.types import Message, CallbackQuery
from handlers.InlineButtons import InlineButtons
from handlers.filter import SuperAdmin
from aiogram.dispatcher.filters import Command
from Database.Database import Database, TablesModerate

buttons = InlineButtons()
com = ''


@dp.message_handler(Command("adminka"), SuperAdmin())
async def f(message: Message):

    await message.answer(f'Выбери что изменить и нажми на соответсвующую кнопку - \n\n{admin_beg()}',
                         disable_web_page_preview=True, reply_markup=buttons.admin_options())


@dp.message_handler(Command(['1', '2', '3', '4', '5', '6']), SuperAdmin())
async def f(message: Message):
    global com

    com = message.text[1:]

    info = Database().get_chats()

    await message.answer(f'Какую инфо поменять в кнопке {info[int(com)-1][1]}?\n\n'
                         f'Текст или ссылку?', reply_markup=buttons.info_or_link())


@dp.callback_query_handler(text='text')
async def inline_kb_answer_callback_handler(query: CallbackQuery):
    answer_data = query.data

    if answer_data == 'text':
        await query.message.answer('Напиши новый текст и бот сам все сделает')
        text()


def text():
    @dp.message_handler(SuperAdmin())
    async def changed(message: Message):
        global com

        try:
            TablesModerate().change_text(com, message.text)

            await message.answer(text=f'Исправлено на:\n\n {message.text}', reply_markup=
            buttons.common())

        except:
            pass


@dp.callback_query_handler(text='link')
async def inline_kb_answer_callback_handler(query: CallbackQuery):
    answer_data = query.data

    if answer_data == 'link':

        await query.message.answer('Напиши новый ссылку и бот сам все сделает')

        link()


def link():
    @dp.message_handler(SuperAdmin())
    async def changed(message: Message):
        global com

        try:

            TablesModerate().change_link(com, message.text)

            await message.answer(text=f'Исправлено на:\n\n {message.text}', reply_markup=buttons.common())

        except:
            pass


@dp.callback_query_handler(text='delete')
async def inline_kb_answer_callback_handler(query: CallbackQuery):
    answer_data = query.data

    if answer_data == 'delete':

        await query.message.answer('Вы уверены?', reply_markup=buttons.sure())


@dp.callback_query_handler(text='yes')
async def inline_kb_answer_callback_handler(query: CallbackQuery):
    answer_data = query.data

    if answer_data == 'yes':
        print(com)
        TablesModerate().delete_button(com)
        await query.message.answer('Кнопка удалена', reply_markup=buttons.common())

