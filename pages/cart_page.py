from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from base.base_class import Base





class CartPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    CHECKOUT_BUTTON: str = "//button[@data-testid='checkout-button' and contains(., 'Перейти к оформлению')]"
    PRODUCT_NAME: str = "div.kGnH5f:nth-child(1) > div:nth-child(2) > div:nth-child(1) > h4:nth-child(1) > a:nth-child(1)"

    def get_checkout_button(self) -> WebElement:
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, self.CHECKOUT_BUTTON)))

    def get_cart_product_name(self) -> str:
        element = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.CSS_SELECTOR, self.PRODUCT_NAME))
        )
        # product_name = self.driver.find_element(By.CSS_SELECTOR, self.PRODUCT_NAME)
        product_name =element.text
        print(product_name)
        return product_name

    def click_checkout_button(self) -> None:
        self.get_checkout_button().click()

    def select_checkout_button(self) -> None:
        self.get_current_url()
        self.get_screenshot()
        self.click_checkout_button()

