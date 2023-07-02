"""
    Функции для работы с сущностью User через БД
"""

user_table_name = "public.users"  # название таблицы в БД
user_table_headers = ["id", "first_name", "last_name", "full_name", "job_title", "job_type", "phone", "email",
                      "image", "country", "city", "onboarding_completion"]  # заголовки в таблице public.users


class UserDBFunc:
    @staticmethod
    def create(db_client, user_data: dict):
        """Добавляем нового User-а в таблицу"""
        values_str = UserDBFunc._create_values_from_user_data_for_insert(user_data)
        insert_sql = f"INSERT INTO {user_table_name} ({', '.join(user_table_headers)}) " \
                     f"VALUES ({values_str});"
        db_client.execute_query(insert_sql)

    @staticmethod
    def get_by_id(db_client, user_id: int):
        """Получаем User-а из таблицы"""
        select_sql = f"SELECT * FROM {user_table_name} WHERE id = {user_id};"
        return db_client.execute_read_query(select_sql)

    @staticmethod
    def update_by_id(db_client, user_id: int, user_data: dict):
        """Обновляем User-а в таблице"""
        set_str = UserDBFunc._create_set_from_user_data_for_update(user_data)
        update_sql = f"UPDATE {user_table_name} SET {set_str} WHERE id={user_id};"
        db_client.execute_query(update_sql)

    @staticmethod
    def delete_by_id(db_client, user_id: int):
        delete_sql = f"DELETE FROM {user_table_name} WHERE id={user_id};"
        db_client.execute_query(delete_sql)

    @staticmethod
    def _create_values_from_user_data_for_insert(user_data: dict):
        """Формируем строку из user_data для блока VALUES в INSERT запросе"""
        values_str = ""
        for value in user_data.values():
            if isinstance(value, str):
                values_str += f"'{value}', "
            elif isinstance(value, int):
                values_str += f"{value}, "
        return values_str[:-2]

    @staticmethod
    def _create_set_from_user_data_for_update(user_data: dict):
        """Формируем строку из user_data для блока SET в UPDATE запросе"""
        set_str = ""
        for key, value in user_data.items():
            if isinstance(value, str):
                set_str += f"{key}='{value}', "
            elif isinstance(value, int):
                set_str += f"{key}={value}, "
        return set_str[:-2]


if __name__ == "__main__":
    # для теста
    import os

    import src.config
    from src.db_client import DBClient

    user_data = {
        "id": 141,
        "first_name": "Ivan",
        "last_name": "Ivanov",
        "full_name": "Ivan Ivanov",
        "job_title": "manager",
        "job_type": "boss",
        "phone": "+79000000000",
        "email": "iivanov@mail.ru",
        "image": "iivanov.jpg",
        "country": "Russia",
        "city": "Tomsk",
        "onboarding_completion": 1
    }

    db_credential = (
        os.getenv("DB_NAME"),
        os.getenv("DB_USER"),
        os.getenv("DB_PASSWORD"),
        os.getenv("DB_HOST"),
        os.getenv("DB_PORT")
    )
    db_client = DBClient()
    db_client.create_connection(*db_credential)
    UserDBFunc.create(db_client, user_data)
    print("create:\n" + str(UserDBFunc.get_by_id(db_client, user_data["id"])))
    user_update_data = {
        "first_name": "Ivan2",
        "last_name": "Ivanov2",
        "full_name": "Ivan Ivanov2",
        "job_title": "manager2",
        "job_type": "boss2",
        "phone": "+790000000002",
        "email": "iivanov@mail.ru2",
        "image": "iivanov.jpg2",
        "country": "Russia2",
        "city": "Tomsk2",
        "onboarding_completion": 2
    }
    UserDBFunc.update_by_id(db_client, user_data["id"], user_update_data)
    print("update:\n" + str(UserDBFunc.get_by_id(db_client, user_data["id"])))
    UserDBFunc.delete_by_id(db_client, user_data["id"])
    assert len(UserDBFunc.get_by_id(db_client, user_data["id"])) == 0, "Error: delete User from table UNSUCCESSFUL!"

    db_client.close_connection()
