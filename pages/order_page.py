from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from const import Const
from locators.main_page_locators import MainPageLocators


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderPageLocators()

    def open_order_page(self):
        self.open_url(Const.ORDER_PAGE)

    def input_name(self, name):
        self.wait_for_element_visibility(self.locators.INPUT_NAME).send_keys(name)

    def input_surname(self, surname):
        self.wait_for_element_visibility(self.locators.INPUT_SURNAME).send_keys(surname)

    def input_address(self, address):
        self.wait_for_element_visibility(self.locators.INPUT_ADDRESS).send_keys(address)

    def select_subway_station(self, station):
        self.wait_for_element_clickable(self.locators.SELECT_SUBWAY).click()
        self.wait_for_element_clickable(self.locators.select_station_subway(station)).click()

    def input_telephone(self, phone):
        self.wait_for_element_visibility(self.locators.INPUT_TELEPHONE).send_keys(phone)

    def tap_next_page_button(self):
        self.click_on_element(self.locators.ORDER_NEXT_BUTTON)
        self.wait_for_element_visibility(OrderPageLocators.ORDER_HEADER_ABOUT_RENT)

    def select_delivery_date(self, date_piker):
        self.wait_for_element_clickable(self.locators.INPUT_DATA_PIKER).click()
        self.wait_for_element_clickable(self.locators.select_data_on_piker(date_piker)).click()

    def select_rental_period(self, rental_period):
        self.wait_for_element_clickable(self.locators.INPUT_DROPDOWN_RENTAL_PERIOD).click()
        self.wait_for_element_clickable(self.locators.select_dropdown_rental_period(rental_period)).click()

    def select_scooter_color(self, color):
        self.wait_for_element_clickable(self.locators.checkbox_color(color)).click()

    def input_comment(self, comment):
        self.wait_for_element_visibility(self.locators.INPUT_COMMENT).send_keys(comment)

    def tap_order_final_button(self):
        self.click_on_element(self.locators.ORDER_FINAL_BUTTON)

    def tap_order_sure_button(self):
        self.click_on_element(self.locators.ORDER_MODAL_SURE_BUTTON)

    def order_about_person_page(self, name, surname, address, station, phone):
        self.input_name(name)
        self.input_surname(surname)
        self.input_address(address)
        self.select_subway_station(station)
        self.input_telephone(phone)

    def order_about_rental_page(self, date_piker, rental_period, color, comment):
        self.select_delivery_date(date_piker)
        self.select_rental_period(rental_period)
        self.select_scooter_color(color)
        self.input_comment(comment)

    def tap_logo_scooter(self):
        self.wait_for_element_clickable(MainPageLocators.LOGO_SCOOTER).click()

    def is_order_successful(self):
        return self.wait_for_element_visibility(OrderPageLocators.ORDER_MODAL_HEADER_SUCCESSFULLY_PLACED)

    def get_current_url(self):
        return self.driver.current_url
