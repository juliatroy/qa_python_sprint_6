from selenium.webdriver.common.by import By


class MainPageLocators:
    MAIN_PAGE_HEADER = (By.CLASS_NAME, 'Home_Header__iJKdX')
    SUBSECTION_HEADER = (By.XPATH, '//div[text()="Вопросы о важном"]')

    BOTTOM_ORDER_BUTTON = (By.XPATH, "//div[@class='Home_FinishButton__1_cWm']//button[text() = 'Заказать']")
    TOP_ORDER_BUTTON = (By.CLASS_NAME, 'Button_Button__ra12g')

    ACCORDION_HEADER_0_PRICE = (By.ID, 'accordion__heading-0')
    ACCORDION_HEADER_1_QUANTITY = (By.ID, 'accordion__heading-1')
    ACCORDION_HEADER_2_TIME = (By.ID, 'accordion__heading-2')
    ACCORDION_HEADER_3_DATE = (By.ID, 'accordion__heading-3')
    ACCORDION_HEADER_4_DURATION = (By.ID, 'accordion__heading-4')
    ACCORDION_HEADER_5_CHARGE = (By.ID, 'accordion__heading-5')
    ACCORDION_HEADER_6_CANCEL = (By.ID, 'accordion__heading-6')
    ACCORDION_HEADER_7_LOCATION = (By.ID, 'accordion__heading-7')

    ACCORDION_TEXT_0_PRICE = (By.ID, 'accordion__panel-0')
    ACCORDION_TEXT_1_QUANTITY = (By.ID, 'accordion__panel-1')
    ACCORDION_TEXT_2_TIME = (By.ID, 'accordion__panel-2')
    ACCORDION_TEXT_3_DATE = (By.ID, 'accordion__panel-3')
    ACCORDION_TEXT_4_DURATION = (By.ID, 'accordion__panel-4')
    ACCORDION_TEXT_5_CHARGE = (By.ID, 'accordion__panel-5')
    ACCORDION_TEXT_6_CANCEL = (By.ID, 'accordion__panel-6')
    ACCORDION_TEXT_7_LOCATION = (By.ID, 'accordion__panel-7')


class OrderPageLocators:
    ORDER_PAGE_HEADER = (By.XPATH, "//div[text()='Для кого самокат']")

    INPUT_FIRST_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    INPUT_LAST_NAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    INPUT_ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    INPUT_METRO_STATION = (By.XPATH, "//input[@placeholder='* Станция метро']")
    INPUT_PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text() = 'Далее']")

    RENT_PAGE_HEADER = (By.XPATH, "//div[text()='Про аренду']")
    DATE_PICKER = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    DURATION_SELECT = (By.CLASS_NAME, 'Dropdown-root')
    INPUT_COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//div[@class='Order_Buttons__1xGrp']//button[text() = 'Заказать']")

    MODAL_WINDOW_HEADER = (By.XPATH, "//div[text()='Хотите оформить заказ?']")
    CONFIRM_BUTTON = (By.XPATH, "//button[text() = 'Да']")
    CONFIRMATION_HEADER = (By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ']")

    YANDEX_LOGO = (By.CLASS_NAME, 'Header_LogoYandex__3TSOI')
    SAMOKAT_LOGO = (By.CLASS_NAME, 'Header_LogoScooter__3lsAR')




