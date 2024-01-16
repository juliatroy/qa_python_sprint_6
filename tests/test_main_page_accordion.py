import allure
import pytest

from data.locators import MainPageLocators
from data.text_constants import AccordionHeaders
from data.text_constants import AccordionTexts
from pages.main_page import MainPageScooter


class TestMainPageAccordion:
    @allure.title('Проверка секции "Вопросы о важном"')
    @pytest.mark.parametrize('header, locator, text, text_locator',
                             [
                                 (AccordionHeaders.ACCORDION_HEADER_0_PRICE_TEXT, MainPageLocators.ACCORDION_HEADER_0_PRICE,
                                  AccordionTexts.ACCORDION_TEXT_0_PRICE_TEXT, MainPageLocators.ACCORDION_TEXT_0_PRICE),
                                 (AccordionHeaders.ACCORDION_HEADER_1_QUANTITY_TEXT, MainPageLocators.ACCORDION_HEADER_1_QUANTITY,
                                  AccordionTexts.ACCORDION_TEXT_1_QUANTITY_TEXT, MainPageLocators.ACCORDION_TEXT_1_QUANTITY),
                                 (AccordionHeaders.ACCORDION_HEADER_2_TIME_TEXT, MainPageLocators.ACCORDION_HEADER_2_TIME,
                                  AccordionTexts.ACCORDION_TEXT_2_TIME_TEXT, MainPageLocators.ACCORDION_TEXT_2_TIME),
                                 (AccordionHeaders.ACCORDION_HEADER_3_DATE_TEXT, MainPageLocators.ACCORDION_HEADER_3_DATE,
                                  AccordionTexts.ACCORDION_TEXT_3_DATE_TEXT, MainPageLocators.ACCORDION_TEXT_3_DATE),
                                 (AccordionHeaders.ACCORDION_HEADER_4_DURATION_TEXT, MainPageLocators.ACCORDION_HEADER_4_DURATION,
                                  AccordionTexts.ACCORDION_TEXT_4_DURATION_TEXT, MainPageLocators.ACCORDION_TEXT_4_DURATION),
                                 (AccordionHeaders.ACCORDION_HEADER_5_CHARGE_TEXT, MainPageLocators.ACCORDION_HEADER_5_CHARGE,
                                  AccordionTexts.ACCORDION_TEXT_5_CHARGE_TEXT, MainPageLocators.ACCORDION_TEXT_5_CHARGE),
                                 (AccordionHeaders.ACCORDION_HEADER_6_CANCEL_TEXT, MainPageLocators.ACCORDION_HEADER_6_CANCEL,
                                  AccordionTexts.ACCORDION_TEXT_6_CANCEL_TEXT, MainPageLocators.ACCORDION_TEXT_6_CANCEL),
                                 (AccordionHeaders.ACCORDION_HEADER_7_LOCATION_TEXT, MainPageLocators.ACCORDION_HEADER_7_LOCATION,
                                  AccordionTexts.ACCORDION_TEXT_7_LOCATION_TEXT, MainPageLocators.ACCORDION_TEXT_7_LOCATION)
                             ]
                             )
    @allure.description('Проверяем соответствие вопроса ожидаемой формулировке, '
                        ' ответа на вопрос - ожидаемому ответу"')
    def test_check_important_questions_subsection_headers(self, driver, header, locator, text, text_locator):
        page = MainPageScooter(driver)
        page.open_main_page()
        page.wait_for_main_page_header_loaded()
        page.scroll_to_important_questions_subsection()
        header_found = page.get_text_by_locator(locator)
        page.click_element_located(locator)
        text_found = page.get_text_by_locator(text_locator)
        assert header_found == header and text_found == text
