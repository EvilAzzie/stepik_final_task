from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "This URL not for login page"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "No login form"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "No register form"

    def register_new_user(self,email,password):
        user_email=self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_LINK)
        user_email.send_keys(str(email))
        user_password=self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_LINK)
        user_password.send_keys(str(password))
        user_password_2=self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_LINK_2)
        user_password_2.send_keys(str(password))
        register_button=self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()
        
        
