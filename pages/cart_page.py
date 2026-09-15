import time

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from base.base_class import Base


class CartPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    CHECKOUT_BUTTON: str = "//button[@data-testid='checkout-button']"
    PRODUCT_NAME: str = "//a[@class='RSMgR3 wkpN3d ZwXSmF']"

    def get_checkout_button(self) -> WebElement:
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, self.CHECKOUT_BUTTON)))

    def get_cart_product_name(self) -> str:
        time.sleep(10)
        product_name = self.driver.find_element(By.XPATH, self.PRODUCT_NAME)
        result = product_name.text
        return result

    def click_checkout_button(self) -> None:
        self.get_checkout_button().click()

    def select_checkout_button(self) -> None:
        self.get_current_url()
        time.sleep(1)
        self.get_screenshot()
        self.click_checkout_button()
        time.sleep(3)
