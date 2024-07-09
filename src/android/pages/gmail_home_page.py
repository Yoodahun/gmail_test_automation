from src.android.locators.gmail_home_page_locator import GmailHomePageLocator
from src.base_page import BasePage

from appium.webdriver.webdriver import WebDriver


class GmailHomePage(BasePage, GmailHomePageLocator):
    """
    안드로이드 Gmail 앱에서 구글로그인페이지로 이동하는 동안에 노출되는 페이지입니다.
    """

    def __init__(self, driver:WebDriver):
        super().__init__(driver)

    def go_to_google_login_home(self):
        self._click(self.GMAIL_HOME_CONFIRM_BUTTON)
        self._click(self.ADD_NEW_EMAIL_ADDRESS_BUTTON)
        self._click(self.ADD_NEW_GOOGLE_ADDRESS_BUTTON)


