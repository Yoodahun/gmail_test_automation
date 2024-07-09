from src.web.locators.gmail_home_page_locator import GmailHomePageLocator
from src.base_page import BasePage
from selenium.webdriver.remote.webdriver import  WebDriver


class GmailHomePage(BasePage, GmailHomePageLocator):
    """
    Web Gmail 홈페이지에서 구글 로그인 페이지로 이동하는 클래스입니다.
    """

    def __init__(self, driver:WebDriver):
        super().__init__(driver)

    def check_home_image_is_displayed(self)->bool:
        return self._is_visible(self.HOME_IMAGE)

    def click_login_button(self):
        self._click(self.LOGIN_BUTTON)



