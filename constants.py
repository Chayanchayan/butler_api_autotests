import os


class Constants:
    try:
        key = os.getenv('API_KEY')
    except KeyError:
        print("API KEY wasn't found")


class TestData:
    VALID_EMAIL = "testone+teacher@uchi.ru"
    FACTOR_EMAIL = "email"
