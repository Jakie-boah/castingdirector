from aiogram import executor
from loguru import logger
from config import dp
from handlers.filter import SuperAdmin
import bot.imports
from Database.Database import CreateTables, TablesModerate

if __name__ == '__main__':

    logger.info("Бот запущен")
    dp.filters_factory.bind(SuperAdmin)
    CreateTables()
    #TablesModerate().add_new_info()
    executor.start_polling(dp)