import time

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from base.base_class import Base
from faker import Faker


class DeliveryAddressPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    faker_ = Faker("ru_RU")
    zipcode: int = faker_.postcode()
    city: str = faker_.city()
    street: str = faker_.street_name()
    house: str = faker_.building_number()
    apartment: int = faker_.building_number()

    ADDRESS_BOX: str = "//textarea[@data-testid='base-input:field']"
    CLIENT_INFO_FIELD: str = "//div[@data-testid='input']"
    CONFIRM_ADDRESS_BUTTON: str = "//button[@data-testid='button']"
    CONFIRM_WITH_MANAGER_BUTTON: str = "//div[@class='D5FCL_']"

    def get_address_box(self) -> WebElement:
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, self.ADDRESS_BOX)))

    def get_float_field(self, field_index) -> WebElement:
        float_field: WebElement = self.driver.find_elements(By.XPATH, self.CLIENT_INFO_FIELD)[field_index]
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(float_field))

    # Функция недоступна, тк генерируемых адресов не существует, сайт ищет и не может найти адреса
    def get_confirm_address_button(self) -> WebElement:
        confirm_address_button = self.driver.find_elements(By.XPATH, self.CLIENT_INFO_FIELD)[1]
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(confirm_address_button))

    def get_confirm_address_with_manager_button(self) -> WebElement:
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, self.CONFIRM_WITH_MANAGER_BUTTON)))

    def send_address_box(self) -> None:
        self.get_address_box().send_keys(f"{self.zipcode}, {self.city}, {self.street}, {self.house}")

    # Функция недоступна, тк генерируемых адресов не существует, сайт ищет и
    # не может найти дом, № квартиры и тд
    def send_client_info_fields(self):
        info = ["apartment", "doorphone", "entrance", "floor"]
        for index, i in enumerate(range(3, 7)):
            self.get_float_field(i).send_keys("1")
            time.sleep(2)

    def click_confirm_address_button(self) -> None:
        self.get_confirm_address_with_manager_button().click()
        print("Click Send address info")

    def select_address_box(self) -> None:
        self.get_current_url()
        time.sleep(1)
        self.send_address_box()
        time.sleep(3)

    def select_confirm_address_button(self) -> None:
        self.click_confirm_address_button()
        time.sleep(3)
