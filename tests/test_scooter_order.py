import pytest
import allure
from pages.main_page import MainPageScooter
from pages.order_page import OrderPage
from data.user_data import UserDataSet
from data.user_data import UserDataSetExtra


class TestOrderScooterPage:
    @allure.title('Проверка флоу заказа самоката')
    @pytest.mark.parametrize('button_position, user_data_set',
                             [
                                 ("top", UserDataSet),
                                 ("bottom", UserDataSetExtra)
                             ]
                             )
    @allure.description('Точка входа задается в параметре button_position')
    def test_order_scooter_positive(self, driver, button_position, user_data_set):
        page = MainPageScooter(driver)
        page.open_main_page()
        page.wait_for_main_page_header_loaded()
        page.click_order_button(button_position)
        order_page = OrderPage(driver)
        order_page.fill_order_form(user_data_set.FIRST_NAME, user_data_set.LAST_NAME, user_data_set.ADDRESS,
                                   user_data_set.METRO_STATION, user_data_set.PHONE)
        order_page.click_next_button()
        order_page.fill_rent_form(user_data_set.DATE, user_data_set.DURATION, user_data_set.COLOR,
                                  user_data_set.COMMENT)
        order_page.click_submit_order_button()
        order_page.wait_for_modal_window_header_loaded()
        order_page.click_confirm_button()
        assert 'Заказ оформлен' in order_page.get_confirmation_window_header()
