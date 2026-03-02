from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        print("Перешли на страницу")

        delay_element = driver.find_element(By.ID, "delay")
        delay_element.clear()
        delay_element.send_keys("45")

        button_7 = driver.find_element(By.XPATH, "//span[text()='7']")
        button_7.click()

        button_plus = driver.find_element(By.XPATH, "//span[text()='+']")
        button_plus.click()

        button_8 = driver.find_element(By.XPATH, "//span[text()='8']")
        button_8.click()

        button_equals = driver.find_element(By.XPATH, "//span[text()='=']")
        button_equals.click()

        WebDriverWait(driver, 45).until(lambda d: d.find_element(By.CSS_SELECTOR, ".screen").text == "15")

        result_text = driver.find_element(By.CSS_SELECTOR, ".screen").text
        assert result_text == "15"

    finally:
        driver.quit()
