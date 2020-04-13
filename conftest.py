import pytest
import requests


class APIClient:
    """Упрощенный клиент для работы с API"""

    def __init__(self, base_address):
        self.base_address = base_address

    def post(self, path="/", params=None, data=None, headers=None):
        url = self.base_address + path
        return requests.post(url=url, params=params, data=data, headers=headers, verify=False, timeout=3)

    def get(self, path="/", params=None):
        url = self.base_address + path
        return requests.get(url=url, params=params, verify=False, timeout=3)


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://jsonplaceholder.typicode.com",
        help="This is request url"
    )


@pytest.fixture(scope="session")
def api_client(request):
    base_url = request.config.getoption("--url")
    return APIClient(base_address=base_url)
