import time
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from base.base_class import Base


class SubcategoryPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    SHOW_MORE_SUBCATEGORIES_BUTTON: str = "//a[@class='qg75pZ w6urhi svaRbR lv7xBL JaxV3g']"
    SUBCATEGORY_NAMES: str = "//a[@class='qg75pZ w6urhi JaxV3g']"

    def get_show_more_button(self) -> WebElement:
        show_more_button: WebElement = self.driver.find_elements(By.XPATH, self.SHOW_MORE_SUBCATEGORIES_BUTTON)[0]
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(show_more_button))

    def get_subcategory(self) -> WebElement:
        halloween_subcategory_index = 13
        subcategory_name = self.driver.find_elements(By.XPATH, self.SUBCATEGORY_NAMES)[halloween_subcategory_index]
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(subcategory_name))

    def click_show_more_button(self) -> None:
        self.get_show_more_button().click()

    def click_subcategory_name(self) -> None:
        self.get_subcategory().click()

    def select_show_more(self) -> None:
        self.get_current_url()
        self.click_show_more_button()

    def select_subcategory(self) -> None:
        self.click_subcategory_name()
