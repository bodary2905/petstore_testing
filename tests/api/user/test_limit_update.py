"""Тесты CRUD User"""

import pytest
from http import HTTPStatus

from src.data_func import get_response_body
from src.api_entity.User.api_func import UserApiFunc
from src.api_entity.User.api_path import user_entity_name

# ---------- LIMIT VALUES ----------
# Зададим произвольные граничные значения для полей сущности User:
# username: str, [1, 50]
# firstName: str, [1, 50]
# lastName: str, [1, 50]
# email: str, email
# password: str, [6, 20]
# phone: str, 11 integers
# userStatus: int, [0, 9]

typical_values = {
    "username": "apopov",
    "firstName": "Alex",
    "lastName": "Popov",
    "email": "apopov@mail.ru",
    "password": "qwerty",
    "phone": "+71234567890",
    "userStatus": 1
}

limit_values = [
    {
        "username": "1",
        "firstName": "2",
        "lastName": "3",
        "email": "post3@mail.ru",
        "password": "vxevrT",
        "phone": "+79000000002",
        "userStatus": 1
    },
    {
        "username": "93haYlRI2zcByGWYNFa0S51FAP5kBElRLKWcqCUtZeQvtmwuip",
        "firstName": "VPhqsIiX5PPuyoK0g0KYKMzF4xW0pelwoXFMQOWw0dCuqsRvts",
        "lastName": "dsFX7fKSFdQZ9ZQYJw4krHrGXiuzM0TkIa5tRA7ZvFDBP17aRe",
        "email": "post4@mail.ru",
        "password": "eN4uIeBJ5fsgMKVDvACq",
        "phone": "+79000000003",
        "userStatus": 9
    }
]


@pytest.mark.positive
@pytest.mark.user
@pytest.mark.limit_update
@pytest.mark.parametrize("limit", limit_values)
def test_limit(limit):
    """Тест граничных значений для User на update"""
    # ---------- CREATE USER ----------
    response = UserApiFunc.create(typical_values)
    assert response.status_code == HTTPStatus.OK, f"Wrong status code {user_entity_name}: create for limit in typical_values\n" \
                                                  f"Actual: {response.status_code}. Expected 200\n" \
                                                  f"Message: {response.text}"
    # получаем body user после create
    create_body = get_response_body(response,
                                    err_msg="Error in test_limit for create after create for limit in typical_values")
    assert create_body[
               "code"] == HTTPStatus.OK, f"Wrong status code {user_entity_name} in body after create for limit in typical_values\n" \
                                         f"Actual: {create_body['code']}. Expected 200\n" \
                                         f"Body Message: {create_body['message']}"
    # ---------- GET USER ----------
    response = UserApiFunc.get(typical_values["username"])
    assert response.status_code == HTTPStatus.OK, f"Wrong status code {user_entity_name}: get after create for limit in typical_values\n" \
                                                  f"Actual: {response.status_code}. Expected 200\n" \
                                                  f"Message: {response.text}"
    # получаем body user после get
    get_body = get_response_body(response, err_msg="Error in test_limit after get for create limit in typical_values")
    # удаляем поле "id" из словаря
    id_user_create = get_body.pop("id")
    assert isinstance(id_user_create, int), "Wrong field with id in body get for create limit in typical_values"
    # сравниваем отправленный и полученные словари
    assert typical_values == get_body, f"Dict limit {limit} not equal dict {get_body} for limit_update"
    # ---------- UPDATE USER ----------
    response = UserApiFunc.update(typical_values["username"], limit)
    assert response.status_code == HTTPStatus.OK, f"Wrong status code {user_entity_name} in body after update for limit_update\n" \
                                                  f"Actual: {create_body['code']}. Expected 200\n" \
                                                  f"Body Message: {create_body['message']}"
    # получаем body user после update
    update_body = get_response_body(response, err_msg="Error in test_limit after update for limit_update")
    assert update_body["code"] == HTTPStatus.OK, f"Wrong status code {user_entity_name}: update for limit_update\n" \
                                                 f"Actual: {response.status_code}. Expected 200\n" \
                                                 f"Message: {response.text}"
    # ---------- GET USER ----------
    response = UserApiFunc.get(limit["username"])
    assert response.status_code == HTTPStatus.OK, f"Wrong status code {user_entity_name}: get after update for limit_update\n" \
                                                  f"Actual: {response.status_code}. Expected 200\n" \
                                                  f"Message: {response.text}"
    # получаем body user после get
    get_body = get_response_body(response, err_msg="Error in test_limit after get for limit_update")
    # удаляем поле "id" из словаря
    id_user_update = get_body.pop("id")
    assert isinstance(id_user_update, int), "Wrong field with id in body get for limit_update"
    # сравниваем отправленный и полученные словари
    assert limit == get_body, f"Dict USER_BODY {limit} not equal dict {get_body} for limit_update"
    # ---------- DELETE USER ----------
    response = UserApiFunc.delete(limit["username"])
    assert response.status_code == HTTPStatus.OK, f"Wrong status code {user_entity_name} in body after delete for limit_update\n" \
                                                  f"Actual: {create_body['code']}. Expected 200\n" \
                                                  f"Body Message: {create_body['message']}"
    # получаем body user после delete
    delete_body = get_response_body(response, err_msg="Error in test_limit after delete for limit")
    assert delete_body["code"] == HTTPStatus.OK, f"Wrong status code {user_entity_name}: delete\n" \
                                                 f"Actual: {response.status_code}. Expected 200\n" \
                                                 f"Message: {response.text}"
    # ---------- GET USER ----------
    response = UserApiFunc.get(limit["username"])
    get_body = get_response_body(response, err_msg="Error in test_limit after get for delete limit_update")
    if response.status_code == HTTPStatus.OK:  # так как может быть несколько user с одинаковыми именами
        assert get_body[
                   "id"] != id_user_create, f"User not deleted, field id found. Error in test_limit for limit_update"
    else:
        assert response.status_code == HTTPStatus.NOT_FOUND, f"User not deleted, status line not equal Not Found. Error in test_limit for limit_update"
        assert get_body["type"] == "error", f"Wrong field type after delete user.  Error in test_limit for limit_update"
        assert get_body[
                   "message"] == "User not found", f"Wrong field message after delete user.  Error in test_limit for limit_update"
