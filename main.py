from aiogram import executor
from loguru import logger
from config import dp
from handlers.filter import SuperAdmin
import bot.menu
from Database.Database import CreateTables, TablesModerate, Database


if __name__ == '__main__':

    logger.info("Бот запущен")

    CreateTables()
    #TablesModerate().add_new_info()
    # print(Database().get_chats())
    dp.filters_factory.bind(SuperAdmin)
    executor.start_polling(dp)




















