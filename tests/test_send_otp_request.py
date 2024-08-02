from modules.otp_request.model import OtpRequest, OtpSuccessfulResponse


class TestOtpRequest:

    def test_otp_request_with_valid_data(self, app):

        data = OtpRequest.send_request_with_existing_email()
        res = app.otp_request_page.request_otp(data=data, type_response=OtpSuccessfulResponse)
        assert res.status_code == 200
