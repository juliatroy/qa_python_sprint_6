from pages.order_page import OrderPage
from data.urls import URLS
from time import sleep
import allure


class TestOrdersRedirect:
    @allure.description('Клик по логотипу Яндекса"')
    def test_check_orders_page_to_yandex_redirect(self, driver):
        page = OrderPage(driver)
        page.open_order_page()
        page.click_yandex_logo()
        page.wait_for_new_tab_opened()
        page.switch_to_new_tab(driver.window_handles[1])
        sleep(3)  # wait for new page is loaded
        assert 'dzen' in page.get_current_url()

    @allure.description('Клик по логотипу Самоката"')
    def test_check_orders_page_to_samokat_redirect(self, driver):
        page = OrderPage(driver)
        page.open_order_page()
        page.click_samokat_logo()
        assert page.get_current_url() == URLS.MAIN_PAGE_URL

