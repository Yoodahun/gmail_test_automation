import time
import allure
import pytest
from allure_commons.types import AttachmentType

from utilities import driver_factory
from selenium.webdriver.remote import webdriver
from typing import Dict, Tuple

_test_failed_incremental: Dict[str, Dict[Tuple[int, ...], str]] = {}


def pytest_addoption(parser):
    """
    pytest 실행 시에 commandLine option을 설정합니다.
    :param parser:
    :return:
    """
    parser.addoption(
        "--platform", default="web", action="store", help="web/android"
    )


@pytest.fixture(scope="function", autouse=True)
def setup_and_teardown(request) -> webdriver:
    """
    driver 객체를 생성하고, 삭제합니다.
    class 단위로 실행되며, request 객체에 드라이버를 저장하여, 필요 시 request 객체에서 꺼내사용할 수 있습니다.
    :param request:
    :return:
    """

    platform = request.config.getoption('platform').lower()

    driver = driver_factory(platform)

    if platform == "web":
        driver.get("https://www.google.com/intl/ko/gmail/about/")

    request.cls.driver = driver

    if platform == "android":
        time.sleep(3)

    yield

    driver.quit()
    driver = None
    time.sleep(1)


def pytest_runtest_makereport(item, call):
    """
    테스트가 실패했을 시에 리포트에 캡쳐를 첨부하도록 합니다.
    https://docs.pytest.org/en/7.1.x/example/simple.html?highlight=test_failed_incremental#incremental-testing-test-steps
    :param item:
    :param call:
    :return:
    """
    if call.excinfo is not None:
        # the test has failed
        # retrieve the class name of the test
        cls_name = str(item.cls)
        # retrieve the index of the test (if parametrize is used in combination with incremental)
        parametrize_index = (
            tuple(item.callspec.indices.values())
            if hasattr(item, "callspec")
            else ()
        )
        # retrieve the name of the test function
        test_name = item.originalname or item.name
        # store in _test_failed_incremental the original name of the failed test
        _test_failed_incremental.setdefault(cls_name, {}).setdefault(
            parametrize_index, test_name
        )
        allure.attach(
            item.cls.driver.get_screenshot_as_png(),
            "Screenshot",
            attachment_type=AttachmentType.PNG
        )
