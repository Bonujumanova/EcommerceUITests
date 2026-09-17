from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from base.base_class import Base


class MainPage(Base):
    url = "https://www.sima-land.ru/"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    CATALOG_BAR: str = "//button[@data-testid='main-bar:catalog-opener']"
    YES_BUTTON_IN_LOCATION_NOTIFICATION: str = "//button[@data-testid='button' and contains (., 'Да, верно')]"
    PRODUCT_CATEGORIES: str = "//a[@data-testid='catalog-menu:root-category-link']"

    COOKIE_ACCEPT_BANNER = ".iPD9Xn"

    def get_main_catalog_bar(self) -> WebElement:
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, self.CATALOG_BAR)))

    def get_yes_location_button(self) -> WebElement:
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, self.YES_BUTTON_IN_LOCATION_NOTIFICATION)))

    def get_product_category(self) -> WebElement:
        # Индекс категории ПРАЗДНИКИ = 20
        events_index: int = 20
        product_category: WebElement = self.driver.find_elements(By.XPATH, self.PRODUCT_CATEGORIES)[events_index]
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(product_category))

    def click_main_catalog_bar(self) -> None:
        self.get_main_catalog_bar().click()

    def click_yes_location_button(self) -> None:
        self.get_yes_location_button().click()

    def click_product_category(self) -> None:
        self.get_product_category().click()

    def click_cookie_button(self):
        cookie_button = WebDriverWait(self.driver, 5).until(
            ec.element_to_be_clickable(
                (By.CSS_SELECTOR, MainPage.COOKIE_ACCEPT_BANNER))
        )
        cookie_button.click()

    def select_main_catalog_bar(self) -> None:
        self.driver.get(self.url)
        self.get_current_url()

        self.click_yes_location_button()

        self.click_main_catalog_bar()

        self.click_cookie_button()

        self.click_product_category()
