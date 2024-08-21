import allure
import pytest
import data
from locators.locators_base_page import LocatorsQuestionList, BasePageLocators
from pages.base_page import BasePage


class TestClickList:

    @allure.title('Проверка списка в разделе "Вопросы о важном"')
    @allure.description('Проверяем, что при клике по каждому вопросу открывается на него ответ')
    @pytest.mark.parametrize(LocatorsQuestionList.parameters, LocatorsQuestionList.values)
    def test_click_and_text_element(self, driver, button_locator, text_locator, element_text):
        base_page = BasePage(driver)
        base_page.open_page(data.URLS.MAIN_PAGE)
        base_page.wait_and_find_element(BasePageLocators.IMPORTANT_QUESTION)
        base_page.js_click_element_by_locator(button_locator)
        answer_element = base_page.wait_and_find_element(text_locator)
        assert answer_element.text == element_text
