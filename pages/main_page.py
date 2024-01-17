from pages.base_page import BasePage
from data.locators import MainPageLocators
from data.urls import URLS
import allure


class MainPageScooter(BasePage):

    @allure.step('Открываем главную страницу проекта')
    def open_main_page(self):
        self.open_page(URLS.MAIN_PAGE_URL)

    @allure.step('Ждем загрузки заголовка главной страницы проекта')
    def wait_for_main_page_header_loaded(self):
        self.wait_for_page_header_loaded(MainPageLocators.MAIN_PAGE_HEADER)

    @allure.step('Скроллим страницу вниз до секции "Вопросы о важном"')
    def scroll_to_important_questions_subsection(self):
        self.scroll_to_element(MainPageLocators.SUBSECTION_HEADER)

    @allure.step('Выбираем локатор для кнопки "Заказать" в зависимости от ее местоположения на странице: {position}')
    def click_order_button(self, position):
        if position == 'top':
            return self.click_element_located(MainPageLocators.TOP_ORDER_BUTTON)
        elif position == 'bottom':
            return self.scroll_to_element_and_click(MainPageLocators.BOTTOM_ORDER_BUTTON)


