import allure
from allure_commons.types import AttachmentType

from data.data import RegistrationData
from data.locators import LoginLocators, RegistrationLocators

from .base_page import BasePage


class RegistrationAndLoginPage(BasePage):
    user_data = []
    fake_user_data = [RegistrationData.username, RegistrationData.password]
    user_data.extend(fake_user_data)
    print(user_data)

    def registration_new_user(self):
        """Функция регистрации нового пользователя"""
        with allure.step('Нажаимаем на кнопку регистрации\
                          нового пользователя в navbar.'):
            registration_button_novbar = self.find_element(
                            RegistrationLocators.registration_button_novbar)
            registration_button_novbar.click()

        with allure.step('Заполняем поля username и password.'):
            username_input_field = self.find_element(
                            RegistrationLocators.username)
            username_input_field.send_keys(self.user_data[0])
            password_input_field = self.find_element(
                            RegistrationLocators.password)
            password_input_field.send_keys(self.user_data[1])

        with allure.step('Нажимаем на кнопку регистрации\
                          нового пользователя в модальном окне регистрации.'):
            registration_button_modal = self.find_element(
                            RegistrationLocators.registration_button_modal)
            registration_button_modal.click()

    def login_new_user(self):
        with allure.step('Нажаимаем на кнопку входа в учетную запись\
                          нового пользователя в navbar.'):
            login_button_novbar = self.find_element(
                                    LoginLocators.login_button_novbar)
            login_button_novbar.click()

        with allure.step('Заполняем поля username и password.'):
            user_input_field = self.find_element(LoginLocators.username)
            user_input_field.send_keys(self.user_data[0])
            password_input_field = self.find_element(LoginLocators.password)
            password_input_field.send_keys(self.user_data[1])

        with allure.step('Нажимаем на кнопку входа в учетную запись\
                          нового пользователя в модальном окне регистрации.'):
            login_button_modal = self.find_element(
                                LoginLocators.login_button_modal)
            login_button_modal.click()

    def should_be_login_username(self, *locator):
        '''Проверка наличия имя пользователя, после успешной регистрации'''
        with allure.step('Проверяем, что после успешной\
                         регистрации и входа мы видим имя пользователя.'):
            assert self.is_element_present_timeout(*locator), 'Login name is not presented.'
        with allure.step('Делаем скриншот.'):
            allure.attach(self.browser.get_screenshot_as_png(),
                          name='Screenshot',
                          attachment_type=AttachmentType.PNG)
