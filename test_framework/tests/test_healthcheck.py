import allure

from test_framework.page_object.ChecksPageObject import ChecksPageObject
from test_framework.page_object.LoginPageObject import LoginPageObject, Account


@allure.feature('Checks')
@allure.title('проверка эмэйла после логина')
def test_open_browser(browser):
    account = Account(email="example@mail.ru", password="111111")
    LoginPageObject(browser).login(account)

    with allure.step("проверяем отображение эмэйла после логина"):
        assert account.email == ChecksPageObject(browser).get_email_from_main_tab()


@allure.feature('Checks')
@allure.title('проверка количества чеков, которые отображаются на главной странице')
def test_open_browser_login(browser):
    LoginPageObject(browser).login(Account(email="example@mail.ru", password="111111"))

    with allure.step("проверяем количество чеков"):
        assert ChecksPageObject(browser).get_check_row_count() == 2


@allure.feature('Checks')
@allure.title('проверка отображения сообщения об ошибке в форме логина')
def test_displayed_error_message_after_input_incorrect_value(browser):
    login_page = LoginPageObject(browser)
    login_page.login(Account(email="example@mail.ru", password="1111111"))

    with allure.step("проверяем сообщение об ошибке"):
        assert login_page.get_error_message() == "Incorrect email or password."
