import requests
from requests import Response

from constants import Constants
from modules.common_models import OtpSuccessfulResponse
from modules.otp_request.model import OtpRequest
from modules.validator import Validator
from common.deco import logging as log


class VerifyOtpApi(Validator):
    def __init__(self, app):
        self.app = app

    POST_VERIFY_OTP = "/auth/verify-otp"

    @log("Sending OTP request")
    def verify_otp(self,
                   data: OtpRequest,
                   type_response=OtpSuccessfulResponse) -> Response:
        response = requests.post(
            f'https://{Constants.key}@{self.app.url}{self.POST_VERIFY_OTP}', json=data.to_dict())
        return self.structure(response, type_response=type_response)
