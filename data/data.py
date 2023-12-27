from faker import Faker

fake = Faker()


class RegistrationData():
    sing_up_successful_message = 'Sign up successful.'
    username = fake.user_name()
    password = fake.password()


class ContactMessageData():
    contact_message = 'Thanks for the message!!'
    email = fake.ascii_free_email()
    name = fake.name()
    message = fake.company()


class ShoppingCartData():
    add_cart_message = 'Product added'


class PlacingOrderData():
    added_message = 'Product added'
    place_orsder_informations = [fake.name(),
                                 fake.country(),
                                 fake.city(),
                                 fake.credit_card_number(),
                                 fake.month(),
                                 fake.year()]
    sweet_alert_message = 'Thank you for your purchase!'
