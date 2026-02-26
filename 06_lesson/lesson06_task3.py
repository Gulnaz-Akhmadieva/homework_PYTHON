from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

driver.get(" https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
print("Перешли на страницу")

# Ждем максимум 30 секунд
wait = WebDriverWait(driver, 30)

wait.until(
    EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Done!')]"))
)
print("Все картинки загружены (появилась надпись Done!)")

# Находим все картинки и берем третью (индекс 2)
images = driver.find_elements(By.TAG_NAME, "img")
third_image = images[2]
src_value = third_image.get_attribute("src")
print(f"src третьей картинки: {src_value}")


driver.quit()
