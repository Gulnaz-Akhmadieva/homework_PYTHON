from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form():
    driver = webdriver.Firefox()
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)


    try:

        # Примечание: сайт может требовать VPN для доступа из некоторых регионах

        driver.get("https://www.saucedemo.com/")
        print("Перешли на страницу")

        user_name = driver.find_element(By.ID, "user-name")
        user_name.send_keys("standard_user")

        password = driver.find_element(By.ID, "password")
        password.send_keys("secret_sauce")

        login_button = driver.find_element(By.ID, "login-button")
        login_button.click()

        wait.until(EC.visibility_of_element_located((By.ID, "inventory_container")))

        backpack_button = driver.find_element(By.CSS_SELECTOR, "[id$='backpack']")
        backpack_button.click()

        t_shirt_button = driver.find_element(By.CSS_SELECTOR, "[id$='t-shirt']")
        t_shirt_button.click()

        onesie_button = driver.find_element(By.CSS_SELECTOR, "[id$='onesie']")
        onesie_button.click()

        shopping_cart_button = driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link")
        shopping_cart_button.click()

        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".cart_list")))

        checkout_button = driver.find_element(By.ID, "checkout")
        checkout_button.click()

        wait.until(EC.visibility_of_element_located((By.ID, "checkout_info_container")))

        first_name = driver.find_element(By.ID, "first-name")
        first_name.send_keys("Гульназ")

        last_name = driver.find_element(By.ID, "last-name")
        last_name.send_keys("Ахмадиева")

        postal_code = driver.find_element(By.ID, "postal-code")
        postal_code.send_keys("452170")

        continue_button = driver.find_element(By.ID, "continue")
        continue_button.click()

        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".cart_list")))

        total_result = driver.find_element(By.CSS_SELECTOR, ".summary_total_label")
        text = total_result.text
        print(text)
        assert text == "Total: $58.29"
    finally:
        driver.quit()
