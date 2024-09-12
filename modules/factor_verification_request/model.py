from faker import Faker
import attr

import constants
from modules.base import BaseClass

fake = Faker()


@attr.s
class FactorVerificationRequest(BaseClass):
    recipient: str = attr.ib(default=None)
    factor: str = attr.ib(default=None)

    @staticmethod
    def send_request_with_valid_email():
        return FactorVerificationRequest(recipient=constants.TestData.VALID_EMAIL,
                                         factor=constants.TestData.FACTOR_EMAIL)

    @staticmethod
    def send_request_with_invalid_email():
        return FactorVerificationRequest(recipient=constants.TestData.INVALID_EMAIL,
                                         factor=constants.TestData.FACTOR_EMAIL)
