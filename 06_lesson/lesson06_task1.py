from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://uitestingplayground.com/ajax")
print("Перешли на страницу")

wait = WebDriverWait(driver, 30)  # Ждем максимум 30 секунд

blue_button = wait.until(
    EC.element_to_be_clickable((By.ID, "ajaxButton"))
)
print("Нашли синюю кнопку")

blue_button.click()
print("Нажали на синюю кнопку")

green_badge = wait.until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ".bg-success"))
)
print("Зеленая плашка появилась")

text = green_badge.text
print(text)

driver.quit()
