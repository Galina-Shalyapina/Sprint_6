import allure
from const import Const
import pytest
from locators.order_page_locators import OrderPageLocators


class TestCheckoutPath:

    @allure.title('Проверка кнопки «Заказать»  в хедере на лендинге Яндекс Самоката')
    @allure.description('Проверяем, что при нажатии на кнопку «Заказать» в хедере сайта, открывается форма заказа')
    def test_check_open_order_page_tap_button_in_header(self, main_page):
        main_page.open_main_page()

        main_page.tap_order_header_button()
        main_page.wait_for_url_to_be(Const.ORDER_PAGE)
        assert Const.ORDER_PAGE == main_page.get_current_url()

    @allure.title('Проверка midle-кнопки «Заказать» на лендинге Яндекс Самоката')
    @allure.description('Проверяем, что при нажатии на кнопку «Заказать» на странице сайта, открывается форма заказа')
    def test_check_open_order_page_tap_midlle_button(self, main_page):
        main_page.open_main_page()

        main_page.scroll_to_middle_button()
        main_page.tap_order_middle_button()
        main_page.wait_for_url_to_be(Const.ORDER_PAGE)
        assert Const.ORDER_PAGE == main_page.get_current_url()

    person_data = [
        ['Лариса', 'Степанова', 'Москва', 'Бульвар Рокоссовского', '79997330232', '15', 'двое суток', 'чёрный жемчуг', 'Оставьте у двери'],
        ['Игорь', 'Куприянов', 'Екатеринбург', 'Черкизовская', '79934340202', '19', 'четверо суток', 'серая безысходность', 'Оставьте у охраны'],
    ]

    @allure.title('Проверка флоу заказа самоката на сайте «Яндекс.Самоката»')
    @allure.description('Проверяем, форму заполнения при заказе самоката')
    @pytest.mark.parametrize("name, surname, address, station, phone, date_piker, rental_period, color, comment", person_data)
    def test_check_pop_up_window_successful_order(self, order_page, name, surname, address, station, phone, date_piker, rental_period, color, comment):
        order_page.open_order_page()
        order_page.order_about_person_page(name, surname, address, station, phone)
        order_page.tap_next_page_button()
        order_page.order_about_rental_page(date_piker, rental_period, color, comment)
        order_page.tap_order_final_button()
        order_page.tap_order_sure_button()
        assert order_page.is_order_successful()
