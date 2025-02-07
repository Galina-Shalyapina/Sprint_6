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

    def open_url(self, url):
        self.driver.get(url)

    def switch_to_new_window(self):
        original_window = self.driver.current_window_handle
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break
