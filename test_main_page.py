"""
link = "http://selenium1py.pythonanywhere.com/"
def go_to_login_page(browser):
    browser.find_element_by_css_selector("#login_link").click()


def test_guest_can_go_to_login_page(browser):
    browser.get(link)
    go_to_login_page(browser)
"""
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
import pytest

@pytest.mark.skip
def test_page_to_login(browser):
    #link = "http://selenium1py.pythonanywhere.com/"
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open_page()
    page.go_to_login_page()

@pytest.mark.skip
def test_should_be_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser,link)
    page.open_page()
    page.should_be_login_link()

def test_should_be_page_Login(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page_log = LoginPage(browser,link)
    page_log.open_page()
    page_log.should_be_login_page()
