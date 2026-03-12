import pytest
from selenium import webdriver
from pages.shop_page import ShopPage


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_shop(driver):
    shop_page = ShopPage(driver)
    shop_page.open()

    shop_page.login("standard_user", "secret_sauce")

    shop_page.add_backpack()
    shop_page.add_tshirt()
    shop_page.add_onesie()

    shop_page.go_to_cart()
    shop_page.checkout()

    shop_page.fill_checkout_info("Гульназ", "Ахмадиева", "452170")
    shop_page.continue_checkout()

    total = shop_page.get_total_text()
    assert total == "Total: $58.29"