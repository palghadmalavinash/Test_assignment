from selenium import webdriver
import pytest

@pytest.fixture
def driver():
    """
    return a webdriver instance for testing
    :return: webdriver instance
    """
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument("--disable-infobars")

    driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver", chrome_options=options)
    driver.set_window_position(0, 0)
    driver.set_window_size(1366, 768)
    driver.maximize_window()
    yield driver
    driver.quit()
    return driver