import time

from selenium.common.exceptions import TimeoutException, NoSuchElementException

from src.base_page import BasePage
from src.web.locators.google_signup_page_locator import GoogleSignUpPageLocator as WebGoogleSignUpPageLocator
from src.android.locators.google_signup_page_locator import GoogleSignUpPageLocator as MobileGoogleSignUpPageLocator
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy


class GoogleSignUpPage(BasePage):
    """
    구글 회원가입 페이지입니다.
    웹과 앱의 페이지형태가 동일하므로 로케이터만 바꾸어서 작성한 테스트케이스를 앱과 웹 둘 다 사용할 수 있도록 고안하였습니다.
    platform 파라미터의 값에 따라 참조하는 로케이터클래스가 달라집니다.
    """

    def __init__(self, driver: WebDriver, platform: str = "web"):
        super().__init__(driver)
        self.custom_gender_flag = False
        self.platform = platform

        if platform == "web":
            self.locator = WebGoogleSignUpPageLocator()
        else:
            self.locator = MobileGoogleSignUpPageLocator()

    def check_title_text(self, header_text: str) -> bool:
        """
        화면 내 중앙에 노출되는 메인 텍스트가 무엇인지를 확인합니다. 텍스트를 넣어 해당하는 요소를 찾아, 입력한 텍스트와 일치하는지 확인합니다.
        :param header_text:str
        :return: bool
        """
        time.sleep(0.3)

        if self.platform != "web" and header_text == "보안문자 입력":
            header_text = "전화번호를 추가하시겠습니까?"

        try:
            locator = (By.XPATH, '//*[@id="headingText"]/span')
            text = self._get_text(locator)
            self.logger.info("화면별 헤더 텍스트 : %s", text)
            if text == header_text:
                return True
            else:
                time.sleep(1)
                return self._get_text(locator) == header_text  # 화면전환 타이밍 상 실패할 수 있으므로 한 번 더 체크한다.
        except TimeoutException:
            return False

    def check_title_sub_text(self, sub_text: str) -> bool:
        """
        화면 내 중앙에 노출되는 메인 텍스트 하단의 서브텍스트를 확인합니다.

        :param sub_text:str
        :return: bool
        """
        time.sleep(0.3)
        try:
            locator = (By.XPATH, '//*[@id="headingSubtext"]/span')
            text = self._get_text(locator)
            self.logger.info("화면별 서브헤더 텍스트 : %s", text)
            return text == sub_text
        except TimeoutException:
            return False

    def get_error_message(self) -> str:
        return self._get_text(self.locator.WARNING_MESSAGE)

    def click_next_button(self):
        """
        화면 내 "다음" 버튼을 누릅니다.

        """
        time.sleep(0.3)
        self._click(self.locator.BUTTON_NEXT)

    def input_lastname(self, lastname: str):
        """
        계정 만들기 페이지에서 성 부분을 입력합니다.
        :param lastname:str
        :return:
        """

        self._input(self.locator.INPUT_LAST_NAME_FIELD, lastname)

    def input_firstname(self, firstname: str):
        """
        계정 만들기 페이지에서 이름 부분을 입력합니다.
        :param firstname:
        :return:
        """

        self._input(self.locator.INPUT_FIRST_NAME_FIELD, firstname)

    def input_year(self, year: str = "2002"):
        """
        기본 정보 입력화면에서 연도 를 입력합니다.
        :param year:str = "2002"
        :return:
        """
        time.sleep(0.3)
        self._input(self.locator.INPUT_YEAR_FIELD, year)

    def input_month(self, month: str = "11"):
        """
        기본 정보 입력화면에서 월을 입력합니다.
        :param month: str
        :return:
        """
        time.sleep(0.3)
        if self.platform == "web":

            self._get_select_tag_element(self.locator.SELECT_MONTH_FIELD).select_by_value(month)

        else:
            self._click(self.locator.SELECT_MONTH_FIELD)
            self._click((AppiumBy.XPATH, f"//android.widget.CheckedTextView[contains(@text, '{month}')]"))

    def input_day(self, day: str = "7"):
        """
        기본 정보 입력창에서 일 부분을 입력합니다.
        :param day: str
        :return:
        """
        time.sleep(0.3)
        self._input(self.locator.INPUT_DAY_FIELD, day)

    def input_gender(self, gender: str, custom_gender: str = "", gender_pronoun: str = ""):
        """
        기본 정보 입력화면에서 성별 부분을 선택합니다.
        gender가 "사용자 지정" 인 경우에는 성별 대명사를 같이 입력해주어야합니다.
        :param gender: str
        :param custom_gender:str
        :param gender_pronoun: str
        :return:
        """
        time.sleep(0.3)

        if self.platform == "web":

            self._get_select_tag_element(self.locator.SELECT_GENDER_FIELD).select_by_visible_text(gender)

            if gender == "맞춤":
                self.custom_gender_flag = True
                self._find_element_for_wait(self.locator.INPUT_CUSTOM_GENDER_FIELD).find_element(By.TAG_NAME,
                                                                                                 "input").send_keys(
                    custom_gender)
                if gender_pronoun != "":
                    self._get_select_tag_element((By.ID, "genderpronoun")).select_by_visible_text(gender_pronoun)

        else:
            self._click(self.locator.SELECT_GENDER_FIELD)
            self._click((AppiumBy.XPATH, f"//android.widget.CheckedTextView[contains(@text, '{gender}')]"))

    def create_my_gmail_address(self, mail_address: str):
        """
        Gmail 주소 선택하기 부분에서 내 Gmail 주소 만들기를 누른 후 메일주소를 입력하여 만듭니다.
        :param mail_address:
        :return:
        """
        time.sleep(0.3)
        self._click(self.locator.LABEL_CREATE_MY_GMAIL_ADDRESS)
        self._input(self.locator.INPUT_GMAIL_ADDRESS_FIELD, mail_address)

    def input_pasword_and_password_again(self, password):
        """
        비밀번호와 비밀번호 확인란을 한 번에 입력합니다.
        :param password: str
        :return:
        """
        if self.platform == "web":
            self.input_password(password)
            self.input_password_again(password)
        else:
            self.input_password(password)

    def input_password(self, password: str):
        """
        비밀번호 입력란을 입력합니다.
        :param password: str
        :return:
        """
        self._input(self.locator.INPUT_PASSWORD_FILED, password)

    def input_password_again(self, password: str):
        """
        비밀번호 확인란을 입력합니다.
        :param password: str
        :return:
        """
        self._input(self.locator.INPUT_PASSWORD_CONFIRM_FILED, password)

    def click_view_password(self):
        """
        비밀번호 보기 체크박스를 클릭하여 비밀번호를 노출시킵니다.
        :return:
        """
        time.sleep(0.3)
        self._click(self.locator.CHECKBOX_VIEW_PASWORD)

    def get_password(self) -> str:
        """
        비밀번호 입력란에서 입력되어있는 비밀번호를 리턴합니다.
        :return: str
        """
        time.sleep(0.5)
        return self._find_element_for_wait(self.locator.INPUT_PASSWORD_FILED).get_attribute("value")

    def get_password_again_field(self) -> str:
        """
        비밀번호 확인란에서 입력되어있는 비밀번호를 리턴합니다.
        :return:str
        """
        return self._find_element_for_wait(self.locator.INPUT_PASSWORD_CONFIRM_FILED).get_attribute("value")

    def check_name_error_message(self, text: str) -> bool:
        """
        이름관련 에러메세지를 확인합니다.
        :param text:
        :return:
        """
        return self.__check_error_message(text, "name")

    def check_date_error_message(self, text: str) -> bool:
        """
        날짜 에러메세지를 확인합니다.
        :param text:
        :return:
        """
        return self.__check_error_message(text, "date")

    def check_gender_error_message(self, text: str) -> bool:
        """
        성별관련 에러메세지를 확인합니다.
        성별을 사용자지정으로 입력했다면, 성별대명사 부분의 에러메세지를 확인합니다.
        :param text:
        :return:
        """
        if self.custom_gender_flag:
            return self.__check_error_message(text, "genderpronoun")
        else:
            return self.__check_error_message(text, "gender")

    def check_custom_gender_input_error_message(self, text: str) -> bool:
        """
        사용자 지정 성별을 선택했을 떄, 성별을 입력하는 input field 하단의 경고메세지를 체크합니다.
        :param text:
        :return:
        """
        try:
            error_message = self._find_element_for_wait((By.XPATH, '//div[@id="customGender"]//span/parent::div')).text
            self.logger.info(error_message)
            return text in error_message
        except:
            return False

    def check_mail_address_error_message(self, text: str) -> bool:
        """
        메일 주소 선택하기 화면에서 내 주소 만들기를 할 때에 에러메세지를 체크합니다.
        :param text: str
        :return: bool
        """
        try:
            return text in self._get_text(self.locator.ADDRESS_ERROR_MESSAGE)
        except TimeoutException:
            return False

    def check_password_error_message(self, text: str) -> bool:
        """
        비밀번호 만들기 화면에서 비밀번호를 생성할 때에 에러메세지를 체크합니다.
        :param text:str
        :return: bool
        """

        try:
            time.sleep(0.5)
            self.logger.info(self._get_text(self.locator.PASSWORD_ERROR_MESSAGE))
            return text in self._get_text(self.locator.PASSWORD_ERROR_MESSAGE)
        except TimeoutException:
            return False

    def __check_error_message(self, text: str, locator_sub_text: str) -> bool:
        """
        에러메세지를 체크합니다.
        :param text:
        :param locator_sub_text:
        :return:
        """
        locator_text = f"//*[@id='{locator_sub_text}Error']"
        locator = None

        if locator_sub_text == "name":
            locator = (By.XPATH, f"{locator_text}//span")
        elif locator_sub_text == "date":
            locator = (By.XPATH, f"{locator_text}/div")
        else:
            locator = (By.XPATH, locator_text)

        self.logger.info(locator)
        try:
            element = self._find_element_for_wait(locator)
            self.logger.info(element.is_displayed())
            self.logger.info(element.text)
            return element.is_displayed() and text in element.text
        except TimeoutException:
            return False
