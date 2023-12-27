from selenium.webdriver.common.by import By


class RegistrationLocators():
    registration_button_novbar = (By.CSS_SELECTOR, '#signin2')
    username = (By.CSS_SELECTOR, '#sign-username')
    password = (By.CSS_SELECTOR, '#sign-password')
    registration_button_modal = (By.XPATH, '//button[text()="Sign up"]')


class LoginLocators():
    login_button_novbar = (By.CSS_SELECTOR, '#login2')
    username = (By.CSS_SELECTOR, '#loginusername')
    password = (By.CSS_SELECTOR, '#loginpassword')
    login_button_modal = (By.XPATH, '//button[text()="Log in"]')


class ContactMessageLocators():
    contact_button = (By.XPATH, '//a[text()="Contact"]')
    recipient_email = (By.CSS_SELECTOR, '#recipient-email')
    recipient_name = (By.CSS_SELECTOR, '#recipient-name')
    recipient_message = (By.CSS_SELECTOR, '#message-text')
    send_meesage_button = (By.XPATH, '//button[text()="Send message"]')


class ShoppingCartLocators():
    add_product_button = (By.XPATH, '//a[text()="Iphone 6 32gb"]')
    add_product_shopping_cart = (By.XPATH, '//a[text()="Add to cart"]')
    cart_button_novbar = (By.XPATH, '//a[text()="Cart"]')
    product_title = (By.XPATH, '//td[text()="Iphone 6 32gb"]')
    place_order_button = (By.XPATH, '//a[text()="Place Order"]')


class PlacingAnOrderLocators():
    phones_categories_button = (By.XPATH, '//a[text()="Phones"]')
    laptops_categories_button = (By.XPATH, '//a[text()="Laptops"]')
    monitors_categories_button = (By.XPATH, '//a[text()="Monitors"]')

    # phone_locator = (By.XPATH, '//a[text()="Samsung galaxy s7"]')
    phone_locator = (By.CSS_SELECTOR, 'a[href="prod.html?idp_=1"]')
    laptop_locator = (By.XPATH, '//a[text()="MacBook Pro"]')
    monitor_locator = (By.XPATH, '//a[text()="ASUS Full HD"]')

    laptop_locators = [laptops_categories_button, laptop_locator]
    phone_locators = [phones_categories_button, phone_locator]
    monitor_locators = [monitors_categories_button, monitor_locator]

    place_order_button = (By.XPATH, '//button[text()="Place Order"]')
    place_order_form = (By.CSS_SELECTOR, '.modal.fade.show form input')
    purchase_button = (By.XPATH, '//button[text()="Purchase"]')
    sweet_alert_message = (By.CSS_SELECTOR, '.sweet-alert h2')
    sweet_alert_button = (By.XPATH, '//button[text()="OK"]')
