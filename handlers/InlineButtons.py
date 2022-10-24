from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from Database.Database import Database


class InlineButtons:

    def common(self):
        markup = InlineKeyboardMarkup(row_width=2)
        menu = InlineKeyboardButton('◀ На главную', callback_data='start')
        return markup.add(menu)

    def introduce(self):
        C = []
        markup = InlineKeyboardMarkup(row_width=2)
        for i in Database().get_chats():
            C.append(InlineKeyboardButton(text=i[1], url=f'{i[2]}',  callback_data=f'{i[0]}'))
        c = 0
        for i in C:
            markup.row(*C[c:c+2])
            c += 2
        return markup

    def admin_options(self):
        markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        for i in Database().get_chats():
            markup.add('/' + str(i[0]))
        markup.add('/Добавить кнопку')
        return markup

    def info_or_link(self):
        markup = InlineKeyboardMarkup(row_width=3)
        text = InlineKeyboardButton('📋 Текст', callback_data='text')
        link = InlineKeyboardButton('📡 Ссылку', callback_data='link')
        delete = InlineKeyboardButton('❌ Удалить кнопку', callback_data='delete')
        menu = InlineKeyboardButton('◀ На главную', callback_data='start')
        markup.add(text, link, delete, menu)
        return markup

    def sure(self):
        markup = InlineKeyboardMarkup(row_width=2)
        yes = InlineKeyboardButton('Да', callback_data='yes')
        no = InlineKeyboardButton('Нет', callback_data='start')
        markup.add(yes, no)
        return markup

    def done(self):
        markup = InlineKeyboardMarkup(row_width=2)
        done = InlineKeyboardButton('Готово', callback_data='done')
        markup.add(done)
        return markup
