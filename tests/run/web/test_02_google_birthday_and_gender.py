from tests.suite.suite_gmail_signup import SuiteGmailSignUp
from src.web.pages.gmail_home_page import GmailHomePage
from src.web.pages.google_login_page import GoogleLoginPage
from src.web.pages.google_signup_page import GoogleSignUpPage


class Test02GoogleBirthdayValidation:
    """
    기본정보 입력페이지에서 날짜에 관한 테스트케이스를 묶어놓았습니다.
    """

    def test_no_input_birthday_and_input_gender(self):
        """
        생년월일은 입력안하고 성별만 입력하는 케이스
        :return:
        """
        google_home_page = GmailHomePage(self.driver)
        google_login_page = GoogleLoginPage(self.driver)
        google_signup_page = GoogleSignUpPage(self.driver)
        base_testsuite = SuiteGmailSignUp(self.driver, google_home_page, google_login_page, google_signup_page)

        base_testsuite.step_check_home_image_and_click_login_button()
        base_testsuite.step_check_login_page_and_click_create_account_button()
        base_testsuite.step_check_and_input_name()

        google_signup_page.check_title_text("기본 정보")
        google_signup_page.check_title_sub_text("생일과 성별을 입력하세요.")
        google_signup_page.input_year("")
        google_signup_page.input_month("")
        google_signup_page.input_day("")
        google_signup_page.input_gender("남자")

        google_signup_page.click_next_button()

        assert google_signup_page.check_date_error_message("정확히 입력해 주세요.")

    def test_no_input_year_and_other_input(self):
        """
        연도만 입력안하고 나머지는 다 입력하는 케이스
        :return:
        """
        google_home_page = GmailHomePage(self.driver)
        google_login_page = GoogleLoginPage(self.driver)
        google_signup_page = GoogleSignUpPage(self.driver)
        base_testsuite = SuiteGmailSignUp(self.driver, google_home_page, google_login_page, google_signup_page)

        base_testsuite.step_check_home_image_and_click_login_button()
        base_testsuite.step_check_login_page_and_click_create_account_button()
        base_testsuite.step_check_and_input_name()

        google_signup_page.check_title_text("기본 정보")
        google_signup_page.check_title_sub_text("생일과 성별을 입력하세요.")
        google_signup_page.input_year("")
        google_signup_page.input_month()
        google_signup_page.input_day()
        google_signup_page.input_gender("남자")

        google_signup_page.click_next_button()

        assert google_signup_page.check_date_error_message("정확히 입력해 주세요.")

    def test_no_input_month_and_other_input(self):
        """
        생년월일 중 월 만 입력안하고 나머지는 다 입력안하는 케이스
        1: ['월', '남자', '없음', '없음']
        :return:
        """
        google_home_page = GmailHomePage(self.driver)
        google_login_page = GoogleLoginPage(self.driver)
        google_signup_page = GoogleSignUpPage(self.driver)
        base_testsuite = SuiteGmailSignUp(self.driver, google_home_page, google_login_page, google_signup_page)

        base_testsuite.step_check_home_image_and_click_login_button()
        base_testsuite.step_check_login_page_and_click_create_account_button()
        base_testsuite.step_check_and_input_name()

        google_signup_page.check_title_text("기본 정보")
        google_signup_page.check_title_sub_text("생일과 성별을 입력하세요.")
        google_signup_page.input_year()
        google_signup_page.input_month("")
        google_signup_page.input_day()
        google_signup_page.input_gender("남자")

        google_signup_page.click_next_button()

        assert google_signup_page.check_date_error_message("정확히 입력해 주세요.")

    def test_no_input_date_and_other_input(self):
        """
        생년월일 중 일만 입력안하고 나머지는 다 입력하는 케이스
        5: ['일', '남자', '없음', '없음']
        :return:
        """
        google_home_page = GmailHomePage(self.driver)
        google_login_page = GoogleLoginPage(self.driver)
        google_signup_page = GoogleSignUpPage(self.driver)
        base_testsuite = SuiteGmailSignUp(self.driver, google_home_page, google_login_page, google_signup_page)

        base_testsuite.step_check_home_image_and_click_login_button()
        base_testsuite.step_check_login_page_and_click_create_account_button()
        base_testsuite.step_check_and_input_name()

        google_signup_page.check_title_text("기본 정보")
        google_signup_page.check_title_sub_text("생일과 성별을 입력하세요.")
        google_signup_page.input_year()
        google_signup_page.input_month()
        google_signup_page.input_day("")
        google_signup_page.input_gender("남자")

        google_signup_page.click_next_button()

        assert google_signup_page.check_date_error_message("정확히 입력해 주세요.")

    def test_input_minus_year_and_other_input(self):
        """
        생년월일 중 연도를 마이너스숫자를 입력안하고 나머지는 다 입력하는 케이스
        :return:
        """
        google_home_page = GmailHomePage(self.driver)
        google_login_page = GoogleLoginPage(self.driver)
        google_signup_page = GoogleSignUpPage(self.driver)
        base_testsuite = SuiteGmailSignUp(self.driver, google_home_page, google_login_page, google_signup_page)

        base_testsuite.step_check_home_image_and_click_login_button()
        base_testsuite.step_check_login_page_and_click_create_account_button()
        base_testsuite.step_check_and_input_name()

        google_signup_page.check_title_text("기본 정보")
        google_signup_page.check_title_sub_text("생일과 성별을 입력하세요.")
        google_signup_page.input_year("-120")
        google_signup_page.input_month()
        google_signup_page.input_day()
        google_signup_page.input_gender("남자")

        google_signup_page.click_next_button()

        assert google_signup_page.check_date_error_message("유효한 날짜")
        assert not google_signup_page.check_gender_error_message("호칭을 선택")

    def test_input_past_old_year_and_other_input(self):
        """
        생년월일 중 연도를 아주 오래전 숫자로 입력하고 나머지를 다 입력하는 케이스
        :return:
        """
        google_home_page = GmailHomePage(self.driver)
        google_login_page = GoogleLoginPage(self.driver)
        google_signup_page = GoogleSignUpPage(self.driver)
        base_testsuite = SuiteGmailSignUp(self.driver, google_home_page, google_login_page, google_signup_page)

        base_testsuite.step_check_home_image_and_click_login_button()
        base_testsuite.step_check_login_page_and_click_create_account_button()
        base_testsuite.step_check_and_input_name()

        google_signup_page.check_title_text("기본 정보")
        google_signup_page.check_title_sub_text("생일과 성별을 입력하세요.")
        google_signup_page.input_year("1800")
        google_signup_page.input_month()
        google_signup_page.input_day()
        google_signup_page.input_gender("남자")

        google_signup_page.click_next_button()

        assert google_signup_page.check_date_error_message("유효한 날짜")
        assert not google_signup_page.check_gender_error_message("호칭을 선택")

    def test_input_three_character_year_and_other_input(self):
        """
        생년월일 중 연도를 세글자숫자로 입력하고 나머지를 다 입력하는 케이스
        :return:
        """
        google_home_page = GmailHomePage(self.driver)
        google_login_page = GoogleLoginPage(self.driver)
        google_signup_page = GoogleSignUpPage(self.driver)
        base_testsuite = SuiteGmailSignUp(self.driver, google_home_page, google_login_page, google_signup_page)

        base_testsuite.step_check_home_image_and_click_login_button()
        base_testsuite.step_check_login_page_and_click_create_account_button()
        base_testsuite.step_check_and_input_name()

        google_signup_page.check_title_text("기본 정보")
        google_signup_page.check_title_sub_text("생일과 성별을 입력하세요.")
        google_signup_page.input_year("199")
        google_signup_page.input_month()
        google_signup_page.input_day()
        google_signup_page.input_gender("남자")

        google_signup_page.click_next_button()

        assert google_signup_page.check_date_error_message("유효한 날짜")
        assert not google_signup_page.check_gender_error_message("호칭을 선택")

    def test_input_three_character_day_and_other_input(self):
        """
        생년월일 중 일자를 세글자숫자로 입력하고 나머지를 다 입력하는 케이스
        :return:
        """
        google_home_page = GmailHomePage(self.driver)
        google_login_page = GoogleLoginPage(self.driver)
        google_signup_page = GoogleSignUpPage(self.driver)
        base_testsuite = SuiteGmailSignUp(self.driver, google_home_page, google_login_page, google_signup_page)

        base_testsuite.step_check_home_image_and_click_login_button()
        base_testsuite.step_check_login_page_and_click_create_account_button()
        base_testsuite.step_check_and_input_name()

        google_signup_page.check_title_text("기본 정보")
        google_signup_page.check_title_sub_text("생일과 성별을 입력하세요.")
        google_signup_page.input_year()
        google_signup_page.input_month()
        google_signup_page.input_day("121")
        google_signup_page.input_gender("남자")

        google_signup_page.click_next_button()

        assert not google_signup_page.check_date_error_message("유효한 날짜")
        assert not google_signup_page.check_gender_error_message("호칭을 선택")
        assert google_signup_page.check_title_text("Gmail 주소 선택하기")

    def test_input_leap_day_on_leap_year_and_other_input(self):
        """
        생년월일 윤년의 날짜를 입력하고 나머지를 다 입력하는 케이스
        :return:
        """
        google_home_page = GmailHomePage(self.driver)
        google_login_page = GoogleLoginPage(self.driver)
        google_signup_page = GoogleSignUpPage(self.driver)
        base_testsuite = SuiteGmailSignUp(self.driver, google_home_page, google_login_page, google_signup_page)

        base_testsuite.step_check_home_image_and_click_login_button()
        base_testsuite.step_check_login_page_and_click_create_account_button()
        base_testsuite.step_check_and_input_name()

        google_signup_page.check_title_text("기본 정보")
        google_signup_page.check_title_sub_text("생일과 성별을 입력하세요.")
        google_signup_page.input_year("2020")
        google_signup_page.input_month("2")
        google_signup_page.input_day("29")
        google_signup_page.input_gender("남자")

        google_signup_page.click_next_button()

        assert not google_signup_page.check_date_error_message("유효한 날짜")
        assert not google_signup_page.check_gender_error_message("호칭을 선택")
        assert google_signup_page.check_title_text("Gmail 주소 선택하기")

    def test_input_leap_day_on_not_leap_year_and_other_input(self):
        """
        생년월일 윤년이 아닌 해에, 윤년의 날짜를 입력하고 나머지를 다 입력하는 케이스
        :return:
        """
        google_home_page = GmailHomePage(self.driver)
        google_login_page = GoogleLoginPage(self.driver)
        google_signup_page = GoogleSignUpPage(self.driver)
        base_testsuite = SuiteGmailSignUp(self.driver, google_home_page, google_login_page, google_signup_page)

        base_testsuite.step_check_home_image_and_click_login_button()
        base_testsuite.step_check_login_page_and_click_create_account_button()
        base_testsuite.step_check_and_input_name()

        google_signup_page.check_title_text("기본 정보")
        google_signup_page.check_title_sub_text("생일과 성별을 입력하세요.")
        google_signup_page.input_year("2019")
        google_signup_page.input_month("2")
        google_signup_page.input_day("29")
        google_signup_page.input_gender("남자")

        google_signup_page.click_next_button()

        assert google_signup_page.check_date_error_message("유효한 날짜")
        assert not google_signup_page.check_gender_error_message("호칭을 선택")

    def test_input_minus_day_and_other_input(self):
        """
        생년월일 중 일자를 마이너스숫자를 넣고 나머지를 다 넣는 케이스
        :return:
        """
        google_home_page = GmailHomePage(self.driver)
        google_login_page = GoogleLoginPage(self.driver)
        google_signup_page = GoogleSignUpPage(self.driver)
        base_testsuite = SuiteGmailSignUp(self.driver, google_home_page, google_login_page, google_signup_page)

        base_testsuite.step_check_home_image_and_click_login_button()
        base_testsuite.step_check_login_page_and_click_create_account_button()
        base_testsuite.step_check_and_input_name()

        google_signup_page.check_title_text("기본 정보")
        google_signup_page.check_title_sub_text("생일과 성별을 입력하세요.")
        google_signup_page.input_year()
        google_signup_page.input_month()
        google_signup_page.input_day("-9")
        google_signup_page.input_gender("남자")

        google_signup_page.click_next_button()

        assert google_signup_page.check_date_error_message("유효한 날짜")
        assert not google_signup_page.check_gender_error_message("호칭을 선택")


