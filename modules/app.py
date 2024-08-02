from modules.otp_request.api import OtpRequestApi
from modules.requests import Client


class OtpApp:

    def __init__(self, url):
        self.url = url
        self.client = Client
        self.otp_request_page = OtpRequestApi(self)
