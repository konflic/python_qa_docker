import allure


@allure.story("Google")
def test_google_0(remote):
    remote.open_page("https://google.ru")
    remote.check_in_title("Google")


@allure.story("Yandex")
def test_yandex_0(remote):
    remote.open_page("https://ya.ru")
    remote.find_element_by_id("text")
    remote.find_element_by_css_selector("a[title='Яндекс']")
    remote.check_in_title("Яндекс")


@allure.story("Avito")
def test_avito_0(remote):
    remote.open_page("https://avito.ru")
    remote.find_element_by_id("category")
    remote.find_element_by_id("search")
    remote.check_in_title("Авито")


@allure.story("Google")
def test_google_1(remote):
    remote.open_page("https://google.ru")
    remote.find_element_by_id("footer")
    remote.find_element_by_id("hplogo")
    remote.check_in_title("Google")


@allure.story("Yandex")
def test_yandex_1(remote):
    remote.open_page("https://ya.ru")
    remote.find_element_by_id("text")
    remote.find_element_by_css_selector("a[title='Яндекс']")
    remote.check_in_title("Яндекс")


@allure.story("Avito")
def test_avito_1(remote):
    remote.open_page("https://avito.ru")
    remote.find_element_by_id("category")
    remote.find_element_by_id("search")
    remote.check_in_title("Авито")
