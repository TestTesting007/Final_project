from .base_page import BasePage # импорт базового класса из файла base_page.py
from selenium.webdriver.common.by import By

#Создаем класс (наследуем из класса BasePage) наследники указываются в скобках
class MainPage(BasePage):
    def go_to_login_page(self):
        link = self.browser.find_element(By.CSS_SELECTOR,"#login_link")
        link.click()


