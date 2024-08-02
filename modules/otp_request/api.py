import requests
from requests import Response

from constants import Constants
from modules.otp_request.model import OtpRequest, OtpSuccessfulResponse
from modules.validator import Validator
from common.deco import logging as log


class OtpRequestApi(Validator):
    def __init__(self, app):
        self.app = app

    POST_OTP_REQUEST = "/auth/otp-request"

    @log("Sending OTP request")
    def request_otp(self,
                    data: OtpRequest,
                    type_response=OtpSuccessfulResponse) -> Response:
        response = requests.post(
            f'https://{Constants.key}@{self.app.url}{self.POST_OTP_REQUEST}', json=data.to_dict())
        return self.structure(response, type_response=type_response)
