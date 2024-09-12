import requests
from requests import Response

from constants import Constants
from modules.common_models import FactorVerificationSuccessfulResponse
from modules.factor_verification_request.model import FactorVerificationRequest
from modules.validator import Validator
from common.deco import logging as log


class VerifyFactorApi(Validator):
    def __init__(self, app):
        self.app = app

    POST_VERIFY_FACTOR = "/auth/verify-factor"

    @log("Sending Factor request")
    def verify_factor(self,
                      data: FactorVerificationRequest,
                      type_response=FactorVerificationSuccessfulResponse) -> Response:
        response = requests.post(
            f'https://{Constants.key}@{self.app.url}{self.POST_VERIFY_FACTOR}', json=data.to_dict())
        return self.structure(response, type_response=type_response)
