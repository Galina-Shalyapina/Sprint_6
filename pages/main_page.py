from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from const import Const


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainPageLocators()

    def open_main_page(self):
        self.open_url(Const.MAIN_PAGE)

    def click_order_button_header(self):
        self.wait_for_element_clickable(self.locators.ORDER_BUTTON).click()

    def click_order_button_middle(self):
        element = self.find_element(self.locators.ORDER_MIDDLE_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.wait_for_element_clickable(self.locators.ORDER_MIDDLE_BUTTON).click()

    def tap_order_middle_button(self):
        self.click_order_button_middle()

    def click_dropdown_question(self, question_id):
        element = self.find_element(self.locators.dropdown_element_question(question_id))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.wait_for_element_clickable(self.locators.dropdown_element_question(question_id)).click()
        self.wait_for_element_visibility(self.locators.dropdown_element_answer(question_id))

    def get_dropdown_answer_text(self, answer_id):
        return self.wait_for_element_visibility(self.locators.dropdown_element_answer(answer_id)).text

    def click_scooter_logo(self):
        self.wait_for_element_clickable(self.locators.LOGO_SCOOTER).click()

    def click_yandex_logo(self):
        self.wait_for_element_clickable(self.locators.LOGO_YANDEX).click()
        self.switch_to_new_window()

    def tap_order_header_button(self):
        self.click_order_button_header()

    def scroll_to_middle_button(self):
        element = self.find_element(self.locators.ORDER_MIDDLE_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def tap_logo_yandex(self):
        self.click_yandex_logo()

    def scroll_to_dropdown_section(self):
        element = self.find_element(self.locators.DROPDOWN_SECTION)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def find_dropdown_question(self, id):
        return self.wait_for_element_visibility(self.locators.dropdown_element_question(id))

    def tap_on_question(self, id):
        self.click_dropdown_question(id)
        return self.wait_for_element_visibility(self.locators.dropdown_element_answer(id))

    def get_current_url(self):
        return self.driver.current_url
