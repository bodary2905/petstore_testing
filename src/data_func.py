"""
    Функции для "общей" обработки данных
"""
from requests import Response
from json import JSONDecodeError


def get_response_body(response: Response, err_msg):
    """Пытаемся получить body из response"""
    try:
        body = response.json()
    except JSONDecodeError:
        raise TypeError(f"{err_msg}: response body НЕ JSON!")
    return body

