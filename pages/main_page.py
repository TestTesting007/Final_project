from .base_page import BasePage # импорт базового класса из файла base_page.py
from selenium.webdriver.common.by import By
from .locators import MainPageLocators

#Создаем класс (наследуем из класса BasePage) наследники указываются в скобках
class MainPage(BasePage):
    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

