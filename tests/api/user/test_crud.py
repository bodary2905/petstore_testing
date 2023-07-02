"""Тесты CRUD User"""

import pytest
from http import HTTPStatus

from src.data_func import get_response_body
from src.api_entity.User.api_func import UserApiFunc
from src.api_entity.User.api_path import user_entity_name

USER_BODY_CREATE = {
    "username": "iivanov7",
    "firstName": "Ivan",
    "lastName": "Ivanov",
    "email": "iivanov@mail.ru",
    "password": "123456",
    "phone": "+79000000000",
    "userStatus": 0
}
USER_BODY_UPDATE = {
    "username": "iivanov_upd",
    "firstName": "Ivan_upd",
    "lastName": "Ivanov_upd",
    "email": "iivanov_upd@mail.ru",
    "password": "654321",
    "phone": "+79000000001",
    "userStatus": 1
}


@pytest.mark.positive
@pytest.mark.crud
@pytest.mark.user
def test_crud():
    """Тест CRUD для User"""
    # ---------- CREATE USER ----------
    response = UserApiFunc.create(USER_BODY_CREATE)
    assert response.status_code == HTTPStatus.OK, f"Wrong status code {user_entity_name}: create\n" \
                                                  f"Actual: {response.status_code}. Expected 200\n" \
                                                  f"Message: {response.text}"
    # получаем body user после create
    create_body = get_response_body(response, err_msg="Error in test_crud_user after create")
    assert create_body["code"] == HTTPStatus.OK, f"Wrong status code {user_entity_name} in body after create\n" \
                                                 f"Actual: {create_body['code']}. Expected 200\n" \
                                                 f"Body Message: {create_body['message']}"
    # ---------- GET USER ----------
    response = UserApiFunc.get(USER_BODY_CREATE["username"])
    assert response.status_code == HTTPStatus.OK, f"Wrong status code {user_entity_name}: get after create\n" \
                                                  f"Actual: {response.status_code}. Expected 200\n" \
                                                  f"Message: {response.text}"
    # получаем body user после get
    get_body = get_response_body(response, err_msg="Error in test_crud_user after get for create")
    # удаляем поле "id" из словаря
    id_user_create = get_body.pop("id")
    assert isinstance(id_user_create, int), "Wrong field with id in body get for create"
    # сравниваем отправленный и полученные словари
    assert USER_BODY_CREATE == get_body, f"Dict USER_BODY {USER_BODY_CREATE} not equal dict {get_body}"
    # ---------- UPDATE USER ----------
    response = UserApiFunc.update(USER_BODY_CREATE["username"], USER_BODY_UPDATE)
    assert response.status_code == HTTPStatus.OK, f"Wrong status code {user_entity_name} in body after update\n" \
                                                  f"Actual: {create_body['code']}. Expected 200\n" \
                                                  f"Body Message: {create_body['message']}"
    # получаем body user после update
    update_body = get_response_body(response, err_msg="Error in test_crud_user after update")
    assert update_body["code"] == HTTPStatus.OK, f"Wrong status code {user_entity_name}: update\n" \
                                                 f"Actual: {response.status_code}. Expected 200\n" \
                                                 f"Message: {response.text}"
    # ---------- GET USER ----------
    response = UserApiFunc.get(USER_BODY_UPDATE["username"])
    assert response.status_code == HTTPStatus.OK, f"Wrong status code {user_entity_name}: get after update\n" \
                                                  f"Actual: {response.status_code}. Expected 200\n" \
                                                  f"Message: {response.text}"
    # получаем body user после get
    get_body = get_response_body(response, err_msg="Error in test_crud_user after get for update")
    # удаляем поле "id" из словаря
    id_user_update = get_body.pop("id")
    assert isinstance(id_user_update, int), "Wrong field with id in body get for update"
    # сравниваем отправленный и полученные словари
    assert USER_BODY_UPDATE == get_body, f"Dict USER_BODY {USER_BODY_UPDATE} not equal dict {get_body}"
    # ---------- DELETE USER ----------
    response = UserApiFunc.delete(USER_BODY_CREATE["username"])
    assert response.status_code == HTTPStatus.OK, f"Wrong status code {user_entity_name} in body after delete\n" \
                                                  f"Actual: {create_body['code']}. Expected 200\n" \
                                                  f"Body Message: {create_body['message']}"
    # получаем body user после delete
    delete_body = get_response_body(response, err_msg="Error in test_crud_user after delete")
    assert delete_body["code"] == HTTPStatus.OK, f"Wrong status code {user_entity_name}: delete\n" \
                                                 f"Actual: {response.status_code}. Expected 200\n" \
                                                 f"Message: {response.text}"
    # ---------- GET USER ----------
    response = UserApiFunc.get(USER_BODY_CREATE["username"])
    get_body = get_response_body(response, err_msg="Error in test_crud_user after get for delete")
    if response.status_code == HTTPStatus.OK:  # так как может быть несколько user с одинаковыми именами
        assert get_body["id"] != id_user_create, f"User not deleted, field id found"
    else:
        assert response.status_code == HTTPStatus.NOT_FOUND, f"User not deleted, status line not equal Not Found"
        assert get_body["type"] == "error", f"Wrong field type after delete user"
        assert get_body["message"] == "User not found", f"Wrong field message after delete user"
