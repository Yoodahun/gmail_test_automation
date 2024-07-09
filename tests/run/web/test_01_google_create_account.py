from tests.suite.suite_gmail_signup import SuiteGmailSignUp
from src.web.pages.gmail_home_page import GmailHomePage
from src.base.google_login_page import GoogleLoginPage
from src.base.google_signup_page import GoogleSignUpPage


class Test01GoogleCreateAccount:
    """
    계정만들기 페이지의 테스트를 수행합니다.
    """

    def test_create_account_not_input_name(self):
        """
        아무것도 입력하지 않는 케이스
        """
        google_home_page = GmailHomePage(self.driver)
        google_login_page = GoogleLoginPage(self.driver)
        google_signup_page = GoogleSignUpPage(self.driver)
        base_testsuite = SuiteGmailSignUp(self.driver, google_home_page, google_login_page, google_signup_page)

        base_testsuite.step_check_home_image_and_click_login_button()
        base_testsuite.step_check_login_page_and_click_create_account_button()
        google_signup_page.input_firstname("")
        google_signup_page.input_lastname("")
        google_signup_page.click_next_button()

        assert google_signup_page.check_name_error_message("이름을 입력하세요.")

    def test_create_account_space_first_name(self):
        """
        이름 란에 공백을 넣는 케이스
        """
        google_home_page = GmailHomePage(self.driver)
        google_login_page = GoogleLoginPage(self.driver)
        google_signup_page = GoogleSignUpPage(self.driver)
        base_testsuite = SuiteGmailSignUp(self.driver, google_home_page, google_login_page, google_signup_page)

        base_testsuite.step_check_home_image_and_click_login_button()
        base_testsuite.step_check_login_page_and_click_create_account_button()
        google_signup_page.input_firstname(" ")
        google_signup_page.input_lastname("")
        google_signup_page.click_next_button()

        assert google_signup_page.check_name_error_message("이름을 입력하세요.")

    def test_create_account_space_between_character_first_name(self):
        """
        성과 이름 사이에 공백을 넣는 케이스
        """
        google_home_page = GmailHomePage(self.driver)
        google_login_page = GoogleLoginPage(self.driver)
        google_signup_page = GoogleSignUpPage(self.driver)
        base_testsuite = SuiteGmailSignUp(self.driver, google_home_page, google_login_page, google_signup_page)

        base_testsuite.step_check_home_image_and_click_login_button()
        base_testsuite.step_check_login_page_and_click_create_account_button()
        google_signup_page.input_firstname("유 다훈")
        google_signup_page.input_lastname("다 훈")
        google_signup_page.click_next_button()

        assert not google_signup_page.check_name_error_message("이름을 정확하게")

    def test_create_account_special_character_first_name(self):
        """
        이름란에 특수문자를 넣는 케이스
        """
        google_home_page = GmailHomePage(self.driver)
        google_login_page = GoogleLoginPage(self.driver)
        google_signup_page = GoogleSignUpPage(self.driver)
        base_testsuite = SuiteGmailSignUp(self.driver, google_home_page, google_login_page, google_signup_page)

        base_testsuite.step_check_home_image_and_click_login_button()
        base_testsuite.step_check_login_page_and_click_create_account_button()
        google_signup_page.input_firstname("!@#$")
        google_signup_page.input_lastname("")
        google_signup_page.click_next_button()

        assert google_signup_page.check_name_error_message("이름을 정확하게")

    def test_create_account_number_first_name(self):
        """
        이름란에 숫자를 넣는 케이스
        """
        google_home_page = GmailHomePage(self.driver)
        google_login_page = GoogleLoginPage(self.driver)
        google_signup_page = GoogleSignUpPage(self.driver)
        base_testsuite = SuiteGmailSignUp(self.driver, google_home_page, google_login_page, google_signup_page)

        base_testsuite.step_check_home_image_and_click_login_button()
        base_testsuite.step_check_login_page_and_click_create_account_button()
        google_signup_page.input_firstname("1234")
        google_signup_page.input_lastname("")
        google_signup_page.click_next_button()

        assert not google_signup_page.check_name_error_message("이름을 정확하게")

    def test_create_account_character_and_number_first_name_1(self):
        """
        이름란에 문자와 숫자를 넣는 케이스
        """
        google_home_page = GmailHomePage(self.driver)
        google_login_page = GoogleLoginPage(self.driver)
        google_signup_page = GoogleSignUpPage(self.driver)
        base_testsuite = SuiteGmailSignUp(self.driver, google_home_page, google_login_page, google_signup_page)

        base_testsuite.step_check_home_image_and_click_login_button()
        base_testsuite.step_check_login_page_and_click_create_account_button()
        google_signup_page.input_firstname("유14")
        google_signup_page.input_lastname("")
        google_signup_page.click_next_button()

        assert not google_signup_page.check_name_error_message("이름을 정확하게")

    def test_create_account_character_and_number_first_name_2(self):
        """
        이름란에 문자-숫자-문자 넣는 케이스
        """
        google_home_page = GmailHomePage(self.driver)
        google_login_page = GoogleLoginPage(self.driver)
        google_signup_page = GoogleSignUpPage(self.driver)
        base_testsuite = SuiteGmailSignUp(self.driver, google_home_page, google_login_page, google_signup_page)

        base_testsuite.step_check_home_image_and_click_login_button()
        base_testsuite.step_check_login_page_and_click_create_account_button()
        google_signup_page.input_firstname("유14다훈")
        google_signup_page.input_lastname("")
        google_signup_page.click_next_button()

        assert not google_signup_page.check_name_error_message("이름을 정확하게")

    def test_create_account_special_character_lastname_and_character_firstname(self):
        """
        성 란에 특수문자, 이름란에 문자를 넣는 케이스
        """
        google_home_page = GmailHomePage(self.driver)
        google_login_page = GoogleLoginPage(self.driver)
        google_signup_page = GoogleSignUpPage(self.driver)
        base_testsuite = SuiteGmailSignUp(self.driver, google_home_page, google_login_page, google_signup_page)

        base_testsuite.step_check_home_image_and_click_login_button()
        base_testsuite.step_check_login_page_and_click_create_account_button()
        google_signup_page.input_firstname("유다훈")
        google_signup_page.input_lastname("!@#$")
        google_signup_page.click_next_button()

        assert google_signup_page.check_name_error_message("이름을 정확하게")

    def test_create_account_special_character_lastname_and_number_firstname(self):
        """
        성 란에 특수문자, 이름란에 숫자를 넣는 케이스
        """
        google_home_page = GmailHomePage(self.driver)
        google_login_page = GoogleLoginPage(self.driver)
        google_signup_page = GoogleSignUpPage(self.driver)
        base_testsuite = SuiteGmailSignUp(self.driver, google_home_page, google_login_page, google_signup_page)

        base_testsuite.step_check_home_image_and_click_login_button()
        base_testsuite.step_check_login_page_and_click_create_account_button()
        google_signup_page.input_firstname("1234")
        google_signup_page.input_lastname("!@#$")
        google_signup_page.click_next_button()

        assert google_signup_page.check_name_error_message("이름을 정확하게")