class Test02GoogleGenderValidation:
    """
    기본정보 입력페이지에서 성별에 관한 테스트케이스를 묶어놓았습니다.
    """

    def test_no_input_gender_and_other_input(self):
        """
        성별을 입력안하고 나머지는 다 입력하는 케이스
        :return:
        """
        google_home_page = GmailHomePage(self.driver)
        google_login_page = GoogleLoginPage(self.driver)
        google_signup_page = GoogleSignUpPage(self.driver)
        base_testsuite = SuiteGmailSignUp(self.driver, google_home_page, google_login_page, google_signup_page)

        base_testsuite.step_check_home_image_and_click_login_button()
        base_testsuite.step_check_login_page_and_click_create_account_button()
        base_testsuite.step_check_and_input_name()

        google_signup_page.check_title_text("기본 정보")
        google_signup_page.check_title_sub_text("생일과 성별을 입력하세요.")
        google_signup_page.input_year()
        google_signup_page.input_month()
        google_signup_page.input_day()
        google_signup_page.input_gender("")

        google_signup_page.click_next_button()

        assert not google_signup_page.check_date_error_message("정확히 입력해 주세요.")
        assert google_signup_page.check_gender_error_message("성별을 선택")

    def test_gender_woman_and_other_input(self):
        """
        여자 성별 선택
        0: ['연도', '여자', '없음', '없음']
        """
        google_home_page = GmailHomePage(self.driver)
        google_login_page = GoogleLoginPage(self.driver)
        google_signup_page = GoogleSignUpPage(self.driver)
        base_testsuite = SuiteGmailSignUp(self.driver, google_home_page, google_login_page, google_signup_page)

        base_testsuite.step_check_home_image_and_click_login_button()
        base_testsuite.step_check_login_page_and_click_create_account_button()
        base_testsuite.step_check_and_input_name()

        google_signup_page.check_title_text("기본 정보")
        google_signup_page.check_title_sub_text("생일과 성별을 입력하세요.")
        google_signup_page.input_year()
        google_signup_page.input_month()
        google_signup_page.input_day()
        google_signup_page.input_gender("여자")

        google_signup_page.click_next_button()

        assert google_signup_page.check_title_text("Gmail 주소 선택하기")

    def test_not_open_and_other_input(self):
        """
        공개안함 성별 선택
        7: ['연도', '공개안함', '없음', '없음']
        """
        google_home_page = GmailHomePage(self.driver)
        google_login_page = GoogleLoginPage(self.driver)
        google_signup_page = GoogleSignUpPage(self.driver)
        base_testsuite = SuiteGmailSignUp(self.driver, google_home_page, google_login_page, google_signup_page)

        base_testsuite.step_check_home_image_and_click_login_button()
        base_testsuite.step_check_login_page_and_click_create_account_button()
        base_testsuite.step_check_and_input_name()

        google_signup_page.check_title_text("기본 정보")
        google_signup_page.check_title_sub_text("생일과 성별을 입력하세요.")
        google_signup_page.input_year()
        google_signup_page.input_month()
        google_signup_page.input_day()
        google_signup_page.input_gender("공개 안함")

        google_signup_page.click_next_button()

        assert google_signup_page.check_title_text("Gmail 주소 선택하기")

    def test_custom_gender_no_input_and_other_input(self):
        """
        사용자지정 호칭을 선택하고, 아무것도 입력하지않고 나머지는 다 입력하는 케이스
        :return:
        """
        google_home_page = GmailHomePage(self.driver)
        google_login_page = GoogleLoginPage(self.driver)
        google_signup_page = GoogleSignUpPage(self.driver)
        base_testsuite = SuiteGmailSignUp(self.driver, google_home_page, google_login_page, google_signup_page)

        base_testsuite.step_check_home_image_and_click_login_button()
        base_testsuite.step_check_login_page_and_click_create_account_button()
        base_testsuite.step_check_and_input_name()

        google_signup_page.check_title_text("기본 정보")
        google_signup_page.check_title_sub_text("생일과 성별을 입력하세요.")
        google_signup_page.input_year()
        google_signup_page.input_month()
        google_signup_page.input_day()
        google_signup_page.input_gender("맞춤")

        google_signup_page.click_next_button()

        assert not google_signup_page.check_date_error_message("유효한 날짜")
        assert google_signup_page.check_custom_gender_input_error_message("자신을 가장 잘 나타내는 성별을 알려주세요")
        assert google_signup_page.check_gender_error_message("호칭을 선택")

    def test_custom_gender_character_and_no_input_genderpronoun_and_other_input(self):
        """
        날짜, 사용자지정 호칭을 선택하고, 성별을 입력하지만 대명사는 입력하지 않는 경우
        :return:
        """
        google_home_page = GmailHomePage(self.driver)
        google_login_page = GoogleLoginPage(self.driver)
        google_signup_page = GoogleSignUpPage(self.driver)
        base_testsuite = SuiteGmailSignUp(self.driver, google_home_page, google_login_page, google_signup_page)

        base_testsuite.step_check_home_image_and_click_login_button()
        base_testsuite.step_check_login_page_and_click_create_account_button()
        base_testsuite.step_check_and_input_name()

        google_signup_page.check_title_text("기본 정보")
        google_signup_page.check_title_sub_text("생일과 성별을 입력하세요.")
        google_signup_page.input_year()
        google_signup_page.input_month()
        google_signup_page.input_day()
        google_signup_page.input_gender("맞춤", custom_gender="가나다")

        google_signup_page.click_next_button()

        assert not google_signup_page.check_date_error_message("유효한 날짜")
        assert not google_signup_page.check_custom_gender_input_error_message("자신을 가장 잘 나타내는 성별을 알려주세요")
        assert google_signup_page.check_gender_error_message("호칭을 선택")


