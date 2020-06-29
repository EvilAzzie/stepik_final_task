from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators ():
    LOGIN_FORM = (By.CSS_SELECTOR, '[id="login_form"]')
    REGISTER_FORM = (By.CSS_SELECTOR, '[id="register_form"]')

class ProductPageLocators ():
    BASKET_BUTTON = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    PRICE_PRODUCT = (By.CSS_SELECTOR, 'div.product_main .price_color')
    PRICE_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, 'div.alert-info .alertinner strong')
    NAME_PRODUCT = (By.CSS_SELECTOR, 'div.product_main h1')
    NAME_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, '.alert-success:nth-child(1) strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success:nth-child(1) .alertinner')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
