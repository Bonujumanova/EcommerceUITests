from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from base.base_class import Base


class SubSubSubcategoryPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Вид товара(кнопка "еще ..."
    SHOW_MORE_BUTTON: str = \
        "div.Ywl6gJ:nth-child(9) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > a:nth-child(1)"
    # Вид товара - "Костюм"
    PRODUCT_SUBJECT_CHECKBOX: str = "//input[@type='checkbox']"
    CHECKBOX = ".cBROg0 > label:nth-child(1) > span:nth-child(2) > a:nth-child(1)"
    PUMPKIN_COSTUME: str = "//span[contains(text(), 'Карнавальный костюм «Осенняя тыква», фетр')]"

    def get_show_more_button(self) -> WebElement:
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.CSS_SELECTOR, SubSubSubcategoryPage.SHOW_MORE_BUTTON)))

    def get_product_subject_checkbox(self) -> WebElement:
        return self.driver.find_element(By.CSS_SELECTOR, self.CHECKBOX)

    def get_witch_carnival_costume(self) -> WebElement:
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, self.PUMPKIN_COSTUME)))

    def click_show_more_button(self) -> None:
        self.get_show_more_button().click()

    def click_product_subject_checkbox(self) -> None:
        self.get_product_subject_checkbox().click()

    def click_witch_carnival_costume(self) -> None:
        self.get_witch_carnival_costume().click()

    def select_show_more_button(self) -> None:
        self.get_current_url()
        self.click_show_more_button()

    def select_checkbox_button(self) -> None:
        self.click_product_subject_checkbox()

    def select_witch_carnival_costume(self) -> None:
        self.click_witch_carnival_costume()
