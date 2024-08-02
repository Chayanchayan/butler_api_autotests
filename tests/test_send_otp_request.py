import pytest

import constants
from modules.otp_request.model import OtpRequest, OtpSuccessfulResponse, OtpErrorResponse


class TestOtpRequest:

    def test_otp_request_with_valid_valid(self, app):
        data = OtpRequest.send_request_with_valid_email()
        res = app.otp_request_page.request_otp(data=data, type_response=OtpSuccessfulResponse)
        assert res.status_code == 200, "Check status code"

    def test_otp_request_with_invalid_valid(self, app):
        data = OtpRequest.send_request_with_invalid_email()
        res = app.otp_request_page.request_otp(data=data, type_response=OtpErrorResponse)
        assert res.status_code == 422, "Check status code"
        assert constants.TestData.INVALID_DOMAIN_NAME_TEXT in res.text

    @pytest.mark.parametrize("field", ["recipient"])
    def test_otp_request_with_short_recipient_mailbox(self, app, field):
        data = OtpRequest.send_request_with_valid_email()
        setattr(data, field, "")
        res = app.otp_request_page.request_otp(data=data, type_response=OtpErrorResponse)
        assert res.status_code == 422, "Check status code"
        assert constants.TestData.SHORT_MAILBOX_NAME_TEXT in res.text

    @pytest.mark.parametrize("field", ["recipient"])
    def test_otp_request_with_empty_recipient(self, app, field):
        data = OtpRequest.send_request_with_valid_email()
        setattr(data, field, None)
        res = app.otp_request_page.request_otp(data=data, type_response=OtpErrorResponse)
        assert res.status_code == 422, "Check status code"
        assert constants.TestData.MISSING_RECIPIENT_TEXT in res.text

    @pytest.mark.parametrize("field", ["factor"])
    def test_otp_request_with_empty_factor(self, app, field):
        data = OtpRequest.send_request_with_valid_email()
        setattr(data, field, None)
        res = app.otp_request_page.request_otp(data=data, type_response=OtpErrorResponse)
        assert res.status_code == 422, "Check status code"
        assert constants.TestData.MISSING_FACTOR_TEXT in res.text
