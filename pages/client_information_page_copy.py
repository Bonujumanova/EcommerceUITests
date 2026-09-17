from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from base.base_class import Base
from faker import Faker


class ClientInformationPageCopy(Base):

    def __init__(self, driver):
        super().__init__(driver)
        faker_ = Faker("ru_RU")

        self.driver = driver
        # Список содержит сгенерированные ФИО, телефон и эл.почту клиента
        self.client_info_list: list[str,] = \
            [
                faker_.name(),
                faker_.phone_number(),
                faker_.email()
            ]

    CUSTOMER_TYPE_TOGGLE: str = "//li[@data-testid='tab' and text()='Физлицо']"
    DELIVERY_BY_COURIER_BUTTON: str = "//div[@data-testid='option-block_delivery-1']"
    # Группа одинаковых локаторов с разными индексами отвечают за ФИО, номер телефона, электронный адрес
    CLIENT_INFO_FIELD: str = "//input[@data-testid='base-input:field']"

    def get_delivery_by_courier_button(self) -> WebElement:
        delivery_cy_courier_btn = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.XPATH, self.DELIVERY_BY_COURIER_BUTTON))
        )
        return delivery_cy_courier_btn

    def get_customer_type_toggle(self) -> WebElement:
        # Ожидает, пока не закроется перекрывающий баннер
        WebDriverWait(self.driver, timeout=15).until(
            ec.invisibility_of_element_located(
                (By.CSS_SELECTOR, ".lEOw_o")
            )
        )
        customer_type_toggle = WebDriverWait(self.driver, timeout=20).until(
            ec.element_to_be_clickable((By.XPATH, self.CUSTOMER_TYPE_TOGGLE))
        )
        return customer_type_toggle

    # Находит локатор ФИО. Локаторы для ФИО, телефона, эмейл - идентичны, имеют разный индекс
    def get_client_info(self) -> list[WebElement,]:
        field_elements = WebDriverWait(self.driver, timeout=10).until(
            ec.presence_of_all_elements_located((By.XPATH, self.CLIENT_INFO_FIELD))
        )
        return field_elements

    def click_delivery_by_courier_button(self) -> None:
        # Ожидает, пока не закроется перекрывающий баннер
        WebDriverWait(self.driver, timeout=15).until(
            ec.invisibility_of_element_located(
                (By.CSS_SELECTOR, ".lEOw_o")
            )
        )

        element = self.get_delivery_by_courier_button()
        element.click()

    def click_customer_type_toggle(self) -> None:
        toggle = self.get_customer_type_toggle()
        toggle.click()

    def send_client_info_fields(self) -> None:
        # index - поля ФИО, телефон, эмейл - имеют подобные локаторы, чтобы найти необходимое поле, необходим
        # индекс нужного поля '0' - ФИО, '1' - телефон, '2' - емейл
        field_elements = self.get_client_info()

        for index in range(3):
            text_for_field = self.client_info_list[index]
            field_elements[index].send_keys(text_for_field)


    def select_customer_type_toggle(self) -> None:
        self.click_customer_type_toggle()

    def select_client_info_fields(self) -> None:
        # Заполняем поля ФИО, телефон, email
        self.send_client_info_fields()


    def select_delivery_by_courier_button(self) -> None:
        self.click_delivery_by_courier_button()
