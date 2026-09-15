import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from base.base_class import Base


class SubSubcategoryPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    SUB_SUBCATEGORY_THEME: str = "//span[@class='Xj5pxy']"

    def get_sub_subcategory_theme(self):
        carnival_costumes_index: int = 6
        sub_subcategory_theme = self.driver.find_elements(By.XPATH, self.SUB_SUBCATEGORY_THEME)[carnival_costumes_index]
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(sub_subcategory_theme))

    def click_sub_subcategory_theme(self):
        self.get_sub_subcategory_theme().click()

    def select_show_more(self):
        self.get_current_url()
        self.click_sub_subcategory_theme()
