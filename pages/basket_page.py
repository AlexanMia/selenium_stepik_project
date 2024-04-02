from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_message_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.INFO_EMPTY_BASKET), \
            "There is no Info message about empty basket"

    def should_not_be_block_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BLOCK_ITEMS_IN_BASKET), \
            "Basket is not empty"
