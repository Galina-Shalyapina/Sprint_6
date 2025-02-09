from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ожидание видимости элемента')
    def wait_for_element_visibility(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step('Ожидание кликабельности элемента')
    def wait_for_element_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    @allure.step('Ожидание соответствия URL: {url}')
    def wait_for_url_to_be(self, url, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.url_to_be(url)
        )

    @allure.step('Ожидание наличия в URL: {url_segment}')
    def wait_for_url_contains(self, url_segment, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.url_contains(url_segment)
        )

    @allure.step('Поиск элемента')
    def find_element(self, locator):
        return self.wait_for_element_clickable(locator)

    @allure.step('Клик по элементу')
    def click_on_element(self, locator):
        self.find_element(locator).click()

    @allure.step('Открытие URL: {url}')
    def open_url(self, url):
        self.driver.get(url)

    @allure.step('Переключение на новое окно')
    def switch_to_new_window(self):
        original_window = self.driver.current_window_handle
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break

    @allure.step('Прокрутка к элементу')
    def scroll_into_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Получение текущего URL')
    def get_current_url(self):
        return self.driver.current_url
