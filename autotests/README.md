# Автотесты API на Python

Простые автотесты для проверки REST API [JSONPlaceholder](https://jsonplaceholder.typicode.com/) с использованием `pytest` и `requests`.

## Что проверяют тесты

1. `test_get_post_by_id` — GET-запрос поста, проверка статуса 200 и наличия поля `userId`.
2. `test_get_all_posts` — GET-запрос всех постов, проверка статуса 200 и длины массива (100 элементов).
3. `test_create_post` — POST-запрос создания поста, проверка статуса 201 и возвращаемого заголовка.
4. `test_get_non_existent_post` — негативный тест, проверка статуса 404 для несуществующего ID.

## Как запустить

1. Установи Python (версия 3.8+).
2. Установи зависимости:
   ```bash
   pip install pytest requests'
   
