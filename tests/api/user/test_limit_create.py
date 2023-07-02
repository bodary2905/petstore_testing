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

limit_values = [
    {
        "username": "q",
        "firstName": "w",
        "lastName": "e",
        "email": "post1@mail.ru",
        "password": "4m9ehK",
        "phone": "+79000000000",
        "userStatus": 1
    },
    {
        "username": "AwAfmEdNpngRF0YHMpHLJg9VjLb3iJwpNWEdiME8QEUuJSFSo6",
        "firstName": "9YPtkYg8T9jZNjtbF5cgyaNOWbyEvvhe61OFaJqfVYQLgi4xDs",
        "lastName": "2aB2bBalMFUFN5e3sZ5psMBi7ACH4FixmizCdf5672rtzEVF8I",
        "email": "post2@mail.ru",
        "password": "YqS5Ky7412PLRr3hdCKO",
        "phone": "+79000000001",
        "userStatus": 9
    }
]


@pytest.mark.positive
@pytest.mark.user
@pytest.mark.limit_create
@pytest.mark.parametrize("limit", limit_values)
def test_limit(limit):
    """Тест граничных значений для User на create"""
    # ---------- CREATE USER ----------
    response = UserApiFunc.create(limit)
    assert response.status_code == HTTPStatus.OK, f"Wrong status code {user_entity_name}: create for limit_create\n" \
                                                  f"Actual: {response.status_code}. Expected 200\n" \
                                                  f"Message: {response.text}"
    # получаем body user после create
    create_body = get_response_body(response, err_msg="Error in test_limit after create")
    assert create_body[
               "code"] == HTTPStatus.OK, f"Wrong status code {user_entity_name} in body after create for limit_create\n" \
                                         f"Actual: {create_body['code']}. Expected 200\n" \
                                         f"Body Message: {create_body['message']}"
    # ---------- GET USER ----------
    response = UserApiFunc.get(limit["username"])
    assert response.status_code == HTTPStatus.OK, f"Wrong status code {user_entity_name}: get after create for limit_create\n" \
                                                  f"Actual: {response.status_code}. Expected 200\n" \
                                                  f"Message: {response.text}"
    # получаем body user после get
    get_body = get_response_body(response, err_msg="Error in test_limit after get for create limit_create")
    # удаляем поле "id" из словаря
    id_user_create = get_body.pop("id")
    assert isinstance(id_user_create, int), "Wrong field with id in body get for create limit_create"
    # сравниваем отправленный и полученные словари
    assert limit == get_body, f"Dict limit {limit} not equal dict {get_body} for limit_create"
    # ---------- DELETE USER ----------
    response = UserApiFunc.delete(limit["username"])
    assert response.status_code == HTTPStatus.OK, f"Wrong status code {user_entity_name} in body after delete for limit_create\n" \
                                                  f"Actual: {create_body['code']}. Expected 200\n" \
                                                  f"Body Message: {create_body['message']}"
    # получаем body user после delete
    delete_body = get_response_body(response, err_msg="Error in test_limit after delete for limit_create")
    assert delete_body["code"] == HTTPStatus.OK, f"Wrong status code {user_entity_name}: delete for limit_create\n" \
                                                 f"Actual: {response.status_code}. Expected 200\n" \
                                                 f"Message: {response.text}"
    # ---------- GET USER ----------
    response = UserApiFunc.get(limit["username"])
    get_body = get_response_body(response, err_msg="Error in test_limit after get for delete limit_create")
    if response.status_code == HTTPStatus.OK:  # так как может быть несколько user с одинаковыми именами
        assert get_body[
                   "id"] != id_user_create, f"User not deleted, field id found. Error in test_limit for limit_create"
    else:
        assert response.status_code == HTTPStatus.NOT_FOUND, f"User not deleted, status line not equal Not Found. Error in test_limit for limit_create"
        assert get_body["type"] == "error", f"Wrong field type after delete user.  Error in test_limit for limit_create"
        assert get_body[
                   "message"] == "User not found", f"Wrong field message after delete user.  Error in test_limit for limit_create"
