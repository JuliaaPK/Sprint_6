import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import URLS
from locators.locators_order_page import LocatorsOrder
from pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step("Перейти к созданию заказа")
    def go_to_crete_order(self):
        self.js_click_element_by_locator(LocatorsOrder.UP_ORDER_BUTTON)

    @allure.step("Заполнение поля Имя")
    def set_name(self, name):
        name_field = self.wait_and_find_element(LocatorsOrder.NAME_FIELD)
        name_field.send_keys(name)

    @allure.step("Заполнение поля Фамилия")
    def set_surname(self, surname):
        surname_field = self.wait_and_find_element(LocatorsOrder.SURNAME_FIELD)
        surname_field.send_keys(surname)

    @allure.step("Заполнение поля Адрес")
    def set_address(self, address):
        address_filed = self.wait_and_find_element(LocatorsOrder.ADDRESS_FIELD)
        address_filed.send_keys(address)

    @allure.step("Выбор станции метро")
    def set_metro(self, metro_option):
        self.click_element_by_locator(LocatorsOrder.METRO_FIELD)
        self.click_element_by_locator(LocatorsOrder.get_metro_option(metro_option))

    @allure.step("Заполнение поля Номер телефона")
    def set_phone(self, phone):
        address_filed = self.wait_and_find_element(LocatorsOrder.PHONE_FILED)
        address_filed.send_keys(phone)

    @allure.step("Выбор даты заказа самоката")
    def set_date(self, date):
        date_field = self.wait_and_find_element(LocatorsOrder.DATE_FIELD)
        date_field.send_keys(date)
        self.click_element_by_locator(LocatorsOrder.RENT_TITLE)

    @allure.step("Выбор периода аренды")
    def set_rental_period(self, rental_option):
        self.click_element_by_locator(LocatorsOrder.RENTAL_PERIOD_FIELD)
        self.click_element_by_locator(LocatorsOrder.get_locator_rental_option(rental_option))

    @allure.step("Шаг объединения методов заполнения полей заказа")
    def set_all_fields(self, name, surname, address, metro_option, phone):
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.set_metro(metro_option)
        self.set_phone(phone)

    @allure.step("Переход на вторую страницу создания заказа")
    def go_to_second_order_page(self):
        self.js_click_element_by_locator(LocatorsOrder.NEXT_BUTTON)

    @allure.step("Подтвердить заказ")
    def confirm_order(self):
        self.js_click_element_by_locator(LocatorsOrder.ORDER_BUTTON_IN_ORDER)
        self.js_click_element_by_locator(LocatorsOrder.BUTTON_YES)

    @allure.step("Проверка успешно созданного заказа")
    def is_success_order(self):
        return self.wait_and_find_element(LocatorsOrder.SUCCESS_ORDER) is not None

    @allure.step("Перейти к просмотру статуса заказа")
    def go_to_order_status(self):
        self.js_click_element_by_locator(LocatorsOrder.VIEW_STATUS_BUTTON)

    @allure.step("Нажать на лого самоката")
    def click_scooter_logo(self):
        self.js_click_element_by_locator(LocatorsOrder.LOGO_SCOOTER)

    @allure.step("Нажать на лого Яндекс")
    def click_yandex_logo(self):
        self.js_click_element_by_locator(LocatorsOrder.LOGO_YANDEX)


