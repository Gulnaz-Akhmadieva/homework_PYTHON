from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShopPage:
    """Страница интернет-магазина."""

    def __init__(self, driver) -> None:
        """Инициализирует страницу."""
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    username_input = (By.ID, "user-name")
    password_input = (By.ID, "password")
    login_button = (By.ID, "login-button")
    inventory_container = (By.ID, "inventory_container")

    backpack_button = (By.CSS_SELECTOR, "[id$='backpack']")
    tshirt_button = (By.CSS_SELECTOR, "[id$='t-shirt']")
    onesie_button = (By.CSS_SELECTOR, "[id$='onesie']")
    cart_link = (By.CSS_SELECTOR, ".shopping_cart_link")
    cart_list = (By.CSS_SELECTOR, ".cart_list")

    checkout_button = (By.ID, "checkout")
    checkout_info = (By.ID, "checkout_info_container")

    firstname_input = (By.ID, "first-name")
    lastname_input = (By.ID, "last-name")
    postal_input = (By.ID, "postal-code")
    continue_button = (By.ID, "continue")

    total_label = (By.CSS_SELECTOR, ".summary_total_label")

    def open(self) -> None:
        """Открывает страницу магазина."""
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username: str, password: str) -> None:
        """Авторизуется с указанными логином и паролем."""
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()
        self.wait.until(EC.visibility_of_element_located(self.inventory_container))

    def add_backpack(self) -> None:
        """Добавляет рюкзак в корзину."""
        self.driver.find_element(*self.backpack_button).click()

    def add_tshirt(self) -> None:
        """Добавляет футболку в корзину."""
        self.driver.find_element(*self.tshirt_button).click()

    def add_onesie(self) -> None:
        """Добавляет комбинезон в корзину."""
        self.driver.find_element(*self.onesie_button).click()

    def go_to_cart(self) -> None:
        """Переходит в корзину."""
        self.driver.find_element(*self.cart_link).click()
        self.wait.until(EC.visibility_of_element_located(self.cart_list))

    def checkout(self) -> None:
        """Нажимает кнопку оформления заказа."""
        self.driver.find_element(*self.checkout_button).click()
        self.wait.until(EC.visibility_of_element_located(self.checkout_info))

    def fill_checkout_info(self, first: str, last: str, zipcode: str) -> None:
        """Заполняет форму оформления заказа."""
        self.driver.find_element(*self.firstname_input).send_keys(first)
        self.driver.find_element(*self.lastname_input).send_keys(last)
        self.driver.find_element(*self.postal_input).send_keys(zipcode)

    def continue_checkout(self) -> None:
        """Нажимает кнопку Continue."""
        self.driver.find_element(*self.continue_button).click()
        self.wait.until(EC.visibility_of_element_located(self.cart_list))

    def get_total_text(self) -> str:
        """Возвращает итоговую сумму заказа."""
        return self.driver.find_element(*self.total_label).text
