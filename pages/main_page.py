import allure
from locators.locators_main_page import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step("Получение ответа на вопрос")
    def click_question_and_get_answer(self, question_number):
        self.js_click_element_by_locator(MainPageLocators.get_question_locator(question_number))
        answer_element = self.wait_and_find_element(MainPageLocators.get_answer_locator(question_number))
        return answer_element.text
