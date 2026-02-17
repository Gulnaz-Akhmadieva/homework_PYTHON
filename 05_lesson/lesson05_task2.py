from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

# перейти на страницу
driver.get("http://uitestingplayground.com/dynamicid")
sleep(2)

# найти элемент "синяя кнопка" по локатору
blue_button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
blue_button.click()
print("Клик по синей кнопке выполнен")

sleep(5)
driver.quit()
