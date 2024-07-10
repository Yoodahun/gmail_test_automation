from tests.suite.suite_gmail_signup import SuiteGmailSignUp
from src.web.pages.gmail_home_page import GmailHomePage
from src.web.pages.google_login_page import GoogleLoginPage
from src.web.pages.google_signup_page import GoogleSignUpPage


class Test04GooglePassword:
    """
    비밀번호 만들기 화면의 테스트케이스를 생성합니다.
    """
    def test_no_input_password_and_password_again(self):
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
        base_testsuite.step_check_and_create_mail_address()

        assert google_signup_page.check_title_text("안전한 비밀번호 만들기")
        assert google_signup_page.check_title_sub_text("문자, 숫자, 기호를 조합하여 안전한 비밀번호를 만드세요.")

        google_signup_page.input_password("")
        google_signup_page.input_password_again("")
        google_signup_page.click_next_button()

        assert google_signup_page.check_password_error_message("비밀번호를 입력")

    def test_input_password_and_no_password_again(self):
        """
        비밀번호는 입력하지만 비밀번호 확인을 입력하지 않는 케이스
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

        assert google_signup_page.check_title_text("안전한 비밀번호 만들기")
        assert google_signup_page.check_title_sub_text("문자, 숫자, 기호를 조합하여 안전한 비밀번호를 만드세요.")

        google_signup_page.input_password("sadasdsd123231")
        google_signup_page.input_password_again("")
        google_signup_page.click_next_button()

        assert google_signup_page.check_password_error_message("비밀번호 확인")

    def test_no_input_password_and_input_password_again(self):
        """
        비밀번호는 입력하지 않고 비밀번호 확인을 입력하는 케이스
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

        assert google_signup_page.check_title_text("안전한 비밀번호 만들기")
        assert google_signup_page.check_title_sub_text("문자, 숫자, 기호를 조합하여 안전한 비밀번호를 만드세요.")

        google_signup_page.input_password("")
        google_signup_page.input_password_again("sadasdsd123231")
        google_signup_page.click_next_button()

        assert google_signup_page.check_password_error_message("비밀번호를 입력")

    def test_input_password_and_input_different_password_again(self):
        """
        비밀번호와 비밀번호 확인을 다르게 입력하는 경우
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

        assert google_signup_page.check_title_text("안전한 비밀번호 만들기")
        assert google_signup_page.check_title_sub_text("문자, 숫자, 기호를 조합하여 안전한 비밀번호를 만드세요.")

        google_signup_page.input_password("1q2w3e4r5t!")
        google_signup_page.input_password_again("1q2w3e4r5t!!")
        google_signup_page.click_next_button()

        assert google_signup_page.check_password_error_message("비밀번호가 일치하지 않았습니다.")

    def test_input_blank_password_and_input_blank_password_again(self):
        """
        공백을 입력하는 케이스
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

        assert google_signup_page.check_title_text("안전한 비밀번호 만들기")
        assert google_signup_page.check_title_sub_text("문자, 숫자, 기호를 조합하여 안전한 비밀번호를 만드세요.")

        google_signup_page.input_password(" ")
        google_signup_page.input_password_again(" ")
        google_signup_page.click_next_button()

        assert google_signup_page.check_password_error_message("비밀번호는 공백으로 시작하거나 끝날 수 없습니다.")

    def test_input_first_blank_and_character_password_and_password_again(self):
        """
        비밀번호 첫 글자에 공백을 입력하는 경우
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

        assert google_signup_page.check_title_text("안전한 비밀번호 만들기")
        assert google_signup_page.check_title_sub_text("문자, 숫자, 기호를 조합하여 안전한 비밀번호를 만드세요.")

        google_signup_page.input_password(" 1q2w3e4r5t!!")
        google_signup_page.input_password_again(" 1q2w3e4r5t!!")
        google_signup_page.click_next_button()

        assert google_signup_page.check_password_error_message("비밀번호는 공백으로 시작하거나 끝날 수 없습니다.")

    def test_input_one_character_password_and_password_again(self):
        """
        비밀번호와 비밀번호 확인을 한 글자씩 입력하는 경우
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

        assert google_signup_page.check_title_text("안전한 비밀번호 만들기")
        assert google_signup_page.check_title_sub_text("문자, 숫자, 기호를 조합하여 안전한 비밀번호를 만드세요.")

        google_signup_page.input_password("a")
        google_signup_page.input_password_again("a")
        google_signup_page.click_next_button()

        assert google_signup_page.check_password_error_message("비밀번호는 8자 이상")

    def test_input_just_eight_character_password_and_password_again(self):
        """
        비밀번호를 8글자를 입력하는 경우
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

        assert google_signup_page.check_title_text("안전한 비밀번호 만들기")
        assert google_signup_page.check_title_sub_text("문자, 숫자, 기호를 조합하여 안전한 비밀번호를 만드세요.")

        google_signup_page.input_password("homew12!")
        google_signup_page.input_password_again("homew12!")
        google_signup_page.click_next_button()

        assert not google_signup_page.check_password_error_message("비밀번호는 8자 이상")

    def test_input_over_30_character_password_and_password_again(self):
        """
        비밀번호를 30글자를 이상 입력하는 경우
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

        assert google_signup_page.check_title_text("안전한 비밀번호 만들기")
        assert google_signup_page.check_title_sub_text("문자, 숫자, 기호를 조합하여 안전한 비밀번호를 만드세요.")

        google_signup_page.input_password("homew12!homew12!homew12!homew12!homew12!homew12!")
        google_signup_page.input_password_again("homew12!homew12!homew12!homew12!homew12!homew12!")
        google_signup_page.click_next_button()

        assert not google_signup_page.check_password_error_message("비밀번호는 8자 이상")

    def test_just_english_character_password_and_password_again(self):
        """
        비밀번호를 영어만 입력하는 경우
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

        assert google_signup_page.check_title_text("안전한 비밀번호 만들기")
        assert google_signup_page.check_title_sub_text("문자, 숫자, 기호를 조합하여 안전한 비밀번호를 만드세요.")

        google_signup_page.input_password("qwerasdf")
        google_signup_page.input_password_again("qwerasdf")
        google_signup_page.click_next_button()

        assert google_signup_page.check_password_error_message("문자, 숫자, 기호를 조합해 보세요")

    def test_english_and_number_character_password_and_password_again(self):
        """
        비밀번호를 영어와 숫자를 입력하는 경우
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

        assert google_signup_page.check_title_text("안전한 비밀번호 만들기")
        assert google_signup_page.check_title_sub_text("문자, 숫자, 기호를 조합하여 안전한 비밀번호를 만드세요.")

        google_signup_page.input_password("1q2w3e4r5t")
        google_signup_page.input_password_again("1q2w3e4r5t")
        google_signup_page.click_next_button()

        assert google_signup_page.check_password_error_message("문자, 숫자, 기호를 조합해 보세요")

    def test_special_character_and_number_character_password_and_password_again(self):
        """
        비밀번호를 특수문자와 숫자를 입력하는 경우
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

        assert google_signup_page.check_title_text("안전한 비밀번호 만들기")
        assert google_signup_page.check_title_sub_text("문자, 숫자, 기호를 조합하여 안전한 비밀번호를 만드세요.")

        google_signup_page.input_password("123!@#$@!")
        google_signup_page.input_password_again("123!@#$@!")
        google_signup_page.click_next_button()

        assert not google_signup_page.check_password_error_message("문자, 숫자, 기호를 조합해 보세요")

    def test_input_only_number_character_password_and_password_again(self):
        """
        비밀번호를 숫자만 입력하는 경우
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

        assert google_signup_page.check_title_text("안전한 비밀번호 만들기")
        assert google_signup_page.check_title_sub_text("문자, 숫자, 기호를 조합하여 안전한 비밀번호를 만드세요.")

        google_signup_page.input_password("91827842")
        google_signup_page.input_password_again("91827842")
        google_signup_page.click_next_button()

        assert google_signup_page.check_password_error_message("문자, 숫자, 기호를 조합해 보세요")

    def test_input_only_upper_english_character_password_and_password_again(self):
        """
        비밀번호를 대문자 영어만 입력하는 경우
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

        assert google_signup_page.check_title_text("안전한 비밀번호 만들기")
        assert google_signup_page.check_title_sub_text("문자, 숫자, 기호를 조합하여 안전한 비밀번호를 만드세요.")

        google_signup_page.input_password("QWERASDF")
        google_signup_page.input_password_again("QWERASDF")
        google_signup_page.click_next_button()

        assert not google_signup_page.check_password_error_message("문자, 숫자, 기호를 조합해 보세요")

    def test_input_blank_between_character(self):
        """
        문자 사이에 공백이 들어간 경우
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

        assert google_signup_page.check_title_text("안전한 비밀번호 만들기")
        assert google_signup_page.check_title_sub_text("문자, 숫자, 기호를 조합하여 안전한 비밀번호를 만드세요.")

        google_signup_page.input_password("1q2w 345")
        google_signup_page.input_password_again("1q2w 345")
        google_signup_page.click_next_button()


        assert not google_signup_page.check_password_error_message("문자, 숫자, 기호를 조합해 보세요")

    def test_click_check_visible_password_and_check_password_and_password_again(self):
        """
        비밀번호와 비밀번호 확인을 입력 후 비밀번호 표시를 클릭했을 때 내가 입력한 비밀번호들이 동일하게 노출되는지 확인
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

        assert google_signup_page.check_title_text("안전한 비밀번호 만들기")
        assert google_signup_page.check_title_sub_text("문자, 숫자, 기호를 조합하여 안전한 비밀번호를 만드세요.")

        google_signup_page.input_password("1q2w3e4r5t")
        google_signup_page.input_password_again("1q2w3e4r5t")
        google_signup_page.click_view_password()

        assert google_signup_page.get_password() == "1q2w3e4r5t"
        assert google_signup_page.get_password_again_field() == "1q2w3e4r5t"
    #
    def test_click_check_visible_password_and_input_wrong_pattern_password_1(self):
        """
        잘못된 패턴의 비밀번호를 입력 후에 비밀번호 표시클릭 후 다음 버튼을 누르면 입력필드가 클리어되는지 확인
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

        assert google_signup_page.check_title_text("안전한 비밀번호 만들기")
        assert google_signup_page.check_title_sub_text("문자, 숫자, 기호를 조합하여 안전한 비밀번호를 만드세요.")

        google_signup_page.input_password("qwerasdf")
        google_signup_page.input_password_again("qwerasdf")
        google_signup_page.click_view_password()
        google_signup_page.click_next_button()


        assert google_signup_page.get_password() != ""
        assert google_signup_page.get_password() == "qwerasdf"
        assert google_signup_page.get_password_again_field() != ""
        assert google_signup_page.check_password_error_message("문자, 숫자, 기호를 조합해 보세요")

    def test_click_check_visible_password_and_input_wrong_pattern_password_2(self):
        """
        짧은 비밀번호를 입력한 후에 비밀번호 표시를 누르고 다음을 눌렀을 때, 클리어되지 않는 것을 확인
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

        assert google_signup_page.check_title_text("안전한 비밀번호 만들기")
        assert google_signup_page.check_title_sub_text("문자, 숫자, 기호를 조합하여 안전한 비밀번호를 만드세요.")

        google_signup_page.input_password("aa")
        google_signup_page.input_password_again("aa")
        google_signup_page.click_view_password()
        google_signup_page.click_next_button()


        assert google_signup_page.get_password() == "aa"
        assert google_signup_page.get_password_again_field() == "aa"
        assert google_signup_page.check_password_error_message("비밀번호는 8자 이상")

    def test_click_check_visible_password_and_input_wrong_pattern_password_3(self):
        """
        비밀번호와 비밀번호 확인이 일치하지 않을 때, 확인 필드가 클리어되는 것을 확인
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

        assert google_signup_page.check_title_text("안전한 비밀번호 만들기")
        assert google_signup_page.check_title_sub_text("문자, 숫자, 기호를 조합하여 안전한 비밀번호를 만드세요.")

        google_signup_page.input_password("1q2w3e4r5t!!")
        google_signup_page.input_password_again("1q2w3e4r5t!")
        google_signup_page.click_view_password()
        google_signup_page.click_next_button()


        assert google_signup_page.get_password() == "1q2w3e4r5t!!"
        assert google_signup_page.get_password_again_field() != "1q2w3e4r5t!"
        assert google_signup_page.get_password_again_field() == ""
        assert google_signup_page.check_password_error_message("비밀번호가 일치하지 않았습니다.")
    #
