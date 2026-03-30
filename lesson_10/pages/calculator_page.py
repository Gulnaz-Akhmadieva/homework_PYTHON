from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """Страница калькулятора с задержкой."""

    def __init__(self, driver: WebDriver) -> None:
        """Инициализирует страницу.
        Args:
            driver (WebDriver): Экземпляр драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 45)

    delay_input = (By.ID, "delay")
    button_7 = (By.XPATH, "//span[text()='7']")
    button_plus = (By.XPATH, "//span[text()='+']")
    button_8 = (By.XPATH, "//span[text()='8']")
    button_equals = (By.XPATH, "//span[text()='=']")
    screen = (By.CSS_SELECTOR, ".screen")

    def set_delay(self, value: str) -> None:
        """Устанавливает задержку.
        Args:
            value (str): Значение задержки в секундах.
        """
        delay_field = self.driver.find_element(*self.delay_input)
        delay_field.clear()
        delay_field.send_keys(value)

    def press_7(self) -> None:
        """Нажимает кнопку 7."""
        self.driver.find_element(*self.button_7).click()

    def press_plus(self) -> None:
        """Нажимает кнопку +."""
        self.driver.find_element(*self.button_plus).click()

    def press_8(self) -> None:
        """Нажимает кнопку 8."""
        self.driver.find_element(*self.button_8).click()

    def press_equals(self) -> None:
        """Нажимает кнопку =."""
        self.driver.find_element(*self.button_equals).click()

    def get_result(self) -> str:
        """Возвращает результат на экране.
        Returns:
            str: Текст результата.
        """
        return self.driver.find_element(*self.screen).text

    def wait_for_result(self, expected: str) -> None:
        """Ждёт появления ожидаемого результата.
        Args:
            expected (str): Ожидаемый текст результата.
        """
        self.wait.until(EC.text_to_be_present_in_element(self.screen, expected))
