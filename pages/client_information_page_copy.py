import time
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from base.base_class import Base
from faker import Faker



class ClientInformationPageCopy(Base):

    def __init__(self, driver):
        super().__init__(driver)

        self.driver = driver

    faker_ = Faker("ru_RU")

    DELIVERY_BY_COURIER_BUTTON: str = "//div[@data-testid='option-block_delivery-1']"
    # Группа одинаковых локаторов с разными индексами отвечают за ФИО, номер телефона, электронный адрес
    CLIENT_INFO_FIELD: str = "//input[@data-testid='base-input:field']"
    CLIENT_FULL_NAME: str = "//input[@id='contact_name']"
    # Список содержит сгенерированные ФИО, телефон и эл.почту клиента
    client_info_list: list[str,] = [faker_.name(), faker_.phone_number(), faker_.email()]
    client_name = client_info_list[0]

    def get_delivery_by_courier_button(self) -> WebElement:
        delivery_cy_courier_btn = self.driver.find_element(By.XPATH, self.DELIVERY_BY_COURIER_BUTTON)
        return delivery_cy_courier_btn

    def get_client_info(self, field_index: int) -> WebElement:
        field_element = self.driver.find_elements(By.XPATH, self.CLIENT_INFO_FIELD)[field_index]
        return field_element

    def click_delivery_by_courier_button(self) -> None:
        self.get_delivery_by_courier_button().click()

    # WebdriverWait to_be_clickable - не работает на этой странице, ошибка 'selenium.common.exceptions.TimeoutException'
    # upd. 1. пришлось использовать явное ожидание implicitly_wait(10).
    # upd. 2 Но!!! ПОЛЯ не заполняются, ошибок нет. Приходится использовать time.sleep(10)
    def send_client_info_fields(self) -> None:
        info_text: list[str,] = ["ФИО", "телефон", "электронная почта"]
        # index - поля ФИО, телефон, эмейл - имеют подобные локаторы, чтобы найти необходимое поле, необходим
        # индекс нужного поля '0' - ФИО, '1' - телефон, '2' - емейл
        for index in range(3):
            text = self.client_info_list[index]
            # self.driver.implicitly_wait(10)
            time.sleep(10)
            self.get_client_info(index).send_keys(text)
            print(f"Send '{info_text[index]}: {text}' INFO")

    def select_delivery_by_courier_button(self) -> None:
        self.get_current_url()
        time.sleep(1)
        self.click_delivery_by_courier_button()
        time.sleep(3)

    def select_client_info_fields(self) -> None:
        # Заполняем поля ФИО, телефон, email
        self.send_client_info_fields()
        time.sleep(3)
        self.get_current_url()
        time.sleep(3)
