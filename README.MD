# Автотесты для приложения [SwaggerPetStore](https://petstore.swagger.io/)

Автотесты написаны для локально развернутого сервиса SwaggerPetStore в Docker-контейнере, так как версия на
сайте [https://petstore.swagger.io](https://petstore.swagger.io) имеет урезанный функционал. Там нельзя нормально
создать, удалить, обновить user-а. Так же вместо `venv` использован `poetry`.

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