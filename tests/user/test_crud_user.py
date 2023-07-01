"""Тесты CRUD User"""

import pytest
from http import HTTPStatus

from src.data_func import get_response_body
from src.api_entity.User.api_func import UserApiFunc
from src.api_entity.User.api_path import user_entity_name

USER_BODY = {
    "username": "iivanov",
    "firstName": "Ivan",
    "lastName": "Ivanov",
    "email": "iivanov@mail.ru",
    "password": "123456",
    "phone": "+79000000000"
}


@pytest.mark.crud
@pytest.mark.user
def test_crud_user():
    """Тест CRUD для User"""

    response = UserApiFunc.create(USER_BODY)
    assert response.status_code == HTTPStatus.OK, f"Wrong status code {user_entity_name}: create\n" \
                                                  f"Actual: {response.status_code}. Expected 200\n" \
                                                  f"Message: {response.text}"
    body = get_response_body(response, err_msg="Error in test_crud_user after create")
    assert body["code"] == HTTPStatus.OK, f"Wrong status code {user_entity_name} in body after create\n" \
                                          f"Actual: {body['code']}. Expected 200\n" \
                                          f"Body Message: {body['message']}"


@pytest.mark.user
def test_dublicate_user():
    """Создаем одинаковых User"""

    response = UserApiFunc.create(USER_BODY)
    assert response.status_code == HTTPStatus.OK, f"Wrong status code {user_entity_name}: create\n" \
                                                  f"Actual: {response.status_code}. Expected 200\n" \
                                                  f"Message: {response.text}"
    response = UserApiFunc.create(USER_BODY)
    assert response.status_code == HTTPStatus.OK, f"Wrong status code {user_entity_name}: create\n" \
                                                  f"Actual: {response.status_code}. Expected 200\n" \
                                                  f"Message: {response.text}"
