from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link")
    BUTTON_BASKET = (By.CSS_SELECTOR, ".btn-group > a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    BUTTON_SIGN_IN_UP = (By.ID, "login_link")
    LOGIN_FORM = (By.ID, "login_form")
    EMAIL = (By.ID, "id_login-username")
    PASSW = (By.ID, "id_login-password")
    BUTTON_ENTER = (By.NAME, "login_submit")
    REGISTER_FORM = (By.ID, "register_form")
    REG_EMAIL = (By.ID, "id_registration-email")
    REG_PASSW = (By.ID, "id_registration-password1")
    REG_PASSW_2 = (By.ID, "id_registration-password2")
    BUTTON_REG = (By.NAME, "registration_submit")


class ProductPageLocators:
    ADD_TO_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    NAME_BOOK = (By.CLASS_NAME, "product_main")
    INFO_ADD_BASKET = (By.CLASS_NAME, "alertinner ")
    NAME_BOOK_IN_BASKET = (By.CSS_SELECTOR, "#messages strong")
    PRICE_BOOK_IN_BASKET = (By.XPATH, "//div[@class='alertinner ']/p[1]/strong")
    PRICE_BOOK = (By.CSS_SELECTOR, "div.col-sm-6.product_main p.price_color")


class BasketPageLocators:
    INFO_EMPTY_BASKET = (By.ID, "content_inner")
    BLOCK_ITEMS_IN_BASKET = (By.CSS_SELECTOR, ".basket-items")
