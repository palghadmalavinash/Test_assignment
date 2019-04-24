from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys

from src.locators.amazon_locators import amazon_locators as al

class amazon(object):

    def __init__(self,driver):
        self.browser= driver


    def enter_search_text(self,text):
        """
        Function to enter text in the search box
        :param text: Search text
        :return: None
        """
        locator = al.__dict__['amazon_main_page']['search']
        input_element = WebDriverWait(self.browser,30).until(
            ec.element_to_be_clickable(locator))

        input_element.clear()
        input_element.send_keys(text)
        input_element.send_keys(Keys.ENTER)

    def select_product(self,product):
        """
        Function to select product after search
        :param product: product to be selected
        :return: None
        """
        locator = al.__dict__['amazon_main_page']['product']
        print(type(self.browser))
        input_element = self.browser.find_element_by_xpath(locator[1])
        input_element.click()

        # switiching to New tab
        WebDriverWait(self.browser,30).until(ec.number_of_windows_to_be(2))
        tabs = self.browser.window_handles
        new_tab=tabs[1]
        self.browser.switch_to_window(new_tab)

    def perform_click(self,container,locator):
        """
        Function to perfrom click action on any locator of the page
        :param container: Dict from locator file
        :param locator: value from above dict
        :return: None
        """
        element = al.__dict__[container][locator]
        WebDriverWait(self.browser,30).until(ec.element_to_be_clickable(element))
        self.browser.find_element_by_css_selector(element[1]).click()


    def enter_text(self,container,locator,text):
        """
        Enter Text in any locator of the page
        :param container: Dict from locator file
        :param locator: value from above dict
        :return: None
        :param text: Text to be enterd in text area/box
        """
        element= al.__dict__[container][locator]
        input_element = WebDriverWait(self.browser, 30).until(
            ec.element_to_be_clickable(element))

        input_element.clear()
        input_element.send_keys(text)
        input_element.send_keys(Keys.ENTER)

    def get_element(self,container,locator):
        """
        Function to get any element on the page
        :param container: Dict from locator file
        :param locator: value from above dict
        :return: None
        """
        element = al.__dict__[container][locator]
        WebDriverWait(self.browser, 30).until(ec.element_to_be_clickable(element))
        elem = self.browser.find_element_by_css_selector(element[1])
        return elem

    def enter_address_field(self,container,locator,text):
        """
        Enter text in address fields. Difference between this and enter_text function
        is that Enter text function performs an ENTER action at the end
        :param container: Dict from locator file
        :param locator: value from above dict
        :param text: Text to be entered in text area/box
        :return: None
        """
        element= al.__dict__[container][locator]
        input_element = WebDriverWait(self.browser, 30).until(
            ec.element_to_be_clickable(element))

        input_element.clear()
        input_element.send_keys(text)
