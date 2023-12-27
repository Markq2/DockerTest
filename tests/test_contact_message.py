import allure
import pytest

from data.data import ContactMessageData
from pages.contact_message import ContactMessage


@pytest.mark.run(order=2)
@pytest.mark.contact_message_tests(scope='class', autouse=True)
@allure.feature('Тесты формы отправления сообщения.')
class TestContactMessageForm():

    main_page_url = 'https://www.demoblaze.com/'

    @pytest.mark.contact_message_form()
    @allure.story('Тест отправления сообщения с контактами.')
    def test_contact_message_form(self, browser):
        page = ContactMessage(browser, self.main_page_url)
        page.open_page()
        page.contact_message()
        page.is_alert_message_present(
            ContactMessageData.contact_message)
