from selenium.webdriver.common.by import By

from test_framework.helpers.BrowserApi import BrowserApi


class ChecksPageSelector:
    CHECKS_ROW = (By.XPATH, "//*[@class='checks-row']")
    EMAIL_TAB = (By.ID, "base-url")


class ChecksPageObject(BrowserApi):
    def __init__(self, driver):
        super().__init__(driver)

    def get_check_row_count(self):
        return len(self._get_elements(ChecksPageSelector.CHECKS_ROW))

    def get_email_from_main_tab(self):
        return self._get_element_text(ChecksPageSelector.EMAIL_TAB)
