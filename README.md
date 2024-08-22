# Проект автоматизации тестирования сервиса Самокат

1. Основа для написания автотестов — фреймворк pytest и инструмент для автоматизации действий веб-браузера Selenium.
2. Подготовка отчетов тестирования выполнена с помощью фреймворка Allure.
3. Установить зависимости — pip install -r requirements.txt.
4. Команда для запуска тестов — pytest -v.
5. Команда для формирования Allure-отчета — pytest --alluredir=allure_results.
6. Команда для формирования отчета в виде web-страницы — allure serve allure_results.

## Описание файлов с тестами
### В папке locators два файла locators_main_page.py и locators_order_page.py 
* locators_main_page.py - локаторы для главной страницы 
* locators_order_page.py -  локаторы для страницы заказа

### В папке pages файлы base_page.py, main_page.py и order_page.py
#### base_page.py (прототип страниц):
* wait_and_find_element - ожидание элемента на странице и возвращение этого элемента
* wait_text_and_find_element - ожидание элемента с нужным текстом и возвращение этого элемента
* open_page - открывает страницу по переданному адресу
* js_click_element_by_locator - клик по элементу с помощью JavaScript
* click_element_by_locator - клик по элементу
* is_current_url_contains - проверка, содержит ли текущий url подстроку
* choose_second_tab - переход на вторую вкладку

### В папке tests файлы test_click_lists_base_page.py и test_order_scooter.py
#### test_click_lists_base_page.py (проверка "Вопросы о важном")
* test_click_and_text_element - проверка соответствия ответа вопросу

#### test_order_scooter.py (проверка заказа самоката и перехода по страницам через логотипы)
* test_success_order - проверка оформления заказа самоката
* test_go_to_scooter - проверка перехода со страницы заказа на главную страницу
* test_go_to_dzen - проверка перехода с главной страницы на Дзен

## Описание вспомогательных файлов
* В файле conftest.py - используемые фикстуры
* В файле data.py - данные для оформления заказа
