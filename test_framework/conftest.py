import os

import allure
import pytest
from selenium import webdriver


class Environments:
    HOST = os.environ.get('HOST')

    REMOTE_SELENOID_SERVER = "http://localhost:4444/wd/hub"

    CAPABILITIES = {
        "browserName": "chrome",
        "version": "84.0",
    }

    BASE_URL = f"http://{HOST}:8000/accounts/login/"


@pytest.fixture
def browser():
    with allure.step(f"инициализируем remote driver : \
                     {Environments.REMOTE_SELENOID_SERVER}, \
                     {Environments.CAPABILITIES}"):
        driver = webdriver.Remote(Environments.REMOTE_SELENOID_SERVER, Environments.CAPABILITIES)

    with allure.step(f"открываем страницу {Environments.BASE_URL}"):
        driver.get(Environments.BASE_URL)
    yield driver
    screenshot = driver.get_screenshot_as_png()
    driver.quit()
    allure.attach(
        screenshot,
        name='screenshot',
        attachment_type=allure.attachment_type.PNG
    )
