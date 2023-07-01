## Развертывание сервиса

1. Клонировать репозиторий с GitHub:

   ```
   git clone https://github.com/bodary2905/petstore_testing
   ```

2. Установить библиотеки с помощью **poetry**:

   ```
   poetry install
   ```

3. Запустить сервис SwaggerPetstore в Docker-контейнере, выполнив команду:
    ```
   docker-compose up
   ```
4. После окончания работы выполнить:
    ```
   docker-compose down
   ```