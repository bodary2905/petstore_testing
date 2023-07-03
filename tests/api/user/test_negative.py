"""Тесты CRUD User"""

import pytest
from http import HTTPStatus

from src.api_entity.User.api_func import UserApiFunc
from src.api_entity.User.api_path import user_entity_name
from tests.api.user.test_crud import USER_BODY_CREATE


@pytest.mark.user
@pytest.mark.negative
def test_dublicate_user():
    """Пробуем создать одинаковых User"""

    response = UserApiFunc.create(USER_BODY_CREATE)
    assert response.status_code == HTTPStatus.OK, f"Wrong status code {user_entity_name}: create\n" \
                                                  f"Actual: {response.status_code}. Expected 200\n" \
                                                  f"Message: {response.text}"
    response = UserApiFunc.create(USER_BODY_CREATE)
    assert response.status_code == HTTPStatus.OK, f"Wrong status code {user_entity_name}: create\n" \
                                                  f"Actual: {response.status_code}. Expected 200\n" \
                                                  f"Message: {response.text}"
