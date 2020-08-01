import time

import pytest
from selenium import webdriver

from tests.page_object.LoginPageObject import LoginPageObject, Account


@pytest.fixture
def browser():
    remote_server = "http://localhost:4444/wd/hub"
    capabilities = {
        "browserName": "chrome",
        "version": "78.0",
    }
    driver = webdriver.Remote(remote_server, capabilities)
    driver.get("http://localhost:8000/accounts/login/")
    yield driver
    driver.quit()


def test_open_browser(browser):
    login_page = LoginPageObject(browser)
    login_page.login(Account(email="example@mail.ru", password="111111"))
