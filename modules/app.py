from modules.factor_verification_request.api import FactorVerificationRequestApi
from modules.otp_request.api import OtpRequestApi
from modules.requests import Client
from modules.verify_otp.api import VerifyOtpApi


class ButlerApp:

    def __init__(self, url):
        self.url = url
        self.client = Client
        self.otp_request_page = OtpRequestApi(self)
        self.verify_otp_page = VerifyOtpApi(self)
        self.factor_request_page = FactorVerificationRequestApi(self)
