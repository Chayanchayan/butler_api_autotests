import pytest
import testit

import constants
from modules.common_models import OtpSuccessfulResponse, OtpErrorResponse
from modules.otp_request.model import OtpRequest


class TestOtpRequest:
    @testit.workItemIds(34375)
    def test_otp_request_with_valid_email(self, app):
        """
        1. Send request with valid email
        2. Check status code is 200
        3. Check response body is equal to model
        """
        data = OtpRequest.send_request_with_valid_email()
        res = app.otp_request_page.request_otp(data=data, type_response=OtpSuccessfulResponse)
        assert res.status_code == 200, "Check status code"

    @testit.workItemIds(34377)
    def test_otp_request_with_invalid_valid(self, app):
        """
        1. Send request with invalid email
        2. Check status code is 422
        3. Check response body has suitable error message
        """
        data = OtpRequest.send_request_with_invalid_email()
        res = app.otp_request_page.request_otp(data=data, type_response=OtpErrorResponse)
        assert res.status_code == 422, "Check status code"
        assert constants.TestData.INVALID_DOMAIN_NAME_TEXT in res.text

    @testit.workItemIds(34511)
    @pytest.mark.parametrize("field", ["recipient"])
    def test_otp_request_with_short_recipient_mailbox(self, app, field):
        """
        1. Send request with short recipient mailbox
        2. Check status code is 422
        3. Check response body has suitable error message
        """
        data = OtpRequest.send_request_with_valid_email()
        setattr(data, field, "")
        res = app.otp_request_page.request_otp(data=data, type_response=OtpErrorResponse)
        assert res.status_code == 422, "Check status code"
        assert constants.TestData.SHORT_MAILBOX_NAME_TEXT in res.text

    @testit.workItemIds(34379)
    @pytest.mark.parametrize("field", ["recipient"])
    def test_otp_request_with_empty_recipient(self, app, field):
        """
        1. Send request with empty recipient
        2. Check status code is 422
        3. Check response body has suitable error message
        """
        data = OtpRequest.send_request_with_valid_email()
        setattr(data, field, None)
        res = app.otp_request_page.request_otp(data=data, type_response=OtpErrorResponse)
        assert res.status_code == 422, "Check status code"
        assert constants.TestData.MISSING_RECIPIENT_TEXT in res.text

    @testit.workItemIds(34380)
    @pytest.mark.parametrize("field", ["factor"])
    def test_otp_request_with_empty_factor(self, app, field):
        """
        1. Send request with empty factor
        2. Check status code is 422
        3. Check response body has suitable error message
        """
        data = OtpRequest.send_request_with_valid_email()
        setattr(data, field, None)
        res = app.otp_request_page.request_otp(data=data, type_response=OtpErrorResponse)
        assert res.status_code == 422, "Check status code"
        assert constants.TestData.MISSING_FACTOR_TEXT in res.text
