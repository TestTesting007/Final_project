from selenium.webdriver.common.by import By
class MainPageLocators(object):
    LOGIN_LINK=(By.CSS_SELECTOR,"#login_link")

class LoginPageLocators(object):
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTR_FORM = (By.CSS_SELECTOR,"#register_fo3rm")