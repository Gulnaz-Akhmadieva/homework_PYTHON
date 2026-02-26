from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://uitestingplayground.com/textinput")
print("Перешли на страницу")

wait = WebDriverWait(driver, 10)  # Ждем максимум 10 секунд

# найти поле поиска
search = driver.find_element(By.CSS_SELECTOR, ".form-control")

# ввести слово SkyPro
search.send_keys("SkyPro")
print("Текст SkyPro введен")


# находим и кликаем синюю кнопку
blue_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
blue_button.click()
print("Клик по синей кнопке выполнен")


# получаем текст кнопки и выводим в консоль
text = blue_button.text
print(text)

driver.quit()
