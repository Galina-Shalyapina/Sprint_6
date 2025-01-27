from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element_visibility(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_element_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def wait_for_url_to_be(self, url, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.url_to_be(url)
        )

    def wait_for_url_contains(self, url_segment, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.url_contains(url_segment)
        )

    def find_element(self, locator):
        return self.wait_for_element_clickable(locator)

    def find_elements(self, locator):
        return self.wait_for_element_clickable(locator)

    def click_on_element(self, locator):
        self.find_element(locator).click()
