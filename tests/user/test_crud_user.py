"""Тесты CRUD User"""

import pytest

from src.api_entity.User.api_func import UserApiFunc
from src.api_entity.User.api_path import user_entity_name


@pytest.mark.crud
@pytest.mark.user
def test_crud_user():
    """Тест CRUD для User"""
