from faker import Faker
import attr

import constants
from modules.base import BaseClass

fake = Faker()


@attr.s
class OtpRequest(BaseClass):
    recipient: str = attr.ib(default=None)
    factor: str = attr.ib(default=None)

    @staticmethod
    def send_request_with_valid_email():
        return OtpRequest(recipient=constants.TestData.VALID_EMAIL,
                          factor=constants.TestData.FACTOR_EMAIL)

    @staticmethod
    def send_request_with_invalid_email():
        return OtpRequest(recipient=constants.TestData.INVALID_EMAIL,
                          factor=constants.TestData.FACTOR_EMAIL)


@attr.s
class OtpSuccessfulResponse:
    failures = attr.ib(default=None, validator=attr.validators.instance_of(int))
    max_attempts = attr.ib(default=None, validator=attr.validators.instance_of(int))
    issued_at = attr.ib(default=None, validator=attr.validators.instance_of(int))
    deadline = attr.ib(default=None, validator=attr.validators.instance_of(int))
    resend_after = attr.ib(default=None, validator=attr.validators.instance_of(int))
    cooldown = attr.ib(default=None, validator=attr.validators.instance_of(int))


@attr.s
class OtpErrorResponse:
    error = attr.ib(default=None, validator=attr.validators.instance_of(str))
    # field_error = attr.ib(default=None, validator=attr.validators.instance_of(list))
    reason = attr.ib(default=None, validator=attr.validators.instance_of(str))
