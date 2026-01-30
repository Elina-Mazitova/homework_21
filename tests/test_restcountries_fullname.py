import requests
import allure
import pytest


BASE_URL = "https://restcountries.com/v3.1/name"


@allure.title("Поиск страны по официальному полному имени — Republic of Finland")
@allure.story("RestCountries: Full name lookup")
def test_get_country_by_full_official_name_finland():
    with allure.step("Отправляем GET запрос для 'Republic of Finland'"):
        response = requests.get(f"{BASE_URL}/Republic%20of%20Finland?fullText=true")
        assert response.status_code == 200

    with allure.step("Проверяем корректность ответа"):
        data = response.json()
        assert data[0]["name"]["common"] == "Finland"
        assert data[0]["name"]["official"] == "Republic of Finland"


@allure.title("Поиск страны по полному имени — United States of America")
@allure.story("RestCountries: Full name lookup")
def test_get_country_by_full_name_usa():
    with allure.step("Отправляем GET запрос для 'United States of America'"):
        response = requests.get(f"{BASE_URL}/United%20States%20of%20America?fullText=true")
        assert response.status_code == 200

    with allure.step("Проверяем корректность ответа"):
        data = response.json()
        assert data[0]["name"]["common"] == "United States"
        assert data[0]["name"]["official"] == "United States of America"


@allure.title("Поиск страны по полному имени — несуществующая страна")
@allure.story("RestCountries: Full name lookup")
def test_get_country_by_full_name_invalid():
    with allure.step("Отправляем GET запрос для несуществующего имени"):
        response = requests.get(f"{BASE_URL}/ElinaLand?fullText=true")

    with allure.step("Проверяем, что API возвращает 404"):
        assert response.status_code == 404
