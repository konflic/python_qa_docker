import selenium
import allure


@allure.step("Verify element {css_selector} on page.")
def verify_element_presence(driver, css_selector):
    try:
        driver.find_element_by_css_selector(css_selector)
    except selenium.common.exceptions.NoSuchElementException:
        allure.attach(
            name=driver.session_id,
            body=driver.get_screenshot_as_png(),
            attachment_type=allure.attachment_type.PNG
        )
        raise AssertionError(f"Element {css_selector} not found on page!")
