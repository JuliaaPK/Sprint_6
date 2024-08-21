from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def wait_and_find_element(self, locator_of_element):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator_of_element))
        return self.driver.find_element(*locator_of_element)

    def wait_text_and_find_element(self, locator_of_element, text):
        WebDriverWait(self.driver, 10).until(expected_conditions.text_to_be_present_in_element(locator_of_element, text))
        return self.driver.find_element(*locator_of_element)

    def open_page(self, url):
        self.driver.get(url)

    def js_click_element_by_locator(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        button = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", button)

    def click_element_by_locator(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        self.driver.find_element(*locator).click()
