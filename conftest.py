import pytest
import requests
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
        default="127.0.0.1",
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
    driver.maximize_window()
    request.addfinalizer(driver.quit)
    return driver
