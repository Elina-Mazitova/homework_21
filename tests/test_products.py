import json
import requests
from jsonschema import validate

BASE_URL = "https://fakestoreapi.com/products"
HEADERS = {"User-Agent": "Mozilla/5.0"}


def load_schema(path: str):
    with open(path) as file:
        return json.load(file)


def test_delete_product():
    response = requests.delete(f"{BASE_URL}/1", headers=HEADERS)
    assert response.status_code == 200


def test_delete_product_invalid_id():
    response = requests.delete(f"{BASE_URL}/1-", headers=HEADERS)
    assert response.status_code == 400


def test_get_product_by_id():
    response = requests.get(f"{BASE_URL}/1")
    assert response.status_code == 200

    body = response.json()
    schema = load_schema("schemas/product_by_id.json")
    validate(instance=body, schema=schema)


def test_get_products():
    response = requests.get(BASE_URL)
    assert response.status_code == 200

    body = response.json()
    schema = load_schema("schemas/products_list.json")
    validate(instance=body, schema=schema)


def test_post_product():
    payload = {
        "title": "New Product",
        "price": 29.99,
        "description": "Cat",
        "category": "Red",
        "image": "https:///example.com"
    }

    response = requests.post(BASE_URL, json=payload, headers=HEADERS)
    assert response.status_code == 201

    body = response.json()
    schema = load_schema("schemas/product_created_or_updated.json")
    validate(instance=body, schema=schema)


def test_put_product():
    payload = {
        "title": "Updated Product",
        "price": 11.99,
        "description": "Dog",
        "category": "Yellow",
        "image": "https:///examples.com"
    }

    response = requests.put(f"{BASE_URL}/1", json=payload, headers=HEADERS)
    assert response.status_code == 200

    body = response.json()
    schema = load_schema("schemas/product_created_or_updated.json")
    validate(instance=body, schema=schema)


def test_put_product_invalid_id():
    payload = {
        "title": "Updated Product",
        "price": 11.99,
        "description": "Dog",
        "category": "Yellow",
        "image": "https:///examples.com"
    }

    response = requests.put(f"{BASE_URL}/1-", json=payload, headers=HEADERS)
    assert response.status_code == 400

    body = response.json()
    schema = load_schema("schemas/product_updated_invalid.json")
    validate(instance=body, schema=schema)
