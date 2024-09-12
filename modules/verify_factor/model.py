from faker import Faker
import attr

import constants
from modules.base import BaseClass

fake = Faker()


@attr.s
class VerifyFactor(BaseClass):
    recipient: str = attr.ib(default=None)
    factor: str = attr.ib(default=None)
    code: str = attr.ib(default=None)

    @staticmethod
    def verify_factor_with_valid_email():
        return VerifyFactor(recipient=constants.TestData.VALID_EMAIL,
                            factor=constants.TestData.FACTOR_EMAIL,
                            code=constants.TestData.VERIFICATION_CODE)

    @staticmethod
    def verify_factor_with_invalid_email():
        return VerifyFactor(recipient=constants.TestData.INVALID_EMAIL,
                            factor=constants.TestData.FACTOR_EMAIL,
                            code=constants.TestData.VERIFICATION_CODE)

    @staticmethod
    def verify_factor_with_invalid_code():
        return VerifyFactor(recipient=constants.TestData.VALID_EMAIL,
                            factor=constants.TestData.FACTOR_EMAIL,
                            code=constants.TestData.INVALID_VERIFICATION_CODE)
