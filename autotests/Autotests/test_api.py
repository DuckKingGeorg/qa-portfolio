import requests

# Базовый URL для тестирования
BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_post_by_id():
    """Тест: получение поста по ID (статус 200 и наличие поля userId)"""
    response = requests.get(f"{BASE_URL}/posts/1")
    
    assert response.status_code == 200
    json_data = response.json()
    assert "userId" in json_data
    assert "title" in json_data

def test_get_all_posts():
    """Тест: получение всех постов (статус 200 и длина списка 100)"""
    response = requests.get(f"{BASE_URL}/posts")
    
    assert response.status_code == 200
    json_data = response.json()
    assert isinstance(json_data, list)
    assert len(json_data) == 100

def test_create_post():
    """Тест: создание нового поста (статус 201 и совпадение title)"""
    new_post = {
        "title": "My python test",
        "body": "This is a test",
        "userId": 1
    }
    response = requests.post(f"{BASE_URL}/posts", json=new_post)
    
    assert response.status_code == 201
    json_data = response.json()
    assert json_data["title"] == "My python test"
    assert "id" in json_data

def test_get_non_existent_post():
    """Тест: запрос несуществующего поста (негативный тест, статус 404)"""
    response = requests.get(f"{BASE_URL}/posts/101")
    
    assert response.status_code == 404
    
