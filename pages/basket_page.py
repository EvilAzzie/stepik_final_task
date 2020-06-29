from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    
    def should_be_no_products(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_IN_BASKET), \
        "Products inside basket is presented, but should not be"

    def should_be_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_MESSAGE), \
        "Basket should be empty, but it isn't"
