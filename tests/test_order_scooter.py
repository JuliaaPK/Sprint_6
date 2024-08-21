import allure
import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import URLS, DatasOrder, DataForField
from locators.locators_base_page import BasePageLocators
from locators.order_page_locators import ButtonsOrder
from pages.order_page import OrderPage


class TestOrderScooter:
    @allure.title('Проверка заказа')
    @allure.description('Заполняем форму заказа и проверяем, что заказ создан успешно ')
    @pytest.mark.parametrize(DatasOrder.parameters, DatasOrder.values)
    def test_success_order(self, driver, locator_button, name, surname, address, metro_option, phone, date, rental_option):
        order_page = OrderPage(driver)
        order_page.open_page(URLS.MAIN_PAGE)
        order_page.js_click_element_by_locator(locator_button)
        order_page.wait_and_find_element(ButtonsOrder.NAME_FIELD)
        order_page.set_all_fields(name, surname, address, metro_option, phone)
        order_page.js_click_element_by_locator(ButtonsOrder.NEXT_BUTTON)
        order_page.wait_and_find_element(ButtonsOrder.DATE_FIELD)
        order_page.set_date(date)
        order_page.set_rental_period(rental_option)
        order_page.js_click_element_by_locator(ButtonsOrder.ORDER_BUTTON_IN_ORDER)
        order_page.js_click_element_by_locator(ButtonsOrder.BUTTON_YES)
        see_status_button = order_page.wait_and_find_element(ButtonsOrder.SUCCESS_ORDER)

        assert see_status_button.text == 'Посмотреть статус'

    @allure.title('Проверка перехода на главную страницу "Самокат"')
    @allure.description('Переходим из окна заказанного самоката на главную страницу через логотип "Самокат"')
    def test_go_to_scooter(self, driver):
        order_page = OrderPage(driver)
        order_page.open_page(URLS.MAIN_PAGE)
        order_page.js_click_element_by_locator(ButtonsOrder.UP_ORDER_BUTTON)
        order_page.wait_and_find_element(ButtonsOrder.NAME_FIELD)
        order_page.set_all_fields(DataForField.NAME, DataForField.SURNAME, DataForField.ADRESS, DataForField.METRO_OPTION, DataForField.PHONE)
        order_page.js_click_element_by_locator(ButtonsOrder.NEXT_BUTTON)
        order_page.wait_and_find_element(ButtonsOrder.DATE_FIELD)
        order_page.set_date(DataForField.DATE)
        order_page.set_rental_period(DataForField.RENTAL_OPTION)
        order_page.js_click_element_by_locator(ButtonsOrder.ORDER_BUTTON_IN_ORDER)
        order_page.js_click_element_by_locator(ButtonsOrder.BUTTON_YES)
        order_page.js_click_element_by_locator(ButtonsOrder.SUCCESS_ORDER)
        order_page.js_click_element_by_locator(ButtonsOrder.LOGO_SCOOTER)
        about_important_text = order_page.wait_and_find_element(BasePageLocators.IMPORTANT_QUESTION)

        assert about_important_text.text == 'Вопросы о важном'

    @allure.title('Проверка перехода на главуню страницу "Дзен"')
    @allure.description('Переходим из окна главной страницы "Самоката" на главную страницу "Дзена" через логотип Дзен')
    def test_go_to_dzen(self, driver):
        order_page = OrderPage(driver)
        order_page.open_page(URLS.MAIN_PAGE)
        order_page.js_click_element_by_locator(ButtonsOrder.UP_ORDER_BUTTON)
        order_page.wait_and_find_element(ButtonsOrder.NAME_FIELD)
        order_page.set_all_fields(DataForField.NAME, DataForField.SURNAME, DataForField.ADRESS, DataForField.METRO_OPTION,
                                  DataForField.PHONE)
        order_page.js_click_element_by_locator(ButtonsOrder.NEXT_BUTTON)
        order_page.wait_and_find_element(ButtonsOrder.DATE_FIELD)
        order_page.set_date(DataForField.DATE)
        order_page.set_rental_period(DataForField.RENTAL_OPTION)
        order_page.js_click_element_by_locator(ButtonsOrder.ORDER_BUTTON_IN_ORDER)
        order_page.js_click_element_by_locator(ButtonsOrder.BUTTON_YES)
        order_page.js_click_element_by_locator(ButtonsOrder.SUCCESS_ORDER)
        order_page.js_click_element_by_locator(ButtonsOrder.LOGO_SCOOTER)
        order_page.wait_and_find_element(BasePageLocators.IMPORTANT_QUESTION)
        order_page.js_click_element_by_locator(ButtonsOrder.LOGO_YANDEX)
        WebDriverWait(driver, 10).until(expected_conditions.number_of_windows_to_be(2))
        driver.switch_to.window(driver.window_handles[1])
        WebDriverWait(driver, 10).until(expected_conditions.url_contains(URLS.DZEN_PAGE))

        assert URLS.DZEN_PAGE in driver.current_url
