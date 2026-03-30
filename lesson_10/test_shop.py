import allure
import pytest
from selenium import webdriver
from pages.shop_page import ShopPage


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Проверка оформления заказа в интернет-магазине")
@allure.description("Тест проверяет, что сумма заказа корректно рассчитывается")
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop(driver):
    with allure.step("Открыть страницу магазина и авторизоваться"):
        shop_page = ShopPage(driver)
        shop_page.open()
        shop_page.login("standard_user", "secret_sauce")

    with allure.step("Добавить товары в корзину"):
        shop_page.add_backpack()
        shop_page.add_tshirt()
        shop_page.add_onesie()

    with allure.step("Перейти в корзину"):
        shop_page.go_to_cart()

    with allure.step("Оформить заказ"):
        shop_page.checkout()
        shop_page.fill_checkout_info("Гульназ", "Ахмадиева", "452170")
        shop_page.continue_checkout()

    with allure.step("Проверить итоговую сумму"):
        total = shop_page.get_total_text()
        assert total == "Total: $58.29"
