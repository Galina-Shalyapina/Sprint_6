from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from const import Const
from locators.main_page_locators import MainPageLocators
import allure


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderPageLocators()

    @allure.step('Открыть страницу заказа')
    def open_order_page(self):
        self.open_url(Const.ORDER_PAGE)

    @allure.step('Ввести имя: {name}')
    def input_name(self, name):
        self.wait_for_element_visibility(self.locators.INPUT_NAME).send_keys(name)

    @allure.step('Ввести фамилию: {surname}')
    def input_surname(self, surname):
        self.wait_for_element_visibility(self.locators.INPUT_SURNAME).send_keys(surname)

    @allure.step('Ввести адрес: {address}')
    def input_address(self, address):
        self.wait_for_element_visibility(self.locators.INPUT_ADDRESS).send_keys(address)

    @allure.step('Выбрать станцию метро: {station}')
    def select_subway_station(self, station):
        self.wait_for_element_clickable(self.locators.SELECT_SUBWAY).click()
        self.wait_for_element_clickable(self.locators.select_station_subway(station)).click()

    @allure.step('Ввести номер телефона: {phone}')
    def input_telephone(self, phone):
        self.wait_for_element_visibility(self.locators.INPUT_TELEPHONE).send_keys(phone)

    @allure.step('Нажать кнопку Далее')
    def tap_next_page_button(self):
        self.click_on_element(self.locators.ORDER_NEXT_BUTTON)
        self.wait_for_element_visibility(OrderPageLocators.ORDER_HEADER_ABOUT_RENT)

    @allure.step('Выбрать дату доставки: {date_piker}')
    def select_delivery_date(self, date_piker):
        self.wait_for_element_clickable(self.locators.INPUT_DATA_PIKER).click()
        self.wait_for_element_clickable(self.locators.select_data_on_piker(date_piker)).click()

    @allure.step('Выбрать срок аренды: {rental_period}')
    def select_rental_period(self, rental_period):
        self.wait_for_element_clickable(self.locators.INPUT_DROPDOWN_RENTAL_PERIOD).click()
        self.wait_for_element_clickable(self.locators.select_dropdown_rental_period(rental_period)).click()

    @allure.step('Выбрать цвет самоката: {color}')
    def select_scooter_color(self, color):
        self.wait_for_element_clickable(self.locators.checkbox_color(color)).click()

    @allure.step('Ввести комментарий: {comment}')
    def input_comment(self, comment):
        self.wait_for_element_visibility(self.locators.INPUT_COMMENT).send_keys(comment)

    @allure.step('Нажать кнопку Заказать')
    def tap_order_final_button(self):
        self.click_on_element(self.locators.ORDER_FINAL_BUTTON)

    @allure.step('Подтвердить заказ')
    def tap_order_sure_button(self):
        self.click_on_element(self.locators.ORDER_MODAL_SURE_BUTTON)

    @allure.step('Заполнить данные о пользователе: имя {name}, фамилия {surname}, адрес {address}, станция {station}, телефон {phone}')
    def order_about_person_page(self, name, surname, address, station, phone):
        self.input_name(name)
        self.input_surname(surname)
        self.input_address(address)
        self.select_subway_station(station)
        self.input_telephone(phone)

    @allure.step('Заполнить данные об аренде: дата {date_piker}, срок {rental_period}, цвет {color}, комментарий {comment}')
    def order_about_rental_page(self, date_piker, rental_period, color, comment):
        self.select_delivery_date(date_piker)
        self.select_rental_period(rental_period)
        self.select_scooter_color(color)
        self.input_comment(comment)

    @allure.step('Нажать на логотип самоката')
    def tap_logo_scooter(self):
        self.wait_for_element_clickable(MainPageLocators.LOGO_SCOOTER).click()

    @allure.step('Проверить успешность оформления заказа')
    def is_order_successful(self):
        return self.wait_for_element_visibility(OrderPageLocators.ORDER_MODAL_HEADER_SUCCESSFULLY_PLACED)
