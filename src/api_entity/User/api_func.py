"""
    API-функции для работы с сущностью User
"""

from http import HTTPStatus
import requests

# from src.data_func import get_response_body
from src.api_entity.User.api_path import UserFullPath



class UserApiFunc:
    @staticmethod
    def create(user_body: dict, **kwargs):
        """Создаем User-а"""
        return requests.post(url=UserFullPath.create, json=user_body, **kwargs)

    @staticmethod
    def create_with_list(user_list: list, **kwargs):
        """Создаем User-ов из list"""
        return requests.post(url=UserFullPath.createWithList, json=user_list, **kwargs)

    @staticmethod
    def create_with_array(user_list: list, **kwargs):
        """Создаем User-ов из list"""
        return requests.post(url=UserFullPath.createWithArray, json=user_list, **kwargs)

    @staticmethod
    def get(user_name: str, **kwargs):
        """Получаем User-а"""
        return requests.get(url=f"{UserFullPath.get}/{user_name}", **kwargs)

    @staticmethod
    def update(user_name: str, user_body: dict, **kwargs):
        """Обновляем User-а"""
        return requests.put(url=f"{UserFullPath.put}/{user_name}", json=user_body, **kwargs)

    @staticmethod
    def delete(user_name: str, **kwargs):
        return requests.delete(url=f"{UserFullPath.delete}/{user_name}", **kwargs)


if __name__ == "__main__":
    user_body = {
        "username": "iivanov",
        "firstName": "Ivan",
        "lastName": "Ivanov",
        "email": "iivanov@mail.ru",
        "password": "123456",
        "phone": "+79000000000"
    }
    response = UserApiFunc.create(user_body)
    assert response.status_code == HTTPStatus.OK, f"Wrong status code {user_entity_name}: create\n" \
                                                  f"Actual: {response.status_code}. Expected 200\n" \
                                                  f"Message: {response.text}"
    response = UserApiFunc.create_with_list([user_body, user_body])
    assert response.status_code == HTTPStatus.OK, f"Wrong status code {user_entity_name}: create_with_list\n" \
                                                  f"Actual: {response.status_code}. Expected 200\n" \
                                                  f"Message: {response.text}"
