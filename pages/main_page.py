from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from const import Const
import allure


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainPageLocators()

    @allure.step('Открыть главную страницу')
    def open_main_page(self):
        self.open_url(Const.MAIN_PAGE)

    @allure.step('Нажать кнопку заказа в хедере')
    def click_order_button_header(self):
        self.wait_for_element_clickable(self.locators.ORDER_BUTTON).click()

    @allure.step('Нажать кнопку заказа в середине страницы')
    def click_order_button_middle(self):
        element = self.find_element(self.locators.ORDER_MIDDLE_BUTTON)
        self.scroll_into_element(element)
        self.wait_for_element_clickable(self.locators.ORDER_MIDDLE_BUTTON).click()

    @allure.step('Нажать среднюю кнопку заказа')
    def tap_order_middle_button(self):
        self.click_order_button_middle()

    @allure.step('Нажать на вопрос {question_id} в выпадающем списке')
    def click_dropdown_question(self, question_id):
        element = self.find_element(self.locators.dropdown_element_question(question_id))
        self.scroll_into_element(element)
        self.wait_for_element_clickable(self.locators.dropdown_element_question(question_id)).click()
        self.wait_for_element_visibility(self.locators.dropdown_element_answer(question_id))

    @allure.step('Получить текст ответа {answer_id}')
    def get_dropdown_answer_text(self, answer_id):
        return self.wait_for_element_visibility(self.locators.dropdown_element_answer(answer_id)).text

    @allure.step('Нажать на логотип самоката')
    def click_scooter_logo(self):
        self.wait_for_element_clickable(self.locators.LOGO_SCOOTER).click()

    @allure.step('Нажать на логотип Яндекса')
    def click_yandex_logo(self):
        self.wait_for_element_clickable(self.locators.LOGO_YANDEX).click()
        self.switch_to_new_window()

    @allure.step('Нажать кнопку заказа в хедере')
    def tap_order_header_button(self):
        self.click_order_button_header()

    @allure.step('Прокрутить до средней кнопки')
    def scroll_to_middle_button(self):
        element = self.find_element(self.locators.ORDER_MIDDLE_BUTTON)
        self.scroll_into_element(element)

    @allure.step('Нажать на логотип Яндекса')
    def tap_logo_yandex(self):
        self.click_yandex_logo()

    @allure.step('Прокрутить до секции с выпадающим списком')
    def scroll_to_dropdown_section(self):
        element = self.find_element(self.locators.DROPDOWN_SECTION)
        self.scroll_into_element(element)

    @allure.step('Найти вопрос с id {id}')
    def find_dropdown_question(self, id):
        return self.wait_for_element_visibility(self.locators.dropdown_element_question(id))

    @allure.step('Нажать на вопрос с id {id}')
    def tap_on_question(self, id):
        self.click_dropdown_question(id)
        return self.wait_for_element_visibility(self.locators.dropdown_element_answer(id))
