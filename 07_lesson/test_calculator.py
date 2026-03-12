import pytest
from selenium import webdriver
from pages.calculator_page import CalculatorPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_calculator(driver):
    calculator_page = CalculatorPage(driver)
    calculator_page.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    calculator_page.set_delay(45)
    calculator_page.press_7()
    calculator_page.press_plus()
    calculator_page.press_8()
    calculator_page.press_equals()

    calculator_page.wait_for_result("15")
    assert calculator_page.get_result() == "15"
