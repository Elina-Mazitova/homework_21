import json
import requests
import allure
from jsonschema import validate

BASE_URL = "https://fakestoreapi.com/products"
HEADERS = {"User-Agent": "Mozilla/5.0"}


def load_schema(path: str):
    with open(path) as file:
        return json.load(file)


@allure.title("Удаление продукта по ID")
@allure.story("Удаление продукта")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("api", "delete")
def test_delete_product():
    with allure.step("Отправляем DELETE запрос"):
        response = requests.delete(f"{BASE_URL}/1", headers=HEADERS)

    with allure.step("Проверяем статус-код 200"):
        assert response.status_code == 200


@allure.title("Удаление продукта с некорректным ID")
@allure.story("Удаление продукта")
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("api", "delete")
def test_delete_product_invalid_id():
    with allure.step("Отправляем DELETE запрос с некорректным ID"):
        response = requests.delete(f"{BASE_URL}/1-", headers=HEADERS)

    with allure.step("Проверяем статус-код 400"):
        assert response.status_code == 400


@allure.title("Получение продукта по ID")
@allure.story("Получение данных")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("api", "get")
def test_get_product_by_id():
    with allure.step("Отправляем GET запрос"):
        response = requests.get(f"{BASE_URL}/1")
        assert response.status_code == 200

    with allure.step("Проверяем тело ответа по JSON-схеме"):
        body = response.json()
        schema = load_schema("schemas/product_by_id.json")
        validate(instance=body, schema=schema)


@allure.title("Получение списка продуктов")
@allure.story("Получение данных")
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("api", "get")
def test_get_products():
    with allure.step("Отправляем GET запрос"):
        response = requests.get(BASE_URL)
        assert response.status_code == 200

    with allure.step("Проверяем тело ответа по JSON-схеме"):
        body = response.json()
        schema = load_schema("schemas/products_list.json")
        validate(instance=body, schema=schema)


@allure.title("Создание нового продукта")
@allure.story("Создание продукта")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("api", "post")
def test_post_product():
    payload = {
        "title": "New Product",
        "price": 29.99,
        "description": "Cat",
        "category": "Red",
        "image": "https:///example.com"
    }

    with allure.step("Отправляем POST запрос"):
        response = requests.post(BASE_URL, json=payload, headers=HEADERS)
        assert response.status_code == 201

    with allure.step("Проверяем тело ответа по JSON-схеме"):
        body = response.json()
        schema = load_schema("schemas/product_created_or_updated.json")
        validate(instance=body, schema=schema)


@allure.title("Обновление продукта по ID")
@allure.story("Обновление продукта")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("api", "put")
def test_put_product():
    payload = {
        "title": "Updated Product",
        "price": 11.99,
        "description": "Dog",
        "category": "Yellow",
        "image": "https:///examples.com"
    }

    with allure.step("Отправляем PUT запрос"):
        response = requests.put(f"{BASE_URL}/1", json=payload, headers=HEADERS)
        assert response.status_code == 200

    with allure.step("Проверяем тело ответа по JSON-схеме"):
        body = response.json()
        schema = load_schema("schemas/product_created_or_updated.json")
        validate(instance=body, schema=schema)


@allure.title("Обновление продукта с некорректным ID")
@allure.story("Обновление продукта")
@allure.severity(allure.severity_level.MINOR)
@allure.tag("api", "put")
def test_put_product_invalid_id():
    payload = {
        "title": "Updated Product",
        "price": 11.99,
        "description": "Dog",
        "category": "Yellow",
        "image": "https:///examples.com"
    }

    with allure.step("Отправляем PUT запрос с некорректным ID"):
        response = requests.put(f"{BASE_URL}/1-", json=payload, headers=HEADERS)
        assert response.status_code == 400

    with allure.step("Проверяем тело ответа по JSON-схеме"):
        body = response.json()
        schema = load_schema("schemas/product_updated_invalid.json")
        validate(instance=body, schema=schema)
