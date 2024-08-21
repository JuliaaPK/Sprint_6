from locators.order_page_locators import ButtonsOrder
from pages.base_page import BasePage


class OrderPage(BasePage):

    def set_name(self, name):
        name_field = self.wait_and_find_element(ButtonsOrder.NAME_FIELD)
        name_field.send_keys(name)

    def set_surname(self, surname):
        surname_field = self.wait_and_find_element(ButtonsOrder.SURNAME_FIELD)
        surname_field.send_keys(surname)

    def set_address(self, address):
        address_filed = self.wait_and_find_element(ButtonsOrder.ADDRESS_FIELD)
        address_filed.send_keys(address)

    def set_metro(self, metro_option):
        self.click_element_by_locator(ButtonsOrder.METRO_FIELD)
        self.click_element_by_locator(ButtonsOrder.get_metro_option(metro_option))

    def set_phone(self, phone):
        address_filed = self.wait_and_find_element(ButtonsOrder.PHONE_FILED)
        address_filed.send_keys(phone)

    def set_date(self, date):
        date_field = self.wait_and_find_element(ButtonsOrder.DATE_FIELD)
        date_field.send_keys(date)
        self.click_element_by_locator(ButtonsOrder.RENT_TITLE)

    def set_rental_period(self, rental_option):
        self.click_element_by_locator(ButtonsOrder.RENTAL_PERIOD_FIELD)
        self.click_element_by_locator(ButtonsOrder.get_locator_rental_option(rental_option))

    def set_all_fields(self, name, surname, address, metro_option, phone):
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.set_metro(metro_option)
        self.set_phone(phone)
