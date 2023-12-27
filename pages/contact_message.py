import allure

from data.data import ContactMessageData
from data.locators import ContactMessageLocators

from .base_page import BasePage


class ContactMessage(BasePage):

    def contact_message(self):
        """Функция отправления сообщения"""
        with allure.step('Нажаимаем на кнопку отправки сообщения\
                        в navbar.'):
            contact_button = self.find_element(
                             ContactMessageLocators.contact_button)
            contact_button.click()

        with allure.step('Заполняем поля username и password.'):
            email_input_field = self.find_element(
                             ContactMessageLocators.recipient_email)
            email_input_field.send_keys(ContactMessageData.email)
            name_input_field = self.find_element(
                             ContactMessageLocators.recipient_name)
            name_input_field.send_keys(ContactMessageData.name)
            message_input_field = self.find_element(
                                  ContactMessageLocators.recipient_message)
            message_input_field.send_keys(ContactMessageData.message)

        with allure.step('Нажимаем кнопку отправки сообщения'):
            send_message_button = self.find_element(
                                  ContactMessageLocators.send_meesage_button)
            send_message_button.click()
