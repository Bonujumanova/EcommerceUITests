from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from base.base_class import Base


class SubSubcategoryPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    # Карнавальные костюмы
    SUB_SUBCATEGORY_THEME: str = \
        "//a[@data-testid='subcategory-link' and contains(., 'Карнавальные костюмы')]"

    def get_sub_subcategory_theme(self):

        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, SubSubcategoryPage.SUB_SUBCATEGORY_THEME))
        )

    def click_sub_subcategory_theme(self):
        self.get_sub_subcategory_theme().click()

    def select_show_more(self):
        self.get_current_url()
        self.click_sub_subcategory_theme()
