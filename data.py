from locators.locators_order_page import LocatorsOrder


class URLS:
    MAIN_PAGE = 'https://qa-scooter.praktikum-services.ru/'
    ORDER_PAGE = 'https://qa-scooter.praktikum-services.ru/order'
    DZEN_PAGE = 'https://dzen.ru/'


class DatasOrder:
    parameters = 'locator_button, name, surname, address, metro_option, phone, date, rental_option'
    values = [
        [LocatorsOrder.UP_ORDER_BUTTON, 'Иван', 'Иванов', 'ул. Пушкина', '2', '12345678912', '27.08.2024', '2'],
        [LocatorsOrder.UNDER_ORDER_BUTTON, 'Петр', 'Петров', 'ул. Маяковского', '4', '98765432113', '28.08.2024', '3']
    ]


class DataForField:
    NAME = 'Имя'
    SURNAME = 'Фамилия'
    ADRESS = 'Адрес'
    METRO_OPTION = '3'
    PHONE = '12345678965'
    DATE = '29.08.24'
    RENTAL_OPTION = '2'
