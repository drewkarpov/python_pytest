import os
import pytest
from selenium import webdriver


class Environments:
    HOST = os.environ.get('HOST')


@pytest.fixture
def browser():
    remote_server = "http://localhost:4444/wd/hub"
    capabilities = {
        "browserName": "chrome",
        "version": "84.0",
    }
    driver = webdriver.Remote(remote_server, capabilities)
    driver.get(f"http://{Environments.HOST}:8000/accounts/login/")
    yield driver
    driver.quit()
