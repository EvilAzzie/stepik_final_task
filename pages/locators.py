from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators ():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTER_EMAIL_LINK = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTER_PASSWORD_LINK = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTER_PASSWORD_LINK_2 = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_BUTTON = (By.CSS_SELECTOR, 'button[name="registration_submit"]')
    

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
    BASKET_LINK = (By.CSS_SELECTOR, 'div.basket-mini a')
    USER_ICON = (By.CSS_SELECTOR, 'div.account-collapse ul.navbar-nav a')

class BasketPageLocators():
    EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
    PRODUCTS_IN_BASKET = (By.CSS_SELECTOR, ".basket_summary")
