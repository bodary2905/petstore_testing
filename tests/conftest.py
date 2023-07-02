"""
    Общие фикстуры для тестов
"""
import os
import pytest

import src.config  # чтобы подгрузились env-переменные
from src.db_client import DBClient


@pytest.fixture(scope="session")
def db_client():
    """Получаем клиента к БД"""
    db_credential = (
        os.getenv("DB_NAME"),
        os.getenv("DB_USER"),
        os.getenv("DB_PASSWORD"),
        os.getenv("DB_HOST"),
        os.getenv("DB_PORT")
    )
    db_client = DBClient()
    db_client.create_connection(*db_credential)
    yield db_client
    db_client.close_connection()
