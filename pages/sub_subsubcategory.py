import time
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from base.base_class import Base


class SubSubSubcategoryPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    SHOW_MORE_BUTTON: str = "//a[@class='WFe7Sg hzy0vv hUkBdJ']"
    PRODUCT_SUBJECT_CHECKBOX: str = "//input[@type='checkbox']"
    CHECKBOX = "/html/body/main/div/div[3]/div[1]/div[1]/div/div[1]/div[7]/div[2]/div/div[1]/label[1]/span[1]/input"
    WITCH_CARNIVAL_COSTUME: str = "//span[contains(text(), 'Карнавальный костюм «Зловещая Колдунья»: платье, шляпа, сумка, чулки, рост 110-116 см')]"

    def get_show_more_button(self) -> WebElement:
        show_more_button = self.driver.find_elements(By.XPATH, self.SHOW_MORE_BUTTON)[1]
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(show_more_button))

    def get_product_subject_checkbox(self) -> WebElement:
        return self.driver.find_element(By.XPATH, self.CHECKBOX)

    def get_witch_carnival_costume(self) -> WebElement:
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, self.WITCH_CARNIVAL_COSTUME)))

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
