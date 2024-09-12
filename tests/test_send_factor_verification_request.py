import pytest
import testit

import constants
from modules.common_models import FactorVerificationSuccessfulResponse, FactorVerificationErrorResponse
from modules.factor_verification_request.model import FactorVerificationRequest


class TestFactorVerificationRequest:
    @testit.workItemIds(36682)
    def test_factor_verification_request_with_valid_email(self, app):
        """
        1. Send request with valid email
        2. Check status code is 200
        3. Check response body is equal to model
        """
        data = FactorVerificationRequest.send_request_with_valid_email()
        res = app.otp_request_page.request_otp(data=data,
                                               type_response=FactorVerificationSuccessfulResponse)
        assert res.status_code == 200, "Check status code"

    @testit.workItemIds(36683)
    def test_factor_verification_request_with_invalid_email(self, app):
        """
        1. Send request with invalid email
        2. Check status code is 422
        3. Check response body has suitable error message
        """
        data = FactorVerificationRequest.send_request_with_invalid_email()
        res = app.otp_request_page.request_otp(data=data,
                                               type_response=FactorVerificationErrorResponse)
        assert res.status_code == 422, "Check status code"
        assert constants.TestData.INVALID_DOMAIN_NAME_TEXT in res.text

    @testit.workItemIds(36684)
    @pytest.mark.parametrize("field", ["recipient"])
    def test_factor_verification_request_with_empty_recipient(self, app, field):
        """
        1. Send request with empty recipient
        2. Check status code is 422
        3. Check response body has suitable error message
        """
        data = FactorVerificationRequest.send_request_with_valid_email()
        setattr(data, field, None)
        res = app.otp_request_page.request_otp(data=data,
                                               type_response=FactorVerificationErrorResponse)
        assert res.status_code == 422, "Check status code"
        assert constants.TestData.MISSING_RECIPIENT_TEXT in res.text

    @testit.workItemIds(36685)
    @pytest.mark.parametrize("field", ["recipient"])
    def test_factor_verification_request_with_short_recipient_mailbox(self, app, field):
        """
        1. Send request with short recipient mailbox
        2. Check status code is 422
        3. Check response body has suitable error message
        """
        data = FactorVerificationRequest.send_request_with_valid_email()
        setattr(data, field, "")
        res = app.otp_request_page.request_otp(data=data,
                                               type_response=FactorVerificationErrorResponse)
        assert res.status_code == 422, "Check status code"
        assert constants.TestData.SHORT_MAILBOX_NAME_TEXT in res.text

    @testit.workItemIds(36686)
    @pytest.mark.parametrize("field", ["factor"])
    def test_factor_verification_request_with_empty_factor(self, app, field):
        """
        1. Send request with empty factor
        2. Check status code is 422
        3. Check response body has suitable error message
        """
        data = FactorVerificationRequest.send_request_with_valid_email()
        setattr(data, field, None)
        res = app.otp_request_page.request_otp(data=data,
                                               type_response=FactorVerificationErrorResponse)
        assert res.status_code == 422, "Check status code"
        assert constants.TestData.MISSING_FACTOR_TEXT in res.text
