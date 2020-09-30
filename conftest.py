import allure
import pytest
import requests
import json
from selenium import webdriver


class APIClient:
    """Упрощенный клиент для работы с API"""

    def __init__(self, base_address):
        self.base_address = base_address

    def post(self, path="/", params=None, data=None, headers=None):
        url = self.base_address + path
        return requests.post(url=url, params=params, data=data, headers=headers, verify=False)

    def get(self, path="/", params=None):
        url = self.base_address + path
        return requests.get(url=url, params=params, verify=False)


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://jsonplaceholder.typicode.com",
    )
    parser.addoption(
        "--browser",
        default="chrome",
    )
    parser.addoption(
        "--executor",
        # Локальный ip адресс хоста где selenium
        default="192.168.1.68",
    )


@pytest.fixture(scope="session")
def api_client(request):
    base_url = request.config.getoption("--url")
    return APIClient(base_address=base_url)


@pytest.fixture
def remote(request):
    browser = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")
    driver = webdriver.Remote(
        command_executor=f"http://{executor}:4444/wd/hub",
        desired_capabilities={"browserName": browser}
    )
    allure.attach(body=json.dumps(driver.capabilities), attachment_type=allure.attachment_type.JSON)
    driver.maximize_window()
    request.addfinalizer(driver.quit)
    return driver
