import allure
from allure_commons.types import AttachmentType
from selenium.webdriver import ActionChains

from data.data import PlacingOrderData, ShoppingCartData
from data.locators import PlacingAnOrderLocators, ShoppingCartLocators
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .base_page import BasePage


class ShoppingCartPage(BasePage):

    def add_shopping_cart(self):
        '''Функция добавление продукта в корзину.'''
        with allure.step('Находим нужный нам продукт,\
                         прокручиваем страницу и\
                         открываем страницу с продуктом.'):
            product_button = self.find_element(
                             ShoppingCartLocators.add_product_button)
            ActionChains(self.browser).scroll_to_element(
                                       product_button).perform()
            product_button.click()
        with allure.step('Добавляем продукт в корзину, \
                         нажимая на соответствующую кнопку.'):
            add_cart_button = self.find_element(
                              ShoppingCartLocators.add_product_shopping_cart)
            add_cart_button.click()
            self.is_alert_message_present(ShoppingCartData.add_cart_message)
        with allure.step('Переходим на страницу корзины,\
                         нажимая на кнопку в navbar.'):
            cart_button_novbar = self.find_element(
                                 ShoppingCartLocators.cart_button_novbar)
            cart_button_novbar.click()

    def should_be_product_in_cart(self, *locator):
        '''Проверка наличия продукта в корзине'''
        with allure.step('Проверяем, наличие продукта в корзине.'):
            assert self.is_element_present(
                        *locator), 'Product is not presented'
        with allure.step('Делаем скриншот.'):
            allure.attach(self.browser.get_screenshot_as_png(),
                          name='Screenshot',
                          attachment_type=AttachmentType.PNG)

    def placing_order(self, data):
        '''Функция оформления заказа.'''
        with allure.step('Находясь на странице корзины с\
                         покупками, нажимаем на кнопку оформления заказа.'):
            place_order_button = self.find_element(
                                 PlacingAnOrderLocators.place_order_button)
            place_order_button.click()
        with allure.step('Заполняем форму оформления закза.'):
            form_input_fields = self.find_elements(
                                PlacingAnOrderLocators.place_order_form)
            i = 0
            while i < len(form_input_fields):
                form_input_fields[i].send_keys(data[i])
                i += 1
            purchase_button = self.find_element(
                              PlacingAnOrderLocators.purchase_button)
            purchase_button.click()
        with allure.step('Проверяем, что заказ успешно создан.'):
            sweet_alert = self.find_element(
                          PlacingAnOrderLocators.sweet_alert_message)
            assert sweet_alert.text == PlacingOrderData.sweet_alert_message, 'Что то пошло не так!'
            sweet_alert_button = self.find_element(
                                 PlacingAnOrderLocators.sweet_alert_button)
            sweet_alert_button.click()

    def add_product_cart(self, category_locator, product_locator):
        category_button = self.find_element(category_locator)
        category_button.click()
        ignored_exceptions = (NoSuchElementException,
                              StaleElementReferenceException,)
        WebDriverWait(self.browser,
                      timeout=2,
                      ignored_exceptions=ignored_exceptions).until(
            EC.presence_of_all_elements_located((product_locator)))
        product_button = self.find_element(product_locator)
        product_button.click()
        add_cart_button = self.find_element(
                          ShoppingCartLocators.add_product_shopping_cart)
        add_cart_button.click()
