import attr


@attr.s
class OtpSuccessfulResponse:
    failures = attr.ib(default=None, validator=attr.validators.instance_of(int))
    max_attempts = attr.ib(default=None, validator=attr.validators.instance_of(int))
    issued_at = attr.ib(default=None, validator=attr.validators.instance_of(int))
    deadline = attr.ib(default=None, validator=attr.validators.instance_of(int))
    resend_after = attr.ib(default=None, validator=attr.validators.instance_of(int))
    cooldown = attr.ib(default=None, validator=attr.validators.instance_of(int))


@attr.s
class OtpErrorResponse:
    error = attr.ib(default=None, validator=attr.validators.instance_of(str))
    reason = attr.ib(default=None, validator=attr.validators.instance_of(str))


@attr.s
class FactorVerificationSuccessfulResponse:
    failures = attr.ib(default=None, validator=attr.validators.instance_of(int))
    max_attempts = attr.ib(default=None, validator=attr.validators.instance_of(int))
    issued_at = attr.ib(default=None, validator=attr.validators.instance_of(int))
    deadline = attr.ib(default=None, validator=attr.validators.instance_of(int))
    resend_after = attr.ib(default=None, validator=attr.validators.instance_of(int))
    cooldown = attr.ib(default=None, validator=attr.validators.instance_of(int))


@attr.s
class FactorVerificationErrorResponse:
    error = attr.ib(default=None, validator=attr.validators.instance_of(str))
    reason = attr.ib(default=None, validator=attr.validators.instance_of(str))
