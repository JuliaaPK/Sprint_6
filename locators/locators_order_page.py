from selenium.webdriver.common.by import By


class LocatorsOrder:
    UP_ORDER_BUTTON = [By.XPATH,
                       './/button[@class = "Button_Button__ra12g"]']  # Кнопка "Заказать" в верхней части страницы
    UNDER_ORDER_BUTTON = [By.XPATH,
                          './/button[@class = "Button_Button__ra12g Button_Middle__1CSJM"]']  # Кнопка "Заказать" в нижней части страницы
    NAME_FIELD = [By.XPATH, './/input[@placeholder = "* Имя"]']  # Поле ввода имени
    SURNAME_FIELD = [By.XPATH, './/input[@placeholder = "* Фамилия"]']  # Поле ввода фамилии
    ADDRESS_FIELD = [By.XPATH, './/input[@placeholder = "* Адрес: куда привезти заказ"]']  # Поле ввода адреса
    METRO_FIELD = [By.XPATH, './/input[@placeholder = "* Станция метро"]']  # Поле выбора станции метро
    PHONE_FILED = [By.XPATH,
                   './/input[@placeholder = "* Телефон: на него позвонит курьер"]']  # Поле ввода номер телефона
    NEXT_BUTTON = [By.XPATH,
                   './/button[contains(@class,  "Button_Button") and text()="Далее"]']  # Кнопка "Далее" на странице с формой заказа
    DATE_FIELD = [By.XPATH,
                  './/input[@placeholder = "* Когда привезти самокат"]']  # Поле ввода "Когда привезти самокат"
    RENTAL_PERIOD_FIELD = [By.XPATH, './/div[@class = "Dropdown-root"]']  # Поле выбора времени аренды самоката
    ORDER_BUTTON_IN_ORDER = [By.XPATH,
                             './/button[@class = "Button_Button__ra12g Button_Middle__1CSJM"]']  # Кнопка "Заказать" на странице с формой заказа
    BUTTON_YES = [By.XPATH, './/button[text() = "Да"]']  # Кнопка "Да" на странице с формой заказа
    SUCCESS_ORDER = [By.XPATH, './/div[contains(text() ,"Заказ оформлен")]']  # Текст "Заказ оформлен"
    VIEW_STATUS_BUTTON = [By.XPATH, './/button[text() = "Посмотреть статус"]']  # Кнопка "Посмотреть статус"
    LOGO_SCOOTER = [By.XPATH, './/a[contains(@class, "LogoScooter")]']  # Логотип "Самокат"
    LOGO_YANDEX = [By.XPATH, './/a[contains(@class, "Header_LogoYandex")]']  # Логотип "Яндекс"
    RENT_TITLE = [By.XPATH, './/div[text() = "Про аренду"]']  # Заголовок страницы при оформлении заказа

    # Генерация локаторов для выбора периода времени аренды
    @staticmethod
    def get_locator_rental_option(option):
        return [By.XPATH, f'//div[@class="Dropdown-menu"]/div[{option}]']

    # Генерация локаторов для выбора станции метро
    @staticmethod
    def get_metro_option(option):
        return [By.XPATH, f'.//button[@value = "{option}"]']
