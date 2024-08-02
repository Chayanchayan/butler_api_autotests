import os


class Constants:
    try:
        key = os.getenv('API_KEY')
    except KeyError:
        print("API KEY wasn't found")


class TestData:
    VALID_EMAIL = "testone+teacher@uchi.ru"
    INVALID_EMAIL = "testone+teacher@uchi"
    FACTOR_EMAIL = "email"
    INVALID_DOMAIN_NAME_TEXT = "Invalid Domain Name"
    SHORT_MAILBOX_NAME_TEXT = "Mailbox name too short"
    MISSING_RECIPIENT_TEXT = "missing parameter for recipient"
    MISSING_FACTOR_TEXT = "missing parameter for factor"
