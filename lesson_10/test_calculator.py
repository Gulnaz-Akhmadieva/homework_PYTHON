import allure
import pytest
from selenium import webdriver
from pages.calculator_page import CalculatorPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Проверка суммы 7+8=15 с задержкой")
@allure.description("Тест проверяет, что калькулятор корректно складывает числа с задержкой 45 секунд")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.NORMAL)
def test_calculator(driver):
    with allure.step("Открыть страницу калькулятора"):
        calculator_page = CalculatorPage(driver)
        calculator_page.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    with allure.step("Установить задержку 45 секунд"):
            calculator_page.set_delay(45)

    with allure.step("Нажать кнопки 7 + 8 ="):
        calculator_page.press_7()
        calculator_page.press_plus()
        calculator_page.press_8()
        calculator_page.press_equals()

    with allure.step("Ожидать результат 15"):
        calculator_page.wait_for_result("15")

    with allure.step("Проверить, что результат равен 15"):
        assert calculator_page.get_result() == "15"
