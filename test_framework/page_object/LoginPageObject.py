from dataclasses import dataclass

import allure
from selenium.webdriver.common.by import By

from test_framework.helpers.BrowserApi import BrowserApi


class LoginPageSelector:
    LOGIN_FIELD = (By.XPATH, "//*[@id='login-form']//*[@name='email']")
    PASSWORD_FIELD = (By.XPATH, "//*[@id='login-form']//*[@name='password']")
    SUBMIT_BUTTON = (By.XPATH, "//*[@id='login-form']//button")
    ERROR_MESSAGE = (By.XPATH, "//*[@id='login-form']//*[@class='text-danger']")


@dataclass
class Account:
    email: str
    password: str


class LoginPageObject(BrowserApi):
    def __init__(self, driver):
        super().__init__(driver)

    def login(self, account: Account):
        with allure.step(f"логинимся под эмэйлом {account.email}"):
            self._type(locator=LoginPageSelector.LOGIN_FIELD, send_value=account.email)
            self._type(locator=LoginPageSelector.PASSWORD_FIELD, send_value=account.password)
            self._click(locator=LoginPageSelector.SUBMIT_BUTTON)

    def get_error_message(self):
        with allure.step("получаем текст ошибки"):
            return self._get_element_text(locator=LoginPageSelector.ERROR_MESSAGE)
