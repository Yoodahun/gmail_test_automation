import time

from src.android.locators.gmail_login_page_locator import GmailLoginPageLocator
from src.web.locators.google_login_page_locator import GoogleLoginPageLocator
from src.base_page import BasePage


class GoogleLoginPage(BasePage, GoogleLoginPageLocator):
    """
    구글 로그인 페이지입니다.
    생성자에서 platform을 파라미터로 전달받습니다. platform이 web이냐 아니냐에 따라 생성하는 로케이터클래스가 다릅니다.

    """

    def __init__(self, driver, platform: str = "web"):
        super().__init__(driver)
        self.platform = platform
        if platform == "web":
            locator_class_name = "GoogleLoginPageLocator"
            locator_class = globals().get(locator_class_name, None)

            self.locator = locator_class()
        else:
            self.locator = GmailLoginPageLocator()

    def check_login_page_elements(self) -> bool:
        self.logger.info(self.platform)
        self.logger.info(self._get_text(self.locator.LOGIN_PAGE_HEADER_TEXT))
        return self._get_text(self.locator.LOGIN_PAGE_HEADER_TEXT) == "로그인" and self._is_visible(
            self.locator.CREATE_ACCOUNT_BUTTON)

    def click_create_personal_account_button(self):
        self._click(self.locator.CREATE_ACCOUNT_BUTTON)
        self._click(self.locator.CREATE_ACCOUNT_OPTION_PERSONAL)
        time.sleep(1)
