from locators.dzen_main_page_locators import DzenMainPageLocators
from pages.base_page import BasePage


class DzenMainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = DzenMainPageLocators()

    def wait_for_dzen_page_load(self):
        self.wait_for_element_visibility(self.locators.HEADER_YANDEX_DZEN)

    def is_dzen_header_displayed(self):
        try:
            self.wait_for_dzen_page_load()
            return True
        except:
            return False
