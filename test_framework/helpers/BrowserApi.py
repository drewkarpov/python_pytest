import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

DEFAULT_ELEMENT_WAIT_TIMEOUT = 40


class BrowserApi:
    def __init__(self, driver):
        self._driver = driver

    def __wait_for_element_present(self, locator, time=None):
        return WebDriverWait(self._driver, time or DEFAULT_ELEMENT_WAIT_TIMEOUT) \
            .until(expected_conditions.presence_of_element_located(locator),
                   message=f"Не найден элемент с локатором {locator}")

    def _click(self, locator):
        with allure.step(f"кликаем по элементу  {locator}"):
            element = self.__wait_for_element_present(locator)
            element.click()

    def _get_element_text(self, locator):
        element = self.__wait_for_element_present(locator)
        return element.text

    def _get_element_attribute(self, locator, attribute_value):
        element = self.__wait_for_element_present(locator)
        return element.get_attribute(attribute_value)

    def _type(self, locator, send_value):
        with allure.step(f"вводим {send_value} в поле {locator}"):
            element = self.__wait_for_element_present(locator)
            element.clear()
            element.send_keys(send_value)

    def _get_elements(self, locator):
        self.__wait_for_element_present(locator)
        return self._driver.find_elements(*locator)
