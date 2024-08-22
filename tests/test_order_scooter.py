import allure
import pytest
from data import URLS, DatasOrder, DataForField
from pages.order_page import OrderPage


class TestOrderScooter:
    @allure.title('Проверка заказа')
    @allure.description('Заполняем форму заказа и проверяем, что заказ создан успешно ')
    @pytest.mark.parametrize(DatasOrder.parameters, DatasOrder.values)
    def test_success_order(self, driver, locator_button, name, surname, address, metro_option, phone, date, rental_option):
        order_page = OrderPage(driver)
        order_page.open_page(URLS.MAIN_PAGE)
        order_page.js_click_element_by_locator(locator_button)
        order_page.set_all_fields(name, surname, address, metro_option, phone)
        order_page.go_to_second_order_page()
        order_page.set_date(date)
        order_page.set_rental_period(rental_option)
        order_page.confirm_order()

        assert order_page.is_success_order() is True

    @allure.title('Проверка перехода на главную страницу "Самокат"')
    @allure.description('Переходим из окна заказанного самоката на главную страницу через логотип "Самокат"')
    def test_go_to_scooter(self, driver):
        order_page = OrderPage(driver)
        order_page.open_page(URLS.MAIN_PAGE)
        order_page.go_to_crete_order()
        order_page.set_all_fields(DataForField.NAME, DataForField.SURNAME, DataForField.ADRESS,
                                  DataForField.METRO_OPTION, DataForField.PHONE)
        order_page.go_to_second_order_page()
        order_page.set_date(DataForField.DATE)
        order_page.set_rental_period(DataForField.RENTAL_OPTION)
        order_page.confirm_order()
        order_page.go_to_order_status()
        order_page.click_scooter_logo()

        assert order_page.is_current_url_contains(URLS.MAIN_PAGE) is True

    @allure.title('Проверка перехода на главуню страницу "Дзен"')
    @allure.description('Переходим из окна главной страницы "Самоката" на главную страницу "Дзена" через логотип Дзен')
    def test_go_to_dzen(self, driver):
        order_page = OrderPage(driver)
        order_page.open_page(URLS.MAIN_PAGE)
        order_page.go_to_crete_order()
        order_page.set_all_fields(DataForField.NAME, DataForField.SURNAME, DataForField.ADRESS,
                                  DataForField.METRO_OPTION, DataForField.PHONE)
        order_page.go_to_second_order_page()
        order_page.set_date(DataForField.DATE)
        order_page.set_rental_period(DataForField.RENTAL_OPTION)
        order_page.confirm_order()
        order_page.go_to_order_status()
        order_page.click_scooter_logo()
        order_page.click_yandex_logo()
        order_page.choose_second_tab()

        assert order_page.is_current_url_contains(URLS.DZEN_PAGE) is True
