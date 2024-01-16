from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from data.locators import OrderPageLocators
from data.urls import URLS
import allure


class OrderPage(BasePage):

    @allure.step('Открываем окно оформления заказа по URL')
    def open_order_page(self):
        self.open_page(URLS.ORDER_PAGE_URL)

    @allure.step('Ввод текстовых данных')
    def enter_text_to_element_located(self, text, locator):
        self.find_element_located(locator).send_keys(text)

    @allure.step('Выбор элемента дропдаун листа')
    def select_dropdown_element_value(self, value, locator):
        self.click_element_located(locator)
        letter = value[0]
        self.find_element_located(locator).send_keys(letter)
        create_xpath = f".//*[text()='{value}']"
        self.click_element_located([By.XPATH, create_xpath])

    @allure.step('Клик по элементу чекбокса')
    def click_checkbox_element(self, value):
        create_xpath = f".//label[@for='{value}']"
        self.click_element_located([By.XPATH, create_xpath])

    @allure.step('Заполняем первую часть формы заказа данными - Имя, Фамилия, Адрес, Станция метро, Телефон')
    def fill_order_form(self, first_name, last_name, address, metro_station, phone):
        self.wait_for_page_header_loaded(OrderPageLocators.ORDER_PAGE_HEADER)
        self.enter_text_to_element_located(first_name, OrderPageLocators.INPUT_FIRST_NAME)
        self.enter_text_to_element_located(last_name, OrderPageLocators.INPUT_LAST_NAME)
        self.enter_text_to_element_located(address, OrderPageLocators.INPUT_ADDRESS)
        self.select_dropdown_element_value(metro_station, OrderPageLocators.INPUT_METRO_STATION)
        self.enter_text_to_element_located(phone, OrderPageLocators.INPUT_PHONE)

    @allure.step('Заполняем вторую часть формы заказа данными - Дата, Длительность аренды, Цвет, Комментарий')
    def fill_rent_form(self, date, duration, color, comment):
        self.wait_for_page_header_loaded(OrderPageLocators.RENT_PAGE_HEADER)
        self.enter_text_to_element_located(date, OrderPageLocators.DATE_PICKER)
        self.enter_text_to_element_located(Keys.ENTER, OrderPageLocators.DATE_PICKER)
        self.click_element_located(OrderPageLocators.DURATION_SELECT)
        create_xpath = f".//*[text()='{duration}']"
        self.click_element_located([By.XPATH, create_xpath])
        self.click_checkbox_element(color)
        self.enter_text_to_element_located(comment, OrderPageLocators.INPUT_COMMENT)

    @allure.step('Нажимаем кнопку "Далее"')
    def click_next_button(self):
        self.click_element_located(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Нажимаем кнопку "Заказать" под формой заказа')
    def click_submit_order_button(self):
        self.click_element_located(OrderPageLocators.ORDER_BUTTON)

    @allure.step('Ждем загрузки заголовка модального окна')
    def wait_for_modal_window_header_loaded(self):
        self.wait_for_page_header_loaded(OrderPageLocators.MODAL_WINDOW_HEADER)

    @allure.step('Нажимаем кнопку "Да" в модальном окне')
    def click_confirm_button(self):
        self.click_element_located(OrderPageLocators.CONFIRM_BUTTON)

    @allure.step('Получаем текст заголовка окна подтверждения заказа')
    def get_confirmation_window_header(self):
        return self.get_text_by_locator(OrderPageLocators.CONFIRMATION_HEADER)

    @allure.step('Клик по логотипу Яндекса в верхнем левом углу')
    def click_yandex_logo(self):
        self.click_element_located(OrderPageLocators.YANDEX_LOGO)

    @allure.step('Клик по логотипу Самоката в верхнем левом углу')
    def click_samokat_logo(self):
        self.click_element_located(OrderPageLocators.SAMOKAT_LOGO)
