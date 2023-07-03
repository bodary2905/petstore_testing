# Автотесты для приложения [SwaggerPetStore](https://petstore.swagger.io/)

Автотесты написаны для локально развернутого сервиса SwaggerPetStore в Docker-контейнере, так как версия на
сайте [https://petstore.swagger.io](https://petstore.swagger.io) имеет урезанный функционал. Там нельзя нормально
создать, удалить, обновить user-а. Так же вместо `venv` использован `poetry`.

## Описание проекта

* в папке [src](src) находится вспомогательный код (микро-фреймворк) для более удобного написания тестов
    * в [api_entity](src/api_entity) реализована "обертка" для отправки API-запросов с помощью библиотеки `request`
    * в [db_entity](src/db_entity) реализована "обертка" для отправки SQL-запросов с помощью библиотеки `psycopg2`
* в файле [config.py](src/config.py) осуществляется загрузка переменных среды из
  файла [.env](.env). Обычно `.env` файл помещают в [.gitignore](.gitignore), но для проверки тестового задания оставила
  его в репозитории
* в файле [db_client.py](src/db_client.py) реализован клиент для подключения к БД с помощью `psycopg2`
* в папке [tests](tests) хранятся файлы с тестами
    * в папке [api](tests/api) реализованы тесты для проверки API-запросов
        * в [test_crud.py](tests/api/user/test_crud.py) реализован тест с операциями CRUD для user
        * в [test_limit_create.py](tests/api/user/test_limit_create.py)
          и [test_limit_update.py](tests/api/user/test_limit_update.py) реализованы тесты для проверки граничных
          значений. Граничные значения были заданы самостоятельно (просто для примера)
        * в [test_negative.py](tests/api/user/test_negative.py) должны были располагаться негативные тесты для user, но
          они требуют более глубокого исследования системы, поэтому не были реализованы
    * в папке [db](tests/db) реализованы тесты для проверки SQL-запросов
        * в [test_crud.py](tests/db/test_crud.py) реализован тест с операциями CRUD для user
    * в файле [conftest.py](tests/conftest.py) реализованы фикстуры, которые используются в тестах
* в файле [setup.cfg](setup.cfg) хранятся маркеры для запуска конкретных тестов

## Развертывание сервиса

1. Клонировать репозиторий с GitHub:

   ```
   git clone https://github.com/bodary2905/petstore_testing
   ```

2. Установить библиотеки с помощью **poetry**:

   ```
   poetry install
   ```
3. Активировать виртуальное окружение **poetry**:
   ```
   poetry shell
   ```
4. Запустить сервис SwaggerPetstore в Docker-контейнере, выполнив команду:
    ```
   docker-compose up
   ```
5. После окончания работы выполнить:
    ```
   docker-compose down
   ```

## Запуск тестов

* запуск всех тестов с сохранением Allure-отчета в папку results

   ```
   pytest --alluredir results
   ```

* запуск тестов с использованием pytest-маркеров (полный список маркеров в [setup.cfg](setup.cfg)) + с сохранением
  Allure-отчета в папку results

   ```
   pytest -m "db and crud" --alluredir results
   ```

## Формирование Allure-отчета

   ```
   allure serve results
   ```