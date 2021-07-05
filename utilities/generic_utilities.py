import os
import random
import string


def generate_a_random_review():
    review_length = 10
    review = ''.join(random.choices(string.ascii_letters + string.digits, k=review_length))
    return review


def generate_a_random_rating():
    return random.randint(0, 5)


def get_appium_server_address():
    address = os.environ.get('APPIUM_SERVER_ADDRESS','http://localhost:4723/wd/hub')
    return address
