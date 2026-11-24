# Postman Collection — JSONPlaceholder API Tests

Коллекция для тестирования REST API [JSONPlaceholder](https://jsonplaceholder.typicode.com/).

## Что внутри

6 запросов с автотестами на вкладке Scripts → Post-response:

| # | Метод | Endpoint | Что проверяет |
|---|-------|----------|---------------|
| 1 | GET | `/posts/1` | Статус 200, наличие поля `userId`, время ответа < 1000 мс |
| 2 | GET | `/posts` | Статус 200, ответ — массив из 100 постов |
| 3 | POST | `/posts` | Статус 201, наличие `id`, совпадение `title` |
| 4 | PUT | `/posts/1` | Статус 200, обновление `title` |
| 5 | DELETE | `/posts/1` | Статус 200 |
| 6 | GET | `/posts/101` | Негативный тест: статус 404, пустой объект в ответе |

Навыки

- REST API, HTTP-методы (GET, POST, PUT, DELETE)
- Статус-коды (200, 201, 404)
- JSON, проверка структуры ответа
- Написание автотестов на JavaScript в Postman
- Негативное тестирование
