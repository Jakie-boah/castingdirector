from config import dp, bot
from aiogram.types import Message, CallbackQuery
from handlers.InlineButtons import InlineButtons
from handlers.filter import SuperAdmin
from aiogram.dispatcher.filters import Command
from Database.Database import Database, TablesModerate


buttons = InlineButtons()
com = ''

@dp.message_handler(Command("ad^minka"), SuperAdmin())
async def f(message: Message):
    info = Database().get_chats()
    await message.answer(f'Выбери что изменить и нажми на соответсвующую кнопку:\n\n'
                         f' 1⃣:\n {info[0][0]}\n'
                         f' 2⃣:\n {info[0][1]}\n'
                         f' 3⃣:\n {info[0][2]}\n'
                         f' 4⃣:\n {info[0][3]}\n'
                         f' 5⃣:\n {info[0][4]}\n'
                         f' 6⃣:\n {info[0][5]}\n', disable_web_page_preview=True, reply_markup=buttons.admin_options())


@dp.message_handler(Command(['1', '2', '3', '4', '5', '6']), SuperAdmin())
async def f(message: Message):
    global com

    com = message.text[1:]

    info = Database().get_chats()

    await message.answer(f'Изменить инфо в:\n\n {info[0][int(com)-1]}\n\n Для того чтобы изменить, отправь боту новую информацию и он сам все сделает')


@dp.message_handler(SuperAdmin())
async def changed(message: Message):
    global com
    try:
        TablesModerate().change_info(com, message.text)
        com = ''

        await message.answer(text=f'Исправлено на:\n\n {message.text}', reply_markup=
                                    buttons.common())
    except:
        pass









