from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup


class InlineButtons:

    def common(self):
        markup = InlineKeyboardMarkup(row_width=2)
        menu = InlineKeyboardButton('◀ На главную', callback_data='start')
        return markup.add(menu)

    def introduce(self):
        markup = InlineKeyboardMarkup(row_width=2)
        menu = InlineKeyboardButton('📃 Меню', callback_data='menu')
        reviews = InlineKeyboardButton('📣 Отзывы', callback_data='reviews')
        drugs = InlineKeyboardButton('🙏 Товары которые я рекомендую', callback_data='drugs')
        return markup.add(menu, reviews, drugs)

    def admin_options(self):

        markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        info_1 = KeyboardButton('/1')
        info_2 = KeyboardButton('/2')
        info_3 = KeyboardButton('/3')
        info_4 = KeyboardButton('/4')
        info_5 = KeyboardButton('/5')
        info_6 = KeyboardButton('/6')

        return markup.add(info_1, info_2, info_3, info_4, info_5, info_6)

    def reviews_buttons(self):
        markup = InlineKeyboardMarkup(row_width=2)
        video_review = InlineKeyboardButton('📹 Видео отзывы', callback_data='video_review')
        hand_review = InlineKeyboardButton('✉ Письменные отзывы', callback_data='hand_review')
        back = InlineKeyboardButton('◀ Назад', callback_data='start')
        return markup.add(video_review, hand_review, back)


