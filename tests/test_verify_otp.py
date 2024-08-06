import pytest
import testit

import constants
from modules.common_models import OtpErrorResponse
from modules.verify_otp.model import VerifyOtp


class TestVerifyOtp:
    @testit.workItemIds(34382)
    def test_verify_otp_with_invalid_email(self, app):
        """
        1. Send request with invalid email
        2. Check status code is 422
        3. Check response body has suitable error message
        """
        data = VerifyOtp.verify_otp_with_invalid_email()
        res = app.verify_otp_page.verify_otp(data=data, type_response=OtpErrorResponse)
        assert res.status_code == 422, "Check status code"
        assert constants.TestData.INVALID_DOMAIN_NAME_TEXT in res.text

    @testit.workItemIds(34384)
    @pytest.mark.parametrize("field", ["recipient"])
    def test_verify_otp_with_empty_recipient(self, app, field):
        """
        1. Send request with empty recipient
        2. Check status code is 422
        3. Check response body has suitable error message
        """
        data = VerifyOtp.verify_otp_with_valid_email()
        setattr(data, field, None)
        res = app.verify_otp_page.verify_otp(data=data, type_response=OtpErrorResponse)
        assert res.status_code == 422, "Check status code"
        assert constants.TestData.MISSING_RECIPIENT_TEXT in res.text

    @testit.workItemIds(34385)
    @pytest.mark.parametrize("field", ["factor"])
    def test_verify_otp_with_empty_factor(self, app, field):
        """
        1. Send request with empty factor
        2. Check status code is 422
        3. Check response body has suitable error message
        """
        data = VerifyOtp.verify_otp_with_valid_email()
        setattr(data, field, None)
        res = app.verify_otp_page.verify_otp(data=data, type_response=OtpErrorResponse)
        assert res.status_code == 422, "Check status code"
        assert constants.TestData.MISSING_FACTOR_TEXT in res.text

    @testit.workItemIds(34390)
    def test_verify_otp_with_invalid_code(self, app):
        """
        1. Send request with invalid code
        2. Check status code is 422
        3. Check response body has suitable error message
        """
        data = VerifyOtp.verify_otp_with_invalid_code()
        res = app.verify_otp_page.verify_otp(data=data, type_response=OtpErrorResponse)
        assert res.status_code == 422, "Check status code"
        assert constants.TestData.INVALID_VERIFICATION_CODE_TEXT in res.text
