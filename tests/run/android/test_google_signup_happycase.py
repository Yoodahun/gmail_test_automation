from tests.suite.suite_gmail_signup import SuiteGmailSignUp
from src.android.pages.gmail_home_page import GmailHomePage
from src.base.google_login_page import GoogleLoginPage
from src.base.google_signup_page import GoogleSignUpPage

class TestGoogleSignUpHappyCase:
    def test_google_sign_up_happycase_on_mobile_app(self, request):
        """
        모바일 gmail앱에서 전화번호 설정화면까지 가는 기본 happy test입니다.
        각 step별로 assert가 있습니다.

        """
        gmail_home_page = GmailHomePage(self.driver)
        google_login_page = GoogleLoginPage(self.driver, platform=request.config.getoption('platform').lower())
        google_signup_page = GoogleSignUpPage(self.driver, platform=request.config.getoption('platform').lower())
        base_testsuite = SuiteGmailSignUp(self.driver, gmail_home_page, google_login_page, google_signup_page)

        base_testsuite.step_check_gmail_home_and_go_login_page_on_mobile_app()
        base_testsuite.step_check_login_page_and_click_create_account_button()
        base_testsuite.step_check_and_input_name()
        base_testsuite.step_check_and_input_birthday_and_gender()
        base_testsuite.step_check_and_create_mail_address()
        base_testsuite.step_check_and_create_password()
        base_testsuite.step_check_phone_number_verification_title()
