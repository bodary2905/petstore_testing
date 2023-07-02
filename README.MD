# Автотесты для приложения [SwaggerPetStore](https://petstore.swagger.io/)

Автотесты написаны для локально развернутого сервиса SwaggerPetStore в Docker-контейнере, так как версия на
сайте [https://petstore.swagger.io](https://petstore.swagger.io) имеет урезанный функционал. Там нельзя нормально
создать, удалить, обновить user-а. Так же вместо `venv` использован `poetry`.

## Описание проекта

* в папке [src](src) находится вспомогательный код (микро-фремворк) для более удобного написания тестов
    * в [api_entity](src/api_entity) реализована "обертка" для отправки API-запросов с помощью библиотеки `request`
    * в [db_entity](src/db_entity) реализована "обертка" для отправки SQL-запросов с помощью библиотеки `psycopg2`
* в файле [config.py](src/config.py) осуществляется загрузка переменных среды из
  файла [.env](.env)
* в файле [data_func.py](src/data_func.py) находятся функии для "общей" обработки данных
* в файле [db_client.py](src/db_client.py) реализован коиент для подключения к БД с помощью `psycopg2`
* в папке [tests](tests) хранятся файлы с тестами
    * в папке [api](tests/api) хранятся тесты реализованные с помощью API-запросов
        * в [test_crud.py](tests/api/user/test_crud.py) реализован тест с операциями CRUD для user
        * в [test_limit_create.py](tests/api/user/test_limit_create.py)
          и [test_limit_update.py](tests/api/user/test_limit_update.py) для теста граничных значений были заданы
          произвольные границы
        * в [test_negative.py](tests/api/user/test_negative.py) должны располагаться негативные тесты для user, но они
          требуют более глубокого исследования системы, поэтому не были реализованы
    * в папке [db](tests/db) хранятся тесты реализованные с помощью SQL-запросов
        * в [test_crud.py](tests/db/test_crud.py) реализован тест с операциями CRUD для user
    * в файле [conftest.py](tests/conftest.py) реализованы фикстуры, которые используются в тестах
* в файле [setup.cfg](setup.cfg) хранятся маркеры для запуска конкретных тестов

## Запуск тестов

   ```
   pytest --alluredir results
   ```

## Формирование Allure-отчета

   ```
   allure serve results
   ```

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