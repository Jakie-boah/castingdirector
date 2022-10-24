from Database.Database import Database


numbers = ['1⃣', '2⃣', '3⃣', '4⃣', '5⃣', '6⃣', '7⃣', '8⃣', '9⃣', '🔟']


def admin_beg():
    info = Database().get_chats()

    back = {}
    for i in info:
        back[i[0]] = {'Название': i[1], 'Ссылка': i[2]}

    text = ''

    for i in back:

        row = f'\n{numbers[i-1]}: \n\n' \
              f'Текст кнопки: {back[i]["Название"]}\n' \
              f'Ссылка кнопки: {back[i]["Ссылка"]}\n'
        text += row

    return text