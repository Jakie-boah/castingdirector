from aiogram import executor
from loguru import logger
from config import dp
from handlers.filter import SuperAdmin
import bot.menu
from Database.Database import CreateTables, TablesModerate, Database

a = 1
if __name__ == '__main__':

    logger.info("Бот запущен")
    dp.filters_factory.bind(SuperAdmin)
    CreateTables()
    if a == 1:
        TablesModerate().add_new_info()
        a+=1
    # print(Database().get_chats())

    executor.start_polling(dp)




















