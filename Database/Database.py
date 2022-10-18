from config import USER, PASSWORD, PORT, Host, DATABASE, DB_URI
import psycopg2
from loguru import logger

# user=user, password=password, host=host, port=port, database=db
class Database:

    def __init__(self, user=USER, password=PASSWORD, host=Host, port=PORT, db=DATABASE):
        self.conn = psycopg2.connect(DB_URI, sslmode='require')
        self.cur = self.conn.cursor()

    def create(self, table):
        self.cur.execute(table)
        self.conn.commit()
        logger.info("Таблица успешно создана в PostgreSQL")

    def insert(self, insert, *args):
        self.cur.execute(insert, (args))
        self.conn.commit()
        logger.info("В таблицу успешно добавлены новые данные")

    def get_chats(self):
        self.cur.execute('select * from info')
        chat_records = self.cur.fetchall()
        return chat_records


class CreateTables:
    def __init__(self):
        self.db = Database()

        self.db.create("""
            CREATE TABLE IF NOT EXISTS info (

           
            info_1 text NOT NULL,
            info_2 text NOT NULL,
            info_3 text,
            info_4 text,
            info_5 text,
            info_6 text
            
            )""")


class TablesModerate:
    def __init__(self):
        self.db = Database()

    def add_new_info(self):

        self.db.insert("""
        INSERT INTO info (info_1, info_2, info_3, info_4, info_5, info_6)
        VALUES (%s, %s, %s, %s, %s, %s);

        """, 'Меню', 'Содержание меню', 'Отзывы', 'Видео Отзывы', 'Письменные отзывы', 'Товары которые я советую')

    def change_info(self, info_num, new_info):

        self.db.insert(f"""
        UPDATE info SET info_{info_num}=%s""", new_info)
        logger.info("Правил")

