#cоздаем класс я так понимаю это шаблон для всех страниц
from selenium.common.exceptions import NoSuchElementException
class  BasePage(object):
    #Создаем метод конструктор (__init__), он будет вызываться, когда будем создавать объект
    def __init__(self, browser, url,timeout=10):# и в конструктор передаем параметры, browser, url
        self.browser = browser # сохраняем как атрибут класса.
        self.url = url # сохраняем, как атрибут класса.
        self.browser.implicitly_wait(timeout) # добавил неявное ожидание

    def open_page(self): # метод открывает нужную страницу
        self.browser.get(self.url)

    def is_element_present(self,how,what): #Метод проверки элемента на странице (Передаем параметр how- как и what -что ищем
        try:
            self.browser.find_element(how,what)
        except NoSuchElementException:
            return False
        return True











