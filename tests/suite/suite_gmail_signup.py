import time

from selenium.webdriver.remote.webdriver import WebDriver

from src.web.pages.gmail_home_page import GmailHomePage as WebGmailHomePage
from src.web.pages.google_login_page import GoogleLoginPage
from src.web.pages.google_signup_page import GoogleSignUpPage

from typing import Union


class SuiteGmailSignUp:
    """
    구글 회원가입하는 테스트의 test suite입니다.
    플랫폼에 따라 gmail 홈페이지만 다르고, 구글로그인페이지, 구글회원가입페이지는 동일합니다.
    testsuite를 생성할 때 생성자를 통해 의존객체를 주입받습니다.
    """

    def __init__(self, driver: WebDriver, home_page: WebGmailHomePage, google_login_page: GoogleLoginPage, google_signup_page: GoogleSignUpPage):
        self.driver = driver
        self.__home_page = home_page
        self.__google_login_page = google_login_page
        self.__google_signup_page = google_signup_page

    def step_check_home_image_and_click_login_button(self):
        """
        WEB gmail 홈에서 로그인 버튼을 클릭해 로그인화면으로 이동합니다.

        """
        assert self.__home_page.check_home_image_is_displayed()
        self.__home_page.click_login_button()

    def step_check_gmail_home_and_go_login_page_on_mobile_app(self):
        """
        APP Gmail홈에서 계정만들기를 통해 구글 로그인 페이지로 이동합니다.
        :return:
        """
        self.__home_page.go_to_google_login_home()

    def step_check_login_page_and_click_create_account_button(self):
        """
        로그인페이지에서 개인용 계정만들기 페이지로 이동합니다.
        :return:
        """
        assert self.__google_login_page.check_login_page_elements()
        self.__google_login_page.click_create_personal_account_button()

    def step_check_and_input_name(self):
        """
        개인용 계정만들기 페이지로 이동하여 성과 이름을 입력합니다.
        :return:
        """
        assert self.__google_signup_page.check_title_text("Google 계정 만들기")
        assert self.__google_signup_page.check_title_sub_text("이름을 입력하세요.")
        self.__google_signup_page.input_lastname("유다훈")
        self.__google_signup_page.input_firstname("테스트")
        self.__google_signup_page.click_next_button()

    def step_check_and_input_birthday_and_gender(self):
        """
        생년월일과 성별을 입력합니다.

        :return:
        """
        assert self.__google_signup_page.check_title_text("기본 정보")
        assert self.__google_signup_page.check_title_sub_text("생일과 성별을 입력하세요.")
        self.__google_signup_page.input_year("2002")
        self.__google_signup_page.input_month("11")
        self.__google_signup_page.input_day("5")
        self.__google_signup_page.input_gender("남자")

        self.__google_signup_page.click_next_button()

    def step_check_and_create_mail_address(self):
        """
        gmail어드레스를 만듭니다.
        :return:
        """
        assert self.__google_signup_page.check_title_text("Gmail 주소 선택하기")
        assert self.__google_signup_page.check_title_sub_text('Gmail 주소를 선택하거나 새 Gmail 주소를 만드세요.')
        self.__google_signup_page.create_my_gmail_address("portfolio.mail.ydh")
        self.__google_signup_page.click_next_button()

    def step_check_and_create_password(self):
        """
        비밀번호를 만듭니다.
        :return:
        """
        password: str = "1q2w3e4r5t!@"
        assert self.__google_signup_page.check_title_text("안전한 비밀번호 만들기")
        assert self.__google_signup_page.check_title_sub_text('문자, 숫자, 기호를 조합하여 안전한 비밀번호를 만드세요.')
        self.__google_signup_page.input_pasword_and_password_again(password)

        time.sleep(2)
        self.__google_signup_page.click_next_button()

    def step_check_phone_number_verification_title(self):
        """
        휴대폰번호 인증화면인지를 체크합니다.
        :return:
        """
        assert self.__google_signup_page.check_title_text("보안문자 입력")
        time.sleep(2)
