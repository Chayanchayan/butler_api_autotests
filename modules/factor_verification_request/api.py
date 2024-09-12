import requests
from requests import Response

from constants import Constants
from modules.common_models import FactorVerificationSuccessfulResponse
from modules.factor_verification_request.model import FactorVerificationRequest
from modules.validator import Validator
from common.deco import logging as log


class FactorVerificationRequestApi(Validator):
    def __init__(self, app):
        self.app = app

    POST_FACTOR_VERIFICATION_REQUEST = "/auth/factor-verification-request"

    @log("Sending Factor request")
    def request_factor_verification(self,
                                    data: FactorVerificationRequest,
                                    type_response=FactorVerificationSuccessfulResponse) -> Response:
        response = requests.post(
            f'https://{Constants.key}@{self.app.url}{self.POST_FACTOR_VERIFICATION_REQUEST}', json=data.to_dict())
        return self.structure(response, type_response=type_response)
