from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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


# ждем, пока кнопка появится И СРАЗУ КЛИКАЕМ
blue_button = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary"))
)
blue_button.click()
print("Клик по синей кнопке выполнен")


# получаем текст кнопки и выводим в консоль
text = blue_button.text
print(text)

driver.quit()
