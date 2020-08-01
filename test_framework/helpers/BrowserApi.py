from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

DEFAULT_ELEMENT_WAIT_TIMEOUT = 40


class BrowserApi:
    def __init__(self, driver):
        self._driver = driver

    def go_to_url(self, url):
        self._driver.get(url)

    def _get_tab_title(self):
        return self._driver.title

    def wait_for_element_present(self, locator, time=None):
        return WebDriverWait(self._driver, time or DEFAULT_ELEMENT_WAIT_TIMEOUT) \
            .until(expected_conditions.presence_of_element_located(locator),
                   message=f"Can't find element by locator {locator}")

    def click(self, locator):
        element = self.wait_for_element_present(locator)
        element.click()

    def get_element_text(self, locator):
        element = self.wait_for_element_present(locator)
        return element.text

    def get_element_attribute(self, locator, attribute_value):
        element = self.wait_for_element_present(locator)
        return element.get_attribute(attribute_value)

    def type(self, locator, send_value):
        element = self.wait_for_element_present(locator)
        element.clear()
        element.send_keys(send_value)

    def close_browser(self):
        if self._driver is not None:
            self._driver.quit()
