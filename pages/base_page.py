#cоздаем класс я так понимаю это шаблон для всех страниц

class  BasePage(object):
    #Создаем метод конструктор (__init__), он будет вызываться, когда будем создавать объект
    def __init__(self, browser, url):# и в конструктор передаем параметры, browser, url
        self.browser = browser # сохраняем как атрибут класса.
        self.url = url # сохраняем, как атрибут класса.

    def open_page(self): # метод открывает нужную страницу
        self.browser.get(self.url)









