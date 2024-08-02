import attr

# from fixtures.base import BaseClass
# from fixtures.register.model import RegisterUser
# from fixtures.user_info.model import AddUserInfo


# @attr.s
# class MessageResponse:
#     message: str = attr.ib()
#
#
# @attr.s
# class UserStore(BaseClass):
#     user: RegisterUser = attr.ib(default=None)
#     user_uuid: int = attr.ib(default=None)
#     header: dict = attr.ib(default=None)
#     user_info: AddUserInfo = attr.ib(default=None)
#     store: str = attr.ib(default=None)
#     store_item: str = attr.ib(default=None)
#     user_balance: int = attr.ib(default=None)
#
#     payment: int = attr.ib(default=None)


@attr.s
class ErrorResponse:
    reason: str = attr.ib()
    field_error: list = attr.ib()
    error: int = attr.ib()
