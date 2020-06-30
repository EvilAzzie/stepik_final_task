import pytest
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import time

"""
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
"""
#@pytest.mark.skip
@pytest.mark.login
class TestLoginFromProductPage():
    
    @pytest.fixture(scope="function", autouse=True)
    def setup(self,browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        self.page = ProductPage(browser,link)
        self.page.open()
         
    def test_guest_should_see_login_link_on_product_page(self,browser):
        self.page.should_be_login_link()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self,browser):
        self.page.go_to_login_page()


class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self,browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        self.page = LoginPage(browser,link)
        self.page.open()
        self.page.go_to_login_page()
        email = str(time.time()) + "@linkmail.com"
        password='qwe'+str(time.time())+'rty'
        self.page.register_new_user(email,password)
        self.page = ProductPage(browser,link)
        self.page.open()
        self.page.should_be_authorized_user()

    @pytest.mark.xfail   
    def test_user_cant_see_success_message_after_adding_product_to_basket(self,browser):
        self.page.add_product_to_basket()
        self.page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self,browser):
        self.page.add_product_to_basket()
        self.page.right_product_price()
        self.page.right_product_name()


class TestGuestAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self,browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        self.page = ProductPage(browser,link)
        self.page.open()

    @pytest.mark.xfail   
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self,browser):
        self.page.add_product_to_basket()
        self.page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self,browser):
        self.page.add_product_to_basket()
        #page.solve_quiz_and_get_code()
        self.page.right_product_price()
        self.page.right_product_name()

#@pytest.mark.skip    
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

#@pytest.mark.skip    
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_be_disappeared_message()
    
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_no_products()
    basket_page.should_be_empty_basket()
