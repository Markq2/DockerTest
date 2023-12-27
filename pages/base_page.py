import allure
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage():
    def __init__(self, browser, url, timeout=1):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open_page(self):
        '''Функция открытия страницы'''
        with allure.step('Открываем главную страницу'):
            self.browser.get(self.url)

    def find_element(self, locator):
        '''Функция поиска элемента.'''
        return self.browser.find_element(*locator)

    def find_elements(self, locator):
        '''Функция поиска всех указанных элемента.'''
        return self.browser.find_elements(*locator)

    def is_alert_message_present(self, allert_message):
        '''Функция проверки появления алерта с соответствующим сообщением.'''
        with allure.step('Проверяем, что появился алерт \
                         с соответствующим сообщением'):
            try:
                WebDriverWait(self.browser, timeout=1).until(
                    EC.alert_is_present(), 'Timed out waiting.')
                sign_up_alert = self.browser.switch_to.alert
                assert sign_up_alert.text == allert_message, f'The message \
                    in the alert box does not match the expected,\
                    {sign_up_alert.text}'
                sign_up_alert.accept()
            except TimeoutException:
                return False
            return True

    def is_element_present(self, how, what):
        '''Функция проверки наличия элемента.'''
        with allure.step('Проверяем наличие нужного нам элемента'):
            try:
                self.browser.find_element(how, what)
            except (NoSuchElementException):
                return False
            return True

    def is_element_present_timeout(self, how, what):
        '''Функция проверки элемента на странице, ожидая.'''
        try:
            WebDriverWait(self.browser, timeout=2).until(
                EC.presence_of_all_elements_located((how, what)))
            # self.browser.find_element(how, what)
        except (TimeoutException):
            return False
        return True
