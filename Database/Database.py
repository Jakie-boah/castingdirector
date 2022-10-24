from config import USER, PASSWORD, PORT, Host, DATABASE, DB_URI
import psycopg2
from loguru import logger

# user=user, password=password, host=host, port=port, database=db


class Database:

    def __init__(self, user=USER, password=PASSWORD, host=Host, port=PORT, db=DATABASE):
        self.conn = psycopg2.connect(DB_URI, sslmode='require')

    # def __init__(self, user=USER, password=PASSWORD, host='127.0.0.1', port='5432', db='back_info'):
    #
    #     self.conn = psycopg2.connect(user=user, password=password, host=host, port=port, database=db)
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
        self.cur.execute('select * from buttons')
        chat_records = self.cur.fetchall()
        return chat_records


class CreateTables:
    def __init__(self):
        self.db = Database()

        self.db.create("""
            CREATE TABLE IF NOT EXISTS buttons (

            id serial PRIMARY KEY,
            button_name text NOT NULL,
            url text NOT NULL
            
            
            )""")


class TablesModerate:
    def __init__(self):
        self.db = Database()

    def change_text(self, info_num, new_info):

        self.db.insert(f"""
        UPDATE buttons SET button_name=%s WHERE id={info_num}""", new_info)
        logger.info("Правил")

    def change_link(self, info_num, new_link):

        self.db.insert(f"""
        UPDATE buttons SET url=%s WHERE id={info_num}""", new_link)
        logger.info("Правил")

    def delete_button(self, info_num):
        self.db.insert(f"""
        DELETE from buttons  WHERE id={info_num}""")
        logger.info("Удалил")

    def add_info(self, name, url):
        self.db.insert("""
                INSERT INTO buttons (button_name, url)
                VALUES (%s, %s);

                """, name, url)
