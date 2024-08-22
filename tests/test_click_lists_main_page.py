import allure
import pytest
import data
from locators.locators_main_page import QuestionList
from pages.main_page import MainPage


class TestClickList:

    @allure.title('Проверка списка в разделе "Вопросы о важном"')
    @allure.description('Проверяем, что при клике по каждому вопросу открывается на него ответ')
    @pytest.mark.parametrize(QuestionList.parameters, QuestionList.values)
    def test_click_and_text_element(self, driver, question_number, answer_text):
        main_page = MainPage(driver)
        main_page.open_page(data.URLS.MAIN_PAGE)
        answer = main_page.click_question_and_get_answer(question_number)

        assert answer == answer_text
