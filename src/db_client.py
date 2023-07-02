"""
    Клиент для работы с DB Postgress
"""

import psycopg2
from psycopg2 import OperationalError, DatabaseError


class DBClient:
    """Клиент для работы с БД"""

    def __init__(self):
        self.connection = None

    def create_connection(self, db_name, db_user, db_password, db_host, db_port: str):
        """Создаем connection к Postgress"""
        try:
            # пытаемся подключиться к бд
            self.connection = psycopg2.connect(
                database=db_name,
                user=db_user,
                password=db_password,
                host=db_host,
                port=int(db_port),
            )
            # настраиваем connection
            self.connection.set_session(readonly=False, autocommit=True)
            print("Connection to PostgreSQL DB successful")
        except OperationalError as e:
            raise DatabaseError(f"The error on create_connection to PostgreSQL DB") from e

    def close_connection(self):
        """Закрываем connection к Postgress"""
        try:
            self.connection.close()
            print("Close connection to PostgreSQL DB successful")
        except Exception as e:
            raise DatabaseError(f"The error on close_connection to PostgreSQL DB") from e

    def execute_read_query(self, query):
        """Послылаем SQL запрос и ждем ответ от БД"""
        try:
            with self.connection:
                with self.connection.cursor() as cursor:
                    cursor.execute(query)
                    result = cursor.fetchall()
                    return result
        except Exception as e:
            raise DatabaseError(f"The error on execute_read_query to PostgreSQL DB") from e

    def execute_query(self, query):
        """Послылаем SQL запрос и НЕ ждем ответ от БД"""
        try:
            with self.connection:
                with self.connection.cursor() as cursor:
                    cursor.execute(query)
        except Exception as e:
            raise DatabaseError(f"The error on execute_query to PostgreSQL DB") from e


if __name__ == "__main__":
    # для теста
    import os

    import src.config

    db_credential = (
        os.getenv("DB_NAME"),
        os.getenv("DB_USER"),
        os.getenv("DB_PASSWORD"),
        os.getenv("DB_HOST"),
        os.getenv("DB_PORT")
    )
    db_client = DBClient()
    db_client.create_connection(*db_credential)
    USERS_TABLE_NAME = "public.users"
    # simle select
    select_users_sql = f"select * from {USERS_TABLE_NAME}"
    result = db_client.execute_read_query(select_users_sql)
    print(result[:2])
    # # insert new row
    # USERS_TABLE_HEADERS = ["id", "first_name", "last_name", "full_name", "job_title", "job_type", "phone", "email",
    #                        "image", "country", "city", "onboarding_completion"]
    # insert_user_sql = f"INSERT INTO {USERS_TABLE_NAME} ({', '.join(USERS_TABLE_HEADERS)}) " \
    #                   "VALUES (132, 'Kattie2', 'Hane2', 'Darrel Champlin2', 'Senior Data Orchestrator2', 'District2', " \
    #                   "'292.479.28312', 'Kirk_Torphy922@gmail.com', 'https://cdn.fakercloud.com/avatars/antjanus_128.jpg', " \
    #                   "'Berkshire2', 'New Gaetano2', 83);"
    # db_client.execute_query(insert_user_sql)
    db_client.close_connection()
