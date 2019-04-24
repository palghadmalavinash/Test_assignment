from selenium.webdriver.common.by import By


class amazon_locators(object):
    """
    File containing locators
    """

    amazon_main_page = {
        'search': (By.CSS_SELECTOR, '#twotabsearchtextbox'),
        'product':(By.XPATH,"(.//*[@class='a-link-normal'])[1]"),
    }

    amazon_product_page = {
        'add_to_cart': (By.CSS_SELECTOR, '#add-to-cart-button'),
        'cart_value': (By.CSS_SELECTOR, '#nav-cart-count'),
        'proceed_buy': (By.CSS_SELECTOR, '#hlb-ptc-btn-native'),
    }

    amazon_login_page= {
        'username': (By.CSS_SELECTOR, '#ap_email'),
        'password': (By.CSS_SELECTOR, '#ap_password'),
    }

    amazon_new_address = {
        'new_address': (By.CSS_SELECTOR, "a[href*='#new-address']"),
        'name': (By.XPATH, "(.//*[@id='enterAddressFullName'])[1]"),
        'mobile_number': (By.XPATH, "(.//*[@id='enterAddressPhoneNumber'])[1]"),
        'pincode': (By.XPATH, "(.//*[@id='enterAddressPostalCode'])[1]"),
        'address': (By.XPATH, "(.//*[@id='enterAddressAddressLine1'])[1]"),
        'area': (By.XPATH, "(.//*[@id='enterAddressAddressLine2'])[1]"),
        'landmark': (By.XPATH, "(.//*[@id='enterAddressLandmark'])[1]"),
        'town': (By.XPATH, "(.//*[@id='enterAddressCity'])[1]"),
        'state': (By.XPATH, "(.//*[@id='enterAddressStateOrRegion'])[1]"),
    }

    amazon_delivery_page={
        'product_name': (By.CSS_SELECTOR, '.a-spacing-base>div>strong')
    }