class Test02GoogleBirthdayAndGenderPairWise:
    """
    기본정보 입력페이지에서 날짜와 성별에 대한 조합케이스들을 묶어놓았습니다.
    PAIRWISE:
     1: ['월', '남자', '없음', '없음']
     2: ['일', '공개안함', '없음', '없음']
     3: ['생년월일', '맞춤', '성별입력', '없음']
     4: ['생년월일', '공개안함', '없음', '없음']
     6: ['월', '공개안함', '없음', '없음']
     8: ['연도', '남자', '없음', '없음']
     9: ['월', '맞춤', '없음', '여자']
    10: ['일', '여자', '없음', '없음']
    11: ['일', '맞춤', '성별입력', '남자']
    12: ['연도', '맞춤', '성별입력', '기타']
    13: ['생년월일', '남자', '없음', '없음']
    14: ['생년월일', '여자', '없음', '없음']
    15: ['월', '여자', '없음', '없음']

    """

    def test_2(self):
        """
        2: ['일', '공개안함', '없음', '없음']

        """
        google_home_page = GmailHomePage(self.driver)
        google_login_page = GoogleLoginPage(self.driver)
        google_signup_page = GoogleSignUpPage(self.driver)
        base_testsuite = SuiteGmailSignUp(self.driver, google_home_page, google_login_page, google_signup_page)

        base_testsuite.step_check_home_image_and_click_login_button()
        base_testsuite.step_check_login_page_and_click_create_account_button()
        base_testsuite.step_check_and_input_name()

        google_signup_page.check_title_text("기본 정보")
        google_signup_page.check_title_sub_text("생일과 성별을 입력하세요.")
        google_signup_page.input_year()
        google_signup_page.input_month()
        google_signup_page.input_day("")
        google_signup_page.input_gender("공개 안함")

        google_signup_page.click_next_button()

        assert google_signup_page.check_date_error_message("정확히 입력해 주세요.")
        assert not google_signup_page.check_gender_error_message("호칭을 선택")

    def test_3(self):
        """
        3: ['생년월일', '맞춤', '성별입력', '없음']

        """
        google_home_page = GmailHomePage(self.driver)
        google_login_page = GoogleLoginPage(self.driver)
        google_signup_page = GoogleSignUpPage(self.driver)
        base_testsuite = SuiteGmailSignUp(self.driver, google_home_page, google_login_page, google_signup_page)

        base_testsuite.step_check_home_image_and_click_login_button()
        base_testsuite.step_check_login_page_and_click_create_account_button()
        base_testsuite.step_check_and_input_name()

        google_signup_page.check_title_text("기본 정보")
        google_signup_page.check_title_sub_text("생일과 성별을 입력하세요.")
        google_signup_page.input_year("")
        google_signup_page.input_month("")
        google_signup_page.input_day("")
        google_signup_page.input_gender("맞춤", custom_gender="가나다")

        google_signup_page.click_next_button()

        assert google_signup_page.check_date_error_message("생년월일을 정확히 입력해 주세요.")
        assert not google_signup_page.check_custom_gender_input_error_message("자신을 가장 잘 나타내는 성별을 알려주세요")
        assert google_signup_page.check_gender_error_message("호칭을 선택")

    def test_4(self):
        """
        4: ['생년월일', '공개안함', '없음', '없음']

        """
        google_home_page = GmailHomePage(self.driver)
        google_login_page = GoogleLoginPage(self.driver)
        google_signup_page = GoogleSignUpPage(self.driver)
        base_testsuite = SuiteGmailSignUp(self.driver, google_home_page, google_login_page, google_signup_page)

        base_testsuite.step_check_home_image_and_click_login_button()
        base_testsuite.step_check_login_page_and_click_create_account_button()
        base_testsuite.step_check_and_input_name()

        google_signup_page.check_title_text("기본 정보")
        google_signup_page.check_title_sub_text("생일과 성별을 입력하세요.")
        google_signup_page.input_year("")
        google_signup_page.input_month("")
        google_signup_page.input_day("")
        google_signup_page.input_gender("공개 안함")

        google_signup_page.click_next_button()

        assert google_signup_page.check_date_error_message("생년월일을 정확히 입력해 주세요.")
        assert not google_signup_page.check_gender_error_message("호칭을 선택")

    def test_6(self):
        """
        6: ['월', '공개안함', '없음', '없음']

        """
        google_home_page = GmailHomePage(self.driver)
        google_login_page = GoogleLoginPage(self.driver)
        google_signup_page = GoogleSignUpPage(self.driver)
        base_testsuite = SuiteGmailSignUp(self.driver, google_home_page, google_login_page, google_signup_page)

        base_testsuite.step_check_home_image_and_click_login_button()
        base_testsuite.step_check_login_page_and_click_create_account_button()
        base_testsuite.step_check_and_input_name()

        google_signup_page.check_title_text("기본 정보")
        google_signup_page.check_title_sub_text("생일과 성별을 입력하세요.")
        google_signup_page.input_year()
        google_signup_page.input_month("")
        google_signup_page.input_day()
        google_signup_page.input_gender("공개 안함")

        google_signup_page.click_next_button()

        assert google_signup_page.check_date_error_message("생년월일을 정확히 입력해 주세요.")
        assert not google_signup_page.check_gender_error_message("호칭을 선택")

    def test_8(self):
        """
        8: ['연도', '남자', '없음', '없음']

        """
        google_home_page = GmailHomePage(self.driver)
        google_login_page = GoogleLoginPage(self.driver)
        google_signup_page = GoogleSignUpPage(self.driver)
        base_testsuite = SuiteGmailSignUp(self.driver, google_home_page, google_login_page, google_signup_page)

        base_testsuite.step_check_home_image_and_click_login_button()
        base_testsuite.step_check_login_page_and_click_create_account_button()
        base_testsuite.step_check_and_input_name()

        google_signup_page.check_title_text("기본 정보")
        google_signup_page.check_title_sub_text("생일과 성별을 입력하세요.")
        google_signup_page.input_year("")
        google_signup_page.input_month()
        google_signup_page.input_day()
        google_signup_page.input_gender("남자")

        google_signup_page.click_next_button()

        assert google_signup_page.check_date_error_message("생년월일을 정확히 입력해 주세요.")
        assert not google_signup_page.check_gender_error_message("호칭을 선택")

    def test_9(self):
        """
        9: ['월', '맞춤', '없음', '여자']

        """
        google_home_page = GmailHomePage(self.driver)
        google_login_page = GoogleLoginPage(self.driver)
        google_signup_page = GoogleSignUpPage(self.driver)
        base_testsuite = SuiteGmailSignUp(self.driver, google_home_page, google_login_page, google_signup_page)

        base_testsuite.step_check_home_image_and_click_login_button()
        base_testsuite.step_check_login_page_and_click_create_account_button()
        base_testsuite.step_check_and_input_name()

        google_signup_page.check_title_text("기본 정보")
        google_signup_page.check_title_sub_text("생일과 성별을 입력하세요.")
        google_signup_page.input_year()
        google_signup_page.input_month("")
        google_signup_page.input_day()
        google_signup_page.input_gender("맞춤", custom_gender="", gender_pronoun="여자")

        google_signup_page.click_next_button()

        assert google_signup_page.check_date_error_message("생년월일을 정확히 입력해 주세요.")
        assert google_signup_page.check_custom_gender_input_error_message("자신을 가장 잘 나타내는 성별을 알려주세요")
        assert not google_signup_page.check_gender_error_message("호칭을 선택")

    def test_10(self):
        """
        10: ['일', '여자', '없음', '없음']

        """
        google_home_page = GmailHomePage(self.driver)
        google_login_page = GoogleLoginPage(self.driver)
        google_signup_page = GoogleSignUpPage(self.driver)
        base_testsuite = SuiteGmailSignUp(self.driver, google_home_page, google_login_page, google_signup_page)

        base_testsuite.step_check_home_image_and_click_login_button()
        base_testsuite.step_check_login_page_and_click_create_account_button()
        base_testsuite.step_check_and_input_name()

        google_signup_page.check_title_text("기본 정보")
        google_signup_page.check_title_sub_text("생일과 성별을 입력하세요.")
        google_signup_page.input_year()
        google_signup_page.input_month()
        google_signup_page.input_day("")
        google_signup_page.input_gender("여자")

        google_signup_page.click_next_button()

        assert google_signup_page.check_date_error_message("생년월일을 정확히 입력해 주세요.")
        assert not google_signup_page.check_gender_error_message("호칭을 선택")

    def test_11(self):
        """
        11: ['일', '맞춤', '성별입력', '남자']

        """
        google_home_page = GmailHomePage(self.driver)
        google_login_page = GoogleLoginPage(self.driver)
        google_signup_page = GoogleSignUpPage(self.driver)
        base_testsuite = SuiteGmailSignUp(self.driver, google_home_page, google_login_page, google_signup_page)

        base_testsuite.step_check_home_image_and_click_login_button()
        base_testsuite.step_check_login_page_and_click_create_account_button()
        base_testsuite.step_check_and_input_name()

        google_signup_page.check_title_text("기본 정보")
        google_signup_page.check_title_sub_text("생일과 성별을 입력하세요.")
        google_signup_page.input_year()
        google_signup_page.input_month()
        google_signup_page.input_day("")
        google_signup_page.input_gender("맞춤", custom_gender="가나다", gender_pronoun="남자")

        google_signup_page.click_next_button()

        assert google_signup_page.check_date_error_message("생년월일을 정확히 입력해 주세요.")
        assert not google_signup_page.check_custom_gender_input_error_message("자신을 가장 잘 나타내는 성별을 알려주세요")
        assert not google_signup_page.check_gender_error_message("호칭을 선택")

    def test_12(self):
        """
        12: ['연도', '맞춤', '성별입력', '기타']

        """
        google_home_page = GmailHomePage(self.driver)
        google_login_page = GoogleLoginPage(self.driver)
        google_signup_page = GoogleSignUpPage(self.driver)
        base_testsuite = SuiteGmailSignUp(self.driver, google_home_page, google_login_page, google_signup_page)

        base_testsuite.step_check_home_image_and_click_login_button()
        base_testsuite.step_check_login_page_and_click_create_account_button()
        base_testsuite.step_check_and_input_name()

        google_signup_page.check_title_text("기본 정보")
        google_signup_page.check_title_sub_text("생일과 성별을 입력하세요.")
        google_signup_page.input_year("")
        google_signup_page.input_month()
        google_signup_page.input_day()
        google_signup_page.input_gender("맞춤", custom_gender="가나다", gender_pronoun="기타")

        google_signup_page.click_next_button()

        assert google_signup_page.check_date_error_message("생년월일을 정확히 입력해 주세요.")
        assert not google_signup_page.check_custom_gender_input_error_message("자신을 가장 잘 나타내는 성별을 알려주세요")
        assert not google_signup_page.check_gender_error_message("호칭을 선택")

    def test_13(self):
        """
        13: ['생년월일', '남자', '없음', '없음']

        """
        google_home_page = GmailHomePage(self.driver)
        google_login_page = GoogleLoginPage(self.driver)
        google_signup_page = GoogleSignUpPage(self.driver)
        base_testsuite = SuiteGmailSignUp(self.driver, google_home_page, google_login_page, google_signup_page)

        base_testsuite.step_check_home_image_and_click_login_button()
        base_testsuite.step_check_login_page_and_click_create_account_button()
        base_testsuite.step_check_and_input_name()

        google_signup_page.check_title_text("기본 정보")
        google_signup_page.check_title_sub_text("생일과 성별을 입력하세요.")
        google_signup_page.input_year("")
        google_signup_page.input_month("")
        google_signup_page.input_day("")
        google_signup_page.input_gender("남자")

        google_signup_page.click_next_button()

        assert google_signup_page.check_date_error_message("생년월일을 정확히 입력해 주세요.")
        assert not google_signup_page.check_gender_error_message("호칭을 선택")

    def test_14(self):
        """
        14: ['생년월일', '여자', '없음', '없음']

        """
        google_home_page = GmailHomePage(self.driver)
        google_login_page = GoogleLoginPage(self.driver)
        google_signup_page = GoogleSignUpPage(self.driver)
        base_testsuite = SuiteGmailSignUp(self.driver, google_home_page, google_login_page, google_signup_page)

        base_testsuite.step_check_home_image_and_click_login_button()
        base_testsuite.step_check_login_page_and_click_create_account_button()
        base_testsuite.step_check_and_input_name()

        google_signup_page.check_title_text("기본 정보")
        google_signup_page.check_title_sub_text("생일과 성별을 입력하세요.")
        google_signup_page.input_year("")
        google_signup_page.input_month("")
        google_signup_page.input_day("")
        google_signup_page.input_gender("여자")

        google_signup_page.click_next_button()

        assert google_signup_page.check_date_error_message("생년월일을 정확히 입력해 주세요.")
        assert not google_signup_page.check_gender_error_message("호칭을 선택")

    def test_15(self):
        """
        15: ['월', '여자', '없음', '없음']

        """
        google_home_page = GmailHomePage(self.driver)
        google_login_page = GoogleLoginPage(self.driver)
        google_signup_page = GoogleSignUpPage(self.driver)
        base_testsuite = SuiteGmailSignUp(self.driver, google_home_page, google_login_page, google_signup_page)

        base_testsuite.step_check_home_image_and_click_login_button()
        base_testsuite.step_check_login_page_and_click_create_account_button()
        base_testsuite.step_check_and_input_name()

        google_signup_page.check_title_text("기본 정보")
        google_signup_page.check_title_sub_text("생일과 성별을 입력하세요.")
        google_signup_page.input_year()
        google_signup_page.input_month("")
        google_signup_page.input_day()
        google_signup_page.input_gender("여자")

        google_signup_page.click_next_button()

        assert google_signup_page.check_date_error_message("생년월일을 정확히 입력해 주세요.")
        assert not google_signup_page.check_gender_error_message("호칭을 선택")


