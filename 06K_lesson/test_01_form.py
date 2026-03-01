from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait




def test_form():
    service = Service("/Users/gulnazahmadieva/webdrivers/msedgedriver")
    driver = webdriver.Edge(service=service)
    driver.maximize_window()

    wait = WebDriverWait(driver, 30)

    try:
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        print("Страница открыта")
        wait.until(EC.presence_of_element_located((By.NAME, "first-name")))

        first_name = driver.find_element(By.NAME, "first-name")
        first_name.send_keys("Иван")

        last_name = driver.find_element(By.NAME, "last-name")
        last_name.send_keys("Петров")

        address_input = driver.find_element(By.NAME, "address")
        address_input.send_keys("Ленина, 55-3")

        email_input = driver.find_element(By.NAME, "e-mail")
        email_input.send_keys("test@skypro.com")

        phone_number = driver.find_element(By.NAME, "phone")
        phone_number.send_keys("+7985899998787")

        zip_code = driver.find_element(By.NAME, "zip-code")
        zip_code.clear()

        city_input = driver.find_element(By.NAME, "city")
        city_input.send_keys("Москва")

        country_input = driver.find_element(By.NAME, "country")
        country_input.send_keys("Россия")

        job_position = driver.find_element(By.NAME, "job-position")
        job_position.send_keys("QA")

        company_input = driver.find_element(By.NAME, "company")
        company_input.send_keys("SkyPro")

        submit_button = driver.find_element(By.CSS_SELECTOR, "[type='submit']")
        submit_button.click()

        wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "[type='submit']")))

        first_name_check = driver.find_element(By.ID, "first-name")
        first_name_class = first_name_check.get_attribute("class")
        assert "alert-success" in first_name_class

        last_name_check = driver.find_element(By.ID, "last-name")
        last_name_class = last_name_check.get_attribute("class")
        assert "alert-success" in last_name_class

        address_check = driver.find_element(By.ID, "address")
        address_class = address_check.get_attribute("class")
        assert "alert-success" in address_class

        email_check = driver.find_element(By.ID, "e-mail")
        email_class = email_check.get_attribute("class")
        assert "alert-success" in email_class

        phone_number_check = driver.find_element(By.ID, "phone")
        phone_number_class = phone_number_check.get_attribute("class")
        assert "alert-success" in phone_number_class

        zip_code_check = driver.find_element(By.ID, "zip-code")
        zip_code_class = zip_code_check.get_attribute("class")
        assert "alert-danger" in zip_code_class

        city_check = driver.find_element(By.ID, "city")
        city_class = city_check.get_attribute("class")
        assert "alert-success" in city_class

        country_check = driver.find_element(By.ID, "country")
        country_class = country_check.get_attribute("class")
        assert "alert-success" in country_class

        job_position_check = driver.find_element(By.ID, "job-position")
        job_position_class = job_position_check.get_attribute("class")
        assert "alert-success" in job_position_class

        company_check = driver.find_element(By.ID, "company")
        company_class = company_check.get_attribute("class")
        assert "alert-success" in company_class
    finally:
        # driver.quit()
        print("Браузер закрыт")
