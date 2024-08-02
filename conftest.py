import logging
import pytest

from modules.app import OtpApp

logger = logging.getLogger("api")


@pytest.fixture(scope="session")
def app(request):
    url = request.config.getoption("--api-url")
    logger.info(f"Start api tests, url is {url}")
    return OtpApp(url)


def pytest_addoption(parser):
    parser.addoption(
        "--api-url",
        action="store",
        help="enter api url",
        default="core-main-auth.stage-uchi.ru",
    ),