class Test02GoogleBirthdayAndGenderOther:
    """
    성별과 생년월일을 입력하는 패턴에서 위 pairwise패턴에서 찾아내지못한 추가 케이스
    """
    def test_no_input_birthday_and_gender(self):
        """
        생녕월일과 성별을 입력하지 않는 케이스
        :return:
        """
        google_home_page = GmailHomePage(self.driver)
        google_login_page = GoogleLoginPage(self.driver)
        google_signup_page = GoogleSignUpPage(self.driver)
        base_testsuite = SuiteGmailSignUp(self.driver, google_home_page, google_login_page, google_signup_page)

        base_testsuite.step_check_home_image_and_click_login_button()
        base_testsuite.step_check_login_page_and_click_create_account_button()
        base_testsuite.step_check_and_input_name()

        google_signup_page.check_title_text("기본 정보")
        google_signup_page.check_title_sub_text("생일과 성별을 입력하세요.")
        google_signup_page.input_year("")
        google_signup_page.input_month("")
        google_signup_page.input_day("")
        google_signup_page.input_gender("")

        google_signup_page.click_next_button()

        assert google_signup_page.check_date_error_message("정확히 입력해 주세요.")
        assert google_signup_page.check_gender_error_message("성별을 선택")

    def test_no_input_birthday_and_custom_gender(self):
        """
        생년월일과 맞춤 호칭을 선택하되 다른것은 입력하지 않는 케이스
        :return:
        """
        google_home_page = GmailHomePage(self.driver)
        google_login_page = GoogleLoginPage(self.driver)
        google_signup_page = GoogleSignUpPage(self.driver)
        base_testsuite = SuiteGmailSignUp(self.driver, google_home_page, google_login_page, google_signup_page)

        base_testsuite.step_check_home_image_and_click_login_button()
        base_testsuite.step_check_login_page_and_click_create_account_button()
        base_testsuite.step_check_and_input_name()

        google_signup_page.check_title_text("기본 정보")
        google_signup_page.check_title_sub_text("생일과 성별을 입력하세요.")
        google_signup_page.input_year("")
        google_signup_page.input_month("")
        google_signup_page.input_day("")
        google_signup_page.input_gender("맞춤")

        google_signup_page.click_next_button()

        assert google_signup_page.check_date_error_message("정확히 입력해 주세요.")
        assert google_signup_page.check_custom_gender_input_error_message("자신을 가장 잘 나타내는 성별을 알려주세요")
        assert google_signup_page.check_gender_error_message("호칭을 선택")

    def test_custom_gender_character_and_no_input_genderpronoun_and_birthday(self):
        """
        사용자지정 호칭을 선택하고, 성별을 입력하지만 생년월일과 대명사는 입력하지 않는 케이스
        :return:
        """
        google_home_page = GmailHomePage(self.driver)
        google_login_page = GoogleLoginPage(self.driver)
        google_signup_page = GoogleSignUpPage(self.driver)
        base_testsuite = SuiteGmailSignUp(self.driver, google_home_page, google_login_page, google_signup_page)

        base_testsuite.step_check_home_image_and_click_login_button()
        base_testsuite.step_check_login_page_and_click_create_account_button()
        base_testsuite.step_check_and_input_name()

        google_signup_page.check_title_text("기본 정보")
        google_signup_page.check_title_sub_text("생일과 성별을 입력하세요.")
        google_signup_page.input_year("")
        google_signup_page.input_month("")
        google_signup_page.input_day("")
        google_signup_page.input_gender("맞춤", custom_gender="가나다")

        google_signup_page.click_next_button()

        assert google_signup_page.check_date_error_message("생년월일을 정확히 입력")
        assert not google_signup_page.check_custom_gender_input_error_message("자신을 가장 잘 나타내는 성별을 알려주세요")
        assert google_signup_page.check_gender_error_message("호칭을 선택")

    def test_custom_gender_pronoun_and_other_no_input(self):
        """
        성별 대명사만 입력하고 나머지는  선택하고 나머지는 전부 입력하지않는 케이스
        :return:
        """
        google_home_page = GmailHomePage(self.driver)
        google_login_page = GoogleLoginPage(self.driver)
        google_signup_page = GoogleSignUpPage(self.driver)
        base_testsuite = SuiteGmailSignUp(self.driver, google_home_page, google_login_page, google_signup_page)

        base_testsuite.step_check_home_image_and_click_login_button()
        base_testsuite.step_check_login_page_and_click_create_account_button()
        base_testsuite.step_check_and_input_name()

        google_signup_page.check_title_text("기본 정보")
        google_signup_page.check_title_sub_text("생일과 성별을 입력하세요.")
        google_signup_page.input_year("")
        google_signup_page.input_month("")
        google_signup_page.input_day("")
        google_signup_page.input_gender("맞춤", custom_gender="", gender_pronoun="남자")

        google_signup_page.click_next_button()

        assert google_signup_page.check_date_error_message("생년월일을 정확히 입력")
        assert google_signup_page.check_custom_gender_input_error_message("자신을 가장 잘 나타내는 성별을 알려주세요")
        assert not google_signup_page.check_gender_error_message("호칭을 선택")
