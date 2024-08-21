from selenium.webdriver.common.by import By


class BasePageLocators:
    IMPORTANT_QUESTION = [By.XPATH, './/div[text()="Вопросы о важном"]'] #Элемент "Вопросы о важном" на главной странице


#Данные списка вопрос-ответ, заданные через параметризацию
class LocatorsQuestionList:

    parameters = 'button_locator, text_locator, element_text '
    values = [
        [(By.XPATH, './/div[@id = "accordion__heading-0"]'), (By.XPATH, './/div[@id = "accordion__panel-0"]/p'), 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'],
        [(By.XPATH, './/div[@id = "accordion__heading-1"]'), (By.XPATH, './/div[@id = "accordion__panel-1"]/p'), 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'],
        [(By.XPATH, './/div[@id = "accordion__heading-2"]'), (By.XPATH, './/div[@id = "accordion__panel-2"]/p'), 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'],
        [(By.XPATH, './/div[@id = "accordion__heading-3"]'), (By.XPATH, './/div[@id = "accordion__panel-3"]/p'), 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'],
        [(By.XPATH, './/div[@id = "accordion__heading-4"]'), (By.XPATH, './/div[@id = "accordion__panel-4"]/p'), 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'],
        [(By.XPATH, './/div[@id = "accordion__heading-5"]'), (By.XPATH, './/div[@id = "accordion__panel-5"]/p'), 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'],
        [(By.XPATH, './/div[@id = "accordion__heading-6"]'), (By.XPATH, './/div[@id = "accordion__panel-6"]/p'), 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'],
        [(By.XPATH, './/div[@id = "accordion__heading-7"]'), (By.XPATH, './/div[@id = "accordion__panel-7"]/p'), 'Да, обязательно. Всем самокатов! И Москве, и Московской области.']

    ]
