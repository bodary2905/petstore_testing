"""
    Конфигурационный файл
"""

import os
from dotenv import load_dotenv

load_dotenv()  # загружаем все env-переменные из .env файла

# PETSTORE_URL
_url_str = os.getenv("PETSTORE_URL")
_port_str = os.getenv("PETSTORE_PORT")
base_url = f"{_url_str}:{_port_str}/"

if __name__ == "__main__":
    # для теста
    print(base_url)
