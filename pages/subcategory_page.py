from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from base.base_class import Base


class SubcategoryPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Halloween sub-category
    SUBCATEGORY_NAME: str = "//a[@data-testid='subcategory-link' and contains(., 'Хэллоуин')]"

    def get_subcategory(self) -> WebElement:

        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, SubcategoryPage.SUBCATEGORY_NAME))
        )

    def click_subcategory_name(self) -> None:
        self.get_subcategory().click()


    def select_subcategory(self) -> None:
        self.click_subcategory_name()
