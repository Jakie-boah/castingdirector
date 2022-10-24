from config import dp
from aiogram.types import Message, CallbackQuery
from handlers.InlineButtons import InlineButtons
from handlers.filter import SuperAdmin
from aiogram.dispatcher.filters import Command
from Database.Database import TablesModerate
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

buttons = InlineButtons()


class Form(StatesGroup):
    name = State()
    url = State()


@dp.message_handler(Command(['Добавить']), SuperAdmin())
async def f(message: Message):

    await Form.name.set()

    await message.answer(f'Что должно быть написано на кнопке?')


@dp.message_handler(state=Form.name)
async def process_name(message: Message, state: FSMContext):

    async with state.proxy() as data:
        data['name'] = message.text
    await Form.next()
    await message.answer('С названием решили, если ошиблись - не беда, чуть позже можно будет поправить. \n'
                         'Напиши теперь какая должна быть вшита ссылка в кнопку'
                         )


@dp.message_handler(state=Form.url)
async def process_name(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['url'] = message.text

    await message.answer('Это все. Нажми на кнопку ниже и кнопка добавится ', reply_markup=buttons.done())


@dp.callback_query_handler(state='*', text='done' )
async def inline_kb_answer_callback_handler(query: CallbackQuery, state: FSMContext):
    answer_data = query.data

    if answer_data == 'done':
        async with state.proxy() as data:
            TablesModerate().add_info(data['name'], data['url'])
            await state.finish()

            await query.message.answer('Кнопка добавлена', reply_markup=buttons.common())
