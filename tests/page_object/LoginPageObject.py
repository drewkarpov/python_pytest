from dataclasses import dataclass

from selenium.webdriver.common.by import By

from tests.helpers.BrowserApi import BrowserApi


class LoginSelector:
    LOGIN_FIELD = (By.XPATH, "//*[@id='login-form']//*[@name='email']")
    PASSWORD_FIELD = (By.XPATH, "//*[@id='login-form']//*[@name='password']")
    SUBMIT_BUTTON = (By.XPATH, "//*[@id='login-form']//button")


@dataclass
class Account:
    email: str
    password: str


class LoginPageObject(BrowserApi):
    def __init__(self, driver):
        super().__init__(driver)

    def login(self, account: Account):
        self.type(locator=LoginSelector.LOGIN_FIELD, send_value=account.email)
        self.type(locator=LoginSelector.PASSWORD_FIELD, send_value=account.password)
        self.click(locator=LoginSelector.SUBMIT_BUTTON)
