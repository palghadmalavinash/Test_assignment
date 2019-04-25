import pytest
from pytest_bdd import (
    given,
    scenarios,
    then,
    when,
    parsers
)

from src.pages.Amazon_UI import amazon

scenarios("../../feature/Amazon_UI/amazon.feature")


@pytest.fixture()
def amazon_page(driver):
    """
    Fixture to create object of src page
    :param driver: webdriver
    :return: page object
    """
    amazon_page = amazon.amazon(driver)
    return amazon_page


@pytest.fixture()
@given("navigates to amazon website")
def browser_instance(driver):
    """
    Navivgate to website
    :param driver: webdriver object
    :return: None
    """
    driver.get("https://www.amazon.in")


@given("search apple <product>")
def search_product(amazon_page,product):
    """
    Function to search product on site
    :param amazon_page: Page object
    :param product: Product to be searched
    :return: None
    """
    amazon_page.enter_search_text(product)


@when("open the <product> in new tab")
def select_product(amazon_page,product):
    """
    Function to select product on site
    :param amazon_page: Page object
    :param product: Product to be searched
    :return: None
    """
    amazon_page.select_product(product)


@when("add the product to cart")
def add_to_cart(amazon_page):
    """
    function to add product to cart
    :param amazon_page: page object
    :return: None
    """
    amazon_page.perform_click('amazon_product_page', 'add_to_cart')


@when("verify product is added to cart")
def get_cart_value(amazon_page):
    """
    Function to get cart value
    :param amazon_page: page object
    :return: None
    """
    cart_val = amazon_page.get_element('amazon_product_page', 'cart_value').text
    assert cart_val == '1'


@when("proceed to buy the product")
def buy_product(amazon_page):
    """
    Function to click on buy product button
    :param amazon_page: page object
    :return: None
    """
    amazon_page.perform_click('amazon_product_page', 'proceed_buy')


@when(parsers.cfparse("enter the credentails in the login page as '{username}' and '{password}'"))
def login_to_amazon(amazon_page,username,password):
    """
    Function to log in to website
    :param amazon_page: page object
    :param username: username passed from feature file
    :param password: password passed from feature file
    :return: None
    """
    amazon_page.enter_text('amazon_login_page', 'username', username)
    amazon_page.enter_text('amazon_login_page', 'password', password)


@when("enter the new shipping address")
def enter_new_address(amazon_page):
    """
    Function to enter new shipping address
    :param amazon_page: page object
    :return: None
    """
    amazon_page.perform_click('amazon_new_address','new_address')
    amazon_page.enter_address_field('amazon_new_address', 'name', 'AgroStar India')
    amazon_page.enter_address_field('amazon_new_address', 'mobile_number', '9975612466')
    amazon_page.enter_address_field('amazon_new_address', 'pincode', '411014')
    amazon_page.enter_address_field('amazon_new_address', 'address', 'E-Space IT Park, 101, S.No: 46/1, A1 Building, First Floor,')
    amazon_page.enter_address_field('amazon_new_address', 'area', 'Nagar Rd, Somnath Nagar, Wadgaon Sheri')
    amazon_page.enter_address_field('amazon_new_address', 'landmark', 'Test Landmark')
    amazon_page.enter_text('amazon_new_address', 'town', 'Pune')


@then("verify navigaton to the delivery options page")
def verify_page_element(amazon_page):
    """
    Function to Verify navigation to delivery page option
    :param amazon_page: page object
    :return: None
    """
    elem = amazon_page.get_element('amazon_delivery_page','product_name')
    assert "Apple" in elem.text