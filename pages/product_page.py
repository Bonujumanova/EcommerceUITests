import time
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from base.base_class import Base


class ProductPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ADD_TO_CART_BUTTON: str = "//button[@data-testid='cart-block:add-to-cart-button']"
    COSTUME_SIZE_PARAMETER: str = "//span[@class='AcHHZC']"
    GO_TO_CART_BUTTON: str = "//div[@class='VAowBn']"
    PRODUCT_NAME: str = "//h1[@data-testid='product-name']"

    def get_add_to_cart_button(self) -> WebElement:
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, self.ADD_TO_CART_BUTTON)))

    def get_costume_size_parameter(self) -> WebElement:
        selected_costume_size_index: int = 0
        costume_size_parameter = self.driver.find_elements(By.XPATH, self.COSTUME_SIZE_PARAMETER)[
            selected_costume_size_index]
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(costume_size_parameter))

    def get_go_to_cart_button(self) -> WebElement:
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, self.GO_TO_CART_BUTTON)))

    def get_product_name(self) -> str:
        product_name = self.driver.find_element(By.XPATH, self.PRODUCT_NAME).text
        return product_name

    def click_add_to_cart_button(self) -> None:
        self.get_add_to_cart_button().click()

    def click_costume_size_parameter(self) -> None:
        self.get_costume_size_parameter().click()

    def click_go_to_cart_button(self) -> None:
        self.get_go_to_cart_button().click()
        print("Click CART button")

    def select_costume_size_parameter(self) -> None:
        self.get_current_url()
        self.click_costume_size_parameter()

    def select_add_to_cart(self) -> None:
        self.click_add_to_cart_button()

    def select_go_to_cart_button(self) -> None:
        self.click_go_to_cart_button()
