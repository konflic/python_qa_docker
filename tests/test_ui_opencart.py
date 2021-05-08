def test_main_page_menu(browser):
    browser.open_page(browser.base_url)
    menu_items = browser.find_elements_by_css_selector("ul.navbar-nav > li")
    assert len(menu_items) == 8, "Неверное количество элементов меню"


def test_main_page_fetured_items(browser):
    browser.open_page(browser.base_url)
    fetured_items = browser.find_elements_by_class_name("product-thumb")
    assert len(fetured_items) == 4, "Неверное количество продуктов в блоке featured"


def test_main_page_footer_blocks(browser):
    browser.open_page(browser.base_url)
    footer_blocks = browser.find_elements_by_xpath("//footer//ul")
    assert len(footer_blocks) == 4, "Неверное количество списков ссылок в футере"


def test_main_page_open_product(browser):
    browser.open_page(browser.base_url)
    fetured_items = browser.find_elements_by_class_name("product-thumb")
    fetured_items[2].click()
    browser.find_elements_by_link_text("Apple Cinema")
