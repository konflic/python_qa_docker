import allure

from framework import verify_element_presence


@allure.story("Google")
def test_google_0(browser):
    browser.open_page("https://google.ru")
    browser.check_in_title("Google")


@allure.story("Yandex")
def test_yandex_0(browser):
    browser.open_page("https://ya.ru")
    verify_element_presence(browser, "#text")
    verify_element_presence(browser, "a[title='Яндекс']")
    browser.check_in_title("Яндекс")


@allure.story("Avito")
def test_avito_0(browser):
    browser.open_page("https://avito.ru")
    verify_element_presence(browser, "#category")
    verify_element_presence(browser, "#search")
    browser.check_in_title("Авито")


@allure.story("Google")
def test_google_1(browser):
    browser.open_page("https://google.ru")
    verify_element_presence(browser, "#footer")
    verify_element_presence(browser, "#hplogo")
    browser.check_in_title("Google")


@allure.story("Yandex")
def test_yandex_1(browser):
    browser.open_page("https://ya.ru")
    verify_element_presence(browser, "#text")
    verify_element_presence(browser, "a[title='Яндекс']")
    browser.check_in_title("Яндекс")


@allure.story("Avito")
def test_avito_1(browser):
    browser.open_page("https://avito.ru")
    verify_element_presence(browser, "#category")
    verify_element_presence(browser, "#search")
    browser.check_in_title("Авито")
