from test_framework.page_object.LoginPageObject import LoginPageObject, Account


def test_open_browser(browser):
    login_page = LoginPageObject(browser)
    login_page.login(Account(email="example@mail.ru", password="111111"))
