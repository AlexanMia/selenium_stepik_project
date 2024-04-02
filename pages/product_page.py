from pages.base_page import BasePage
from pages.locators import MainPageLocators, ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        button_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button_basket.click()
        self.solve_quiz_and_get_code()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_correct_product(self):
        assert self.browser.find_element(*ProductPageLocators.NAME_BOOK_IN_BASKET).text in self.browser.find_element(
            *ProductPageLocators.NAME_BOOK).text, "Title of book is not equal"

    def should_be_correct_price(self):
        assert self.browser.find_element(*ProductPageLocators.PRICE_BOOK).text == self.browser.find_element(
            *ProductPageLocators.PRICE_BOOK).text, "Price of book is not equal"

    def should_not_be_success_message(self):
        assert not self.is_element_present(*ProductPageLocators.INFO_ADD_BASKET), \
            "Success message is presented"
