from src.db_entity.User.db_func import UserDBFunc

USER_DATA_CREATE = {
    "id": 143,
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
USER_DATA_UPDATE = {
    "first_name": "Ivan_update",
    "last_name": "Ivanov_update",
    "full_name": "Ivan Ivanov update",
    "job_title": "manager_update",
    "job_type": "boss_update",
    "phone": "+79000000001",
    "email": "iivanov_update@mail.ru",
    "image": "iivanov_update.jpg",
    "country": "Russia_update",
    "city": "Tomsk_update",
    "onboarding_completion": 2
}


def test_crud(db_client):
    """Тест CRUD для User через запросы к БД"""
    # ---------- CREATE USER ----------
    UserDBFunc.create(db_client, USER_DATA_CREATE)
    # ---------- GET USER ----------
    user_create = UserDBFunc.get_by_id(db_client, USER_DATA_CREATE["id"])
    tuple_user_create = tuple(user_create[0])
    id_user_create = tuple_user_create[0]
    tuple_user_data_create = tuple(USER_DATA_CREATE.values())
    assert tuple_user_data_create == tuple_user_create, f"tuple_user_data_create {tuple_user_data_create} not equal tuple_user_create {tuple_user_create}"
    # ---------- UPDATE USER ----------
    UserDBFunc.update_by_id(db_client, USER_DATA_CREATE["id"], USER_DATA_UPDATE)
    # ---------- GET USER ----------
    user_update = UserDBFunc.get_by_id(db_client, USER_DATA_CREATE["id"])
    tuple_user_update = tuple(user_update[0])
    tuple_user_data_update = tuple(USER_DATA_UPDATE.values())
    id_user_update = tuple_user_update[0]
    assert id_user_update == id_user_create, f"id_user_update {id_user_update} not equal id_user_create {id_user_create}"
    assert tuple_user_data_update == tuple_user_update[
                                     1:], f"tuple_user_data_update {tuple_user_data_update} not equal tuple_user_update {tuple_user_update}"
    # ---------- DELETE USER ----------
    UserDBFunc.delete_by_id(db_client, USER_DATA_CREATE["id"])
    # ---------- GET USER ----------
    assert len(
        UserDBFunc.get_by_id(db_client, USER_DATA_CREATE["id"])) == 0, "Error: delete User from table UNSUCCESSFUL!"
