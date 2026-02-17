from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

# открыть браузер Firefox
driver = webdriver.Firefox()
driver.maximize_window()

# переход по ссылке
driver.get(" http://the-internet.herokuapp.com/inputs")
sleep(3)


# найти поле поиска
search = driver.find_element(By.TAG_NAME, "input")

# ввести слово Sky
search.send_keys("Sky")
sleep(2)


# очистить поле
search.clear()
sleep(2)

# ввести слово Pro
search.send_keys("Pro")
sleep(4)


driver.quit()
