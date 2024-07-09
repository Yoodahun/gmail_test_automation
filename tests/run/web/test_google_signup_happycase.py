from tests.suite.suite_gmail_signup import SuiteGmailSignUp
from src.web.pages.gmail_home_page import GmailHomePage
from src.base.google_login_page import GoogleLoginPage
from src.base.google_signup_page import GoogleSignUpPage

class TestGoogleSignUpHappyCase:
    def test_google_sign_up_happycase(self):
        """
        보안문자 입력화면까지 가는 기본 happy test입니다.
        각 step별로 assert가 있습니다.

        """
        google_home_page = GmailHomePage(self.driver)
        google_login_page = GoogleLoginPage(self.driver)
        google_signup_page = GoogleSignUpPage(self.driver)
        base_testsuite = SuiteGmailSignUp(self.driver, google_home_page, google_login_page, google_signup_page)

        base_testsuite.step_check_home_image_and_click_login_button()
        base_testsuite.step_check_login_page_and_click_create_account_button()
        base_testsuite.step_check_and_input_name()
        base_testsuite.step_check_and_input_birthday_and_gender()
        base_testsuite.step_check_and_create_mail_address()
        base_testsuite.step_check_and_create_password()
        base_testsuite.step_check_phone_number_verification_title()

