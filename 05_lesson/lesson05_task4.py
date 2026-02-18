from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

# открыть браузер Firefox
driver = webdriver.Firefox()
driver.maximize_window()

# Перейти на страницу
driver.get("http://the-internet.herokuapp.com/login")
sleep(3)

# найти поле username и ввести tomsmith
search = driver.find_element(By.ID, "username")
search.send_keys("tomsmith")
sleep(3)

# найти поле password и ввести SuperSecretPassword!
search = driver.find_element(By.ID, "password")
search.send_keys("SuperSecretPassword!")
sleep(3)

# найти и нажать кнопку Login
search_button = driver.find_element(By.CLASS_NAME, "fa-2x")
search_button.click()
sleep(3)

# найти зеленую плашку по Id и получить текст
element = driver.find_element(By.ID, "flash")
text = element.text
sleep(3)

print(text)

driver.quit()
