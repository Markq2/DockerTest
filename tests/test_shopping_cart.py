import allure
import pytest

from data.data import PlacingOrderData
from data.locators import PlacingAnOrderLocators, ShoppingCartLocators
from pages.shopping_cart_page import ShoppingCartPage


@pytest.mark.run(order=3)
@pytest.mark.shopping_cart_tests(scope='class', autouse=True)
@allure.feature('Тесты добавления продукта в корзину и оформления заказа.')
class TestShoppingCart():

    main_page_url = 'https://www.demoblaze.com/'

    @pytest.mark.parametrize('category_locator, product_locator',
                             [PlacingAnOrderLocators.laptop_locators,
                              PlacingAnOrderLocators.phone_locators,
                              PlacingAnOrderLocators.monitor_locators])
    @pytest.mark.add_product_cart_test()
    @allure.story('Тест добавления продуктов в корзину.')
    def test_add_product_cart(self,
                              browser,
                              category_locator,
                              product_locator):
        page = ShoppingCartPage(browser, self.main_page_url)
        page.open_page()
        page.add_product_cart(category_locator, product_locator)
        page.is_alert_message_present(
            PlacingOrderData.added_message)

    @pytest.mark.add_shopping_cart_test()
    @allure.story('Тест оформления заказа.')
    def test_shopping_cart(self, browser):
        page = ShoppingCartPage(browser, self.main_page_url)
        page.open_page()
        page.add_shopping_cart()
        page.should_be_product_in_cart(*ShoppingCartLocators.product_title)
        page.placing_order(PlacingOrderData.place_orsder_informations)
