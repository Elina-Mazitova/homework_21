import requests
import allure


BASE_URL = "https://restcountries.com/v3.1/capital"


@allure.title("Получение страны по столице — Париж")
@allure.story("RestCountries: Capital")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_country_by_capital_paris():
    response = requests.get(f"{BASE_URL}/Paris")
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)
    assert data[0]["capital"][0] == "Paris"
    assert data[0]["name"]["common"] == "France"


@allure.title("Получение страны по столице — Токио")
@allure.story("RestCountries: Capital")
@allure.severity(allure.severity_level.NORMAL)
def test_get_country_by_capital_tokyo():
    response = requests.get(f"{BASE_URL}/Tokyo")
    assert response.status_code == 200

    data = response.json()
    assert data[0]["capital"][0] == "Tokyo"
    assert data[0]["name"]["common"] == "Japan"


@allure.title("Запрос несуществующей столицы")
@allure.story("RestCountries: Capital")
@allure.severity(allure.severity_level.MINOR)
def test_get_country_by_invalid_capital():
    response = requests.get(f"{BASE_URL}/ElinaCity")
    assert response.status_code == 404
