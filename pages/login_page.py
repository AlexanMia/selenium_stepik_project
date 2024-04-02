from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "URL is not consist 'login'"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "LOGIN form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        self.go_to_login_page()
        self.send_keys_to_form(*LoginPageLocators.REG_EMAIL, text=email)
        self.send_keys_to_form(*LoginPageLocators.REG_PASSW, text=password)
        self.send_keys_to_form(*LoginPageLocators.REG_PASSW_2, text=password)
        self.click_button(*LoginPageLocators.BUTTON_REG)
