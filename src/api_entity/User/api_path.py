"""
    API-пути для данной сущности
"""
from enum import Enum
from strenum import StrEnum

from src.config import base_url

# название api-сущности
user_entity_name = "user"

class UserPath(StrEnum):
    """Локальные пути"""
    create = f"{user_entity_name}"
    createWithArray = f"{user_entity_name}/createWithArray"
    createWithList = f"{user_entity_name}/createWithList"
    get = f"{user_entity_name}"
    put = f"{user_entity_name}"
    delete = f"{user_entity_name}"


class UserFullPath(StrEnum):
    """Полные пути"""
    create = f"{base_url}/v2/{UserPath.create}"
    createWithArray = f"{base_url}/v2/{UserPath.createWithArray}"
    createWithList = f"{base_url}/v2/{UserPath.createWithList}"
    get = f"{base_url}/v2/{UserPath.get}"
    put = f"{base_url}/v2/{UserPath.put}"
    delete = f"{base_url}/v2/{UserPath.delete}"


if __name__ == "__main__":
    # для теста
    print(UserFullPath.create)
    print(UserFullPath.create.createWithArray)
    print(UserFullPath.create.createWithList)
    print(UserFullPath.get)
    print(UserFullPath.put)
    print(UserFullPath.delete)
