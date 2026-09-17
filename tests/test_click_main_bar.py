from selenium import webdriver
from pages.cart_page import CartPage
from pages.client_information_page_copy import ClientInformationPageCopy
from pages.delivery_address_info import DeliveryAddressPage
from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.sub_subcategory import SubSubcategoryPage
from pages.sub_subsubcategory import SubSubSubcategoryPage
from pages.subcategory_page import SubcategoryPage


def test_click_main_bar(setup_test, set_group_test):
    driver = webdriver.Firefox()
    driver.maximize_window()

    main_page = MainPage(driver)
    main_page.select_main_catalog_bar()

    subcategory_page = SubcategoryPage(driver)
    # subcategory_page.select_show_more()
    subcategory_page.select_subcategory()

    sub_subcategory_page = SubSubcategoryPage(driver)
    sub_subcategory_page.select_show_more()

    sub_sub_subcategory_page = SubSubSubcategoryPage(driver)
    sub_sub_subcategory_page.select_show_more_button()
    sub_sub_subcategory_page.select_checkbox_button()
    sub_sub_subcategory_page.select_witch_carnival_costume()

    product_page = ProductPage(driver)
    product_page.select_add_to_cart()
    product_name = product_page.get_product_name()
    product_page.select_go_to_cart_button()

    cart_page = CartPage(driver)
    cart_product_name = cart_page.get_cart_product_name()
    try:
        assert product_name == cart_product_name
    except AssertionError as e:
        driver.quit()
    cart_page.select_checkout_button()

    client_info_page = ClientInformationPageCopy(driver)
    client_info_page.select_customer_type_toggle()
    client_info_page.select_client_info_fields()

    client_info_page.select_delivery_by_courier_button()

    delivery_address_info_page = DeliveryAddressPage(driver)
    delivery_address_info_page.select_address_box()
    delivery_address_info_page.select_confirm_address_button()

    client_info_page.get_screenshot()

