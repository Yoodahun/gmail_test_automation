from tests.suite.suite_gmail_signup import SuiteGmailSignUp
from src.web.pages.gmail_home_page import GmailHomePage
from src.web.pages.google_login_page import GoogleLoginPage
from src.web.pages.google_signup_page import GoogleSignUpPage


class Test03GoogleMailAddress:
    """
    이메일 만들기 화면의 테스트를 수행합니다.
    """

    def test_no_input_address(self):
        """
        아무것도 입력하지 않는 케이스
        """
        google_home_page = GmailHomePage(self.driver)
        google_login_page = GoogleLoginPage(self.driver)
        google_signup_page = GoogleSignUpPage(self.driver)
        base_testsuite = SuiteGmailSignUp(self.driver, google_home_page, google_login_page, google_signup_page)

        base_testsuite.step_check_home_image_and_click_login_button()
        base_testsuite.step_check_login_page_and_click_create_account_button()
        base_testsuite.step_check_and_input_name()
        base_testsuite.step_check_and_input_birthday_and_gender()

        google_signup_page.create_my_gmail_address("")
        google_signup_page.click_next_button()

        assert google_signup_page.check_mail_address_error_message("주소를 입력하세요.")

    def test_input_blank_address(self):
        """
        공백만 입력하는 케이스
        """
        google_home_page = GmailHomePage(self.driver)
        google_login_page = GoogleLoginPage(self.driver)
        google_signup_page = GoogleSignUpPage(self.driver)
        base_testsuite = SuiteGmailSignUp(self.driver, google_home_page, google_login_page, google_signup_page)

        base_testsuite.step_check_home_image_and_click_login_button()
        base_testsuite.step_check_login_page_and_click_create_account_button()
        base_testsuite.step_check_and_input_name()
        base_testsuite.step_check_and_input_birthday_and_gender()

        google_signup_page.create_my_gmail_address(" ")
        google_signup_page.click_next_button()

        assert google_signup_page.check_mail_address_error_message("필수 입력란은 반드시 입력해야 합니다")

    def test_input_special_character_address(self):
        """
        특수문자만 입력하는 케이스
        """
        google_home_page = GmailHomePage(self.driver)
        google_login_page = GoogleLoginPage(self.driver)
        google_signup_page = GoogleSignUpPage(self.driver)
        base_testsuite = SuiteGmailSignUp(self.driver, google_home_page, google_login_page, google_signup_page)

        base_testsuite.step_check_home_image_and_click_login_button()
        base_testsuite.step_check_login_page_and_click_create_account_button()
        base_testsuite.step_check_and_input_name()
        base_testsuite.step_check_and_input_birthday_and_gender()

        google_signup_page.create_my_gmail_address("!@#")
        google_signup_page.click_next_button()

        assert google_signup_page.check_mail_address_error_message("글자(a-z), 숫자(0-9) 및 마침표(.)만 입력할 수 있습니다.")

    def test_input_korean_address(self):
        """
        한글만 입력하는 케이스
        """
        google_home_page = GmailHomePage(self.driver)
        google_login_page = GoogleLoginPage(self.driver)
        google_signup_page = GoogleSignUpPage(self.driver)
        base_testsuite = SuiteGmailSignUp(self.driver, google_home_page, google_login_page, google_signup_page)

        base_testsuite.step_check_home_image_and_click_login_button()
        base_testsuite.step_check_login_page_and_click_create_account_button()
        base_testsuite.step_check_and_input_name()
        base_testsuite.step_check_and_input_birthday_and_gender()

        google_signup_page.create_my_gmail_address("유다훈테스트")
        google_signup_page.click_next_button()

        assert google_signup_page.check_mail_address_error_message("글자(a-z), 숫자(0-9) 및 마침표(.)만 입력할 수 있습니다.")

    def test_input_only_number_address(self):
        """
        숫자만 입력하는 케이스
        """
        google_home_page = GmailHomePage(self.driver)
        google_login_page = GoogleLoginPage(self.driver)
        google_signup_page = GoogleSignUpPage(self.driver)
        base_testsuite = SuiteGmailSignUp(self.driver, google_home_page, google_login_page, google_signup_page)

        base_testsuite.step_check_home_image_and_click_login_button()
        base_testsuite.step_check_login_page_and_click_create_account_button()
        base_testsuite.step_check_and_input_name()
        base_testsuite.step_check_and_input_birthday_and_gender()

        google_signup_page.create_my_gmail_address("19911107")
        google_signup_page.click_next_button()

        assert google_signup_page.check_mail_address_error_message("최소 하나의 알파벳 문자")

    def test_input_under_6_character_address(self):
        """
        6자리 이하의 문자를 입력하는 경우
        """
        google_home_page = GmailHomePage(self.driver)
        google_login_page = GoogleLoginPage(self.driver)
        google_signup_page = GoogleSignUpPage(self.driver)
        base_testsuite = SuiteGmailSignUp(self.driver, google_home_page, google_login_page, google_signup_page)

        base_testsuite.step_check_home_image_and_click_login_button()
        base_testsuite.step_check_login_page_and_click_create_account_button()
        base_testsuite.step_check_and_input_name()
        base_testsuite.step_check_and_input_birthday_and_gender()

        google_signup_page.create_my_gmail_address("04024")
        google_signup_page.click_next_button()

        assert google_signup_page.check_mail_address_error_message("사용자 이름은 6자에서 30자")

    def test_input_just_6_character_address(self):
        """
        딱 6글자를 입력하는 케이스
        """
        google_home_page = GmailHomePage(self.driver)
        google_login_page = GoogleLoginPage(self.driver)
        google_signup_page = GoogleSignUpPage(self.driver)
        base_testsuite = SuiteGmailSignUp(self.driver, google_home_page, google_login_page, google_signup_page)

        base_testsuite.step_check_home_image_and_click_login_button()
        base_testsuite.step_check_login_page_and_click_create_account_button()
        base_testsuite.step_check_and_input_name()
        base_testsuite.step_check_and_input_birthday_and_gender()

        google_signup_page.create_my_gmail_address("04024a")
        google_signup_page.click_next_button()

        assert not google_signup_page.check_mail_address_error_message("사용자 이름은 6자에서 30자")

    def test_input_just_30_character_address(self):
        """
        딱 30글자를 입력하는 케이스
        """
        google_home_page = GmailHomePage(self.driver)
        google_login_page = GoogleLoginPage(self.driver)
        google_signup_page = GoogleSignUpPage(self.driver)
        base_testsuite = SuiteGmailSignUp(self.driver, google_home_page, google_login_page, google_signup_page)

        base_testsuite.step_check_home_image_and_click_login_button()
        base_testsuite.step_check_login_page_and_click_create_account_button()
        base_testsuite.step_check_and_input_name()
        base_testsuite.step_check_and_input_birthday_and_gender()

        google_signup_page.create_my_gmail_address("04024a04024asdsd232145121asdzx")
        google_signup_page.click_next_button()

        assert not google_signup_page.check_mail_address_error_message("사용자 이름은 6자에서 30자")

    def test_input_over_30_character_address(self):
        """
        30글자 넘게 입력하는 케이스
        """
        google_home_page = GmailHomePage(self.driver)
        google_login_page = GoogleLoginPage(self.driver)
        google_signup_page = GoogleSignUpPage(self.driver)
        base_testsuite = SuiteGmailSignUp(self.driver, google_home_page, google_login_page, google_signup_page)

        base_testsuite.step_check_home_image_and_click_login_button()
        base_testsuite.step_check_login_page_and_click_create_account_button()
        base_testsuite.step_check_and_input_name()
        base_testsuite.step_check_and_input_birthday_and_gender()

        google_signup_page.create_my_gmail_address("04024a04024asdsd232145121asdzxsds")
        google_signup_page.click_next_button()

        assert google_signup_page.check_mail_address_error_message("사용자 이름은 6자에서 30자")



    def test_already_use_address(self):
        """
        이미 사용중인 계정
        """
        google_home_page = GmailHomePage(self.driver)
        google_login_page = GoogleLoginPage(self.driver)
        google_signup_page = GoogleSignUpPage(self.driver)
        base_testsuite = SuiteGmailSignUp(self.driver, google_home_page, google_login_page, google_signup_page)

        base_testsuite.step_check_home_image_and_click_login_button()
        base_testsuite.step_check_login_page_and_click_create_account_button()
        base_testsuite.step_check_and_input_name()
        base_testsuite.step_check_and_input_birthday_and_gender()

        google_signup_page.create_my_gmail_address("dahun4032")
        google_signup_page.click_next_button()

        assert google_signup_page.check_mail_address_error_message("이미 사용된 사용자 이름입니다.")

    def test_english_and_special_character_address(self):
        """
        영어와 특수문자 섞인 주소
        """
        google_home_page = GmailHomePage(self.driver)
        google_login_page = GoogleLoginPage(self.driver)
        google_signup_page = GoogleSignUpPage(self.driver)
        base_testsuite = SuiteGmailSignUp(self.driver, google_home_page, google_login_page, google_signup_page)

        base_testsuite.step_check_home_image_and_click_login_button()
        base_testsuite.step_check_login_page_and_click_create_account_button()
        base_testsuite.step_check_and_input_name()
        base_testsuite.step_check_and_input_birthday_and_gender()

        google_signup_page.create_my_gmail_address("dahun4032!^%#$")
        google_signup_page.click_next_button()

        assert google_signup_page.check_mail_address_error_message("글자(a-z), 숫자(0-9) 및 마침표(.)만 입력할 수 있습니다.")

    def test_input_full_mail_address(self):
        """
        도메인이 포함된 풀 주소
        """
        google_home_page = GmailHomePage(self.driver)
        google_login_page = GoogleLoginPage(self.driver)
        google_signup_page = GoogleSignUpPage(self.driver)
        base_testsuite = SuiteGmailSignUp(self.driver, google_home_page, google_login_page, google_signup_page)

        base_testsuite.step_check_home_image_and_click_login_button()
        base_testsuite.step_check_login_page_and_click_create_account_button()
        base_testsuite.step_check_and_input_name()
        base_testsuite.step_check_and_input_birthday_and_gender()

        google_signup_page.create_my_gmail_address("portfolio.mail_ydh@naver.com")
        google_signup_page.click_next_button()

        assert google_signup_page.check_mail_address_error_message("글자(a-z), 숫자(0-9) 및 마침표(.)만 입력할 수 있습니다.")

    def test_input_only_upper_character_address(self):
        """
        전부 대문자만 입력하는 경우
        """
        google_home_page = GmailHomePage(self.driver)
        google_login_page = GoogleLoginPage(self.driver)
        google_signup_page = GoogleSignUpPage(self.driver)
        base_testsuite = SuiteGmailSignUp(self.driver, google_home_page, google_login_page, google_signup_page)

        base_testsuite.step_check_home_image_and_click_login_button()
        base_testsuite.step_check_login_page_and_click_create_account_button()
        base_testsuite.step_check_and_input_name()
        base_testsuite.step_check_and_input_birthday_and_gender()

        google_signup_page.create_my_gmail_address("PORTFOLIOMAIL_ydh")
        google_signup_page.click_next_button()

        assert google_signup_page.check_mail_address_error_message("글자(a-z), 숫자(0-9) 및 마침표(.)만 입력할 수 있습니다.")

    def test_input_upper_and_lower_character_address(self):
        """
        대소문자 섞어서 입력하는 경우
        """
        google_home_page = GmailHomePage(self.driver)
        google_login_page = GoogleLoginPage(self.driver)
        google_signup_page = GoogleSignUpPage(self.driver)
        base_testsuite = SuiteGmailSignUp(self.driver, google_home_page, google_login_page, google_signup_page)

        base_testsuite.step_check_home_image_and_click_login_button()
        base_testsuite.step_check_login_page_and_click_create_account_button()
        base_testsuite.step_check_and_input_name()
        base_testsuite.step_check_and_input_birthday_and_gender()

        google_signup_page.create_my_gmail_address("PORTworkFOLIO_ydh")
        google_signup_page.click_next_button()

        assert google_signup_page.check_mail_address_error_message("글자(a-z), 숫자(0-9) 및 마침표(.)만 입력할 수 있습니다.")

    def test_input_upper_and_number_character_address(self):
        """
        대문자와 숫자를 섞어 입력하는 경우
        """
        google_home_page = GmailHomePage(self.driver)
        google_login_page = GoogleLoginPage(self.driver)
        google_signup_page = GoogleSignUpPage(self.driver)
        base_testsuite = SuiteGmailSignUp(self.driver, google_home_page, google_login_page, google_signup_page)

        base_testsuite.step_check_home_image_and_click_login_button()
        base_testsuite.step_check_login_page_and_click_create_account_button()
        base_testsuite.step_check_and_input_name()
        base_testsuite.step_check_and_input_birthday_and_gender()

        google_signup_page.create_my_gmail_address("PORTFOLIOMAIL12")
        google_signup_page.click_next_button()

        assert not google_signup_page.check_mail_address_error_message("글자(a-z), 숫자(0-9) 및 마침표(.)만 입력할 수 있습니다.")


    def test_input_upper_and_number_and_dot_address(self):
        """
        대문자, 구둣점과 숫자를 섞어 입력하는 경우
        """
        google_home_page = GmailHomePage(self.driver)
        google_login_page = GoogleLoginPage(self.driver)
        google_signup_page = GoogleSignUpPage(self.driver)
        base_testsuite = SuiteGmailSignUp(self.driver, google_home_page, google_login_page, google_signup_page)

        base_testsuite.step_check_home_image_and_click_login_button()
        base_testsuite.step_check_login_page_and_click_create_account_button()
        base_testsuite.step_check_and_input_name()
        base_testsuite.step_check_and_input_birthday_and_gender()

        google_signup_page.create_my_gmail_address("PORTFOLIO.MAIL12")
        google_signup_page.click_next_button()

        assert not google_signup_page.check_mail_address_error_message("글자(a-z), 숫자(0-9) 및 마침표(.)만 입력할 수 있습니다.")