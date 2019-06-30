"""
link = "http://selenium1py.pythonanywhere.com/"
def go_to_login_page(browser):
    browser.find_element_by_css_selector("#login_link").click()


def test_guest_can_go_to_login_page(browser):
    browser.get(link)
    go_to_login_page(browser)
"""
from .pages.main_page import MainPage


def test_page_to_login(browser):
    link = "http://selenium1py.pythonanywhere.com/"

    page = MainPage(browser, link)
    page.open_page()
    # page.go_to_login_page()
    page.should_be_login_link()
