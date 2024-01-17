from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открываем страницу по URL={url}')
    def open_page(self, url):
        return self.driver.get(url)

    @allure.step('Ждем загрузки заголовка страницы')
    def wait_for_page_header_loaded(self, locator):
        return WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(locator))

    @allure.step('Ищем элемент по локатору')
    def find_element_located(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f'Element not found in {locator}')

    @allure.step('Кликаем по элементу')
    def click_element_located(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f'Element not found in {locator}').click()

    @allure.step('Ожидаем, что откроется новая вкладка')
    def wait_for_new_tab_opened(self, time=10):
        return WebDriverWait(self.driver, time).until(EC.number_of_windows_to_be(2))

    @allure.step('Скроллим страницу до элемента')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    @allure.step('Скроллим страницу до элемента и кликаем на него')
    def scroll_to_element_and_click(self, locator):
        self.scroll_to_element(locator)
        return self.click_element_located(locator)

    @allure.step('Получаем текст, находящийся по локатору')
    def get_text_by_locator(self, locator):
        return self.find_element_located(locator).text

    @allure.step('Переходим на открывшуюся вкладку')
    def switch_to_new_tab(self, tab):
        self.driver.switch_to.window(tab)
