# Portfolio Gmail

안녕하세요. **유다훈** 입니다.

현재 하이퍼커넥트에서 Software Development in Test 라는 직군으로 근무하고 있습니다. 현재 아래의 업무를 수행하고 있습니다.
- 아자르 제품의 기존 매뉴얼 회귀테스트케이스에 대한 자동화


---

Gmail 회원가입에 대한 테스트코드를 포트폴리오로 제작하였습니다.

사용 언어와 라이브러리는 대략적으로 아래와 같습니다.
- Python
- Selenium
- Appium
- pytest
- webdriver-manager=
- allure-pytest

---

총 실행대상 테스트케이스는 **76개**  입니다. 우선적으로 **web을 구현**하였으며 
드라이버 생성 자체는 Android에 대해서 페이지클래스의 객체 생성 시 `platform` 파라미터를 넘겨주는 것으로 로케이터 클래스를 구분해서 동작할 수 있도록 만들었습니다.

전체 실행하는데 시간이 조금 소요되는 관계로, happy case를 우선적으로 실행하시면 좋을 것 같습니다. 
혹시나 실행에 제약이 있을 수 있어서 web/aos의 happycase를 녹화한 영상을 링크로 제공해드리고자 합니다.

- [web happycase](https://drive.google.com/file/d/1qk7nR_haexhqLKxII1j6isccd23CbLVn/view?usp=drive_link)

감사합니다. 


- [실행 방법](#실행-방법)
  - [전제 조건](#전제-조건)
  - [실행 커맨드](#실행-커맨드)
- [디렉토리 구조](#디렉토리-구조)
- [프로젝트 설계](#프로젝트-설계)
  - [BasePage 상속](#basepage-상속)
  - [Locator 전략](#locator-전략)
  - [Testsuite과 Testrun](#testsuite과-testrun-구성)
- [커맨드라인 옵션과 드라이버 생성](#커스텀-커맨드라인-명령)
  - [커스텀 커맨드라인 명령어](#커스텀-커맨드라인-명령어)
  - [드라이버 생성과 Desired Capabilities](#드라이버-생성과-desired-capabilities)
- [테스트케이스 설계](#테스트케이스-설계)
  - [Happy case](#happy-case)
  - [Google 계정만들기 단계](#google-계정만들기-단계)
  - [기본 정보 입력 단계](#기본-정보-단계)
  - [Gmail 주소 선택하기 단계](#gmail-주소-선택하기-단계)
  - [안전한 비밀번호 만들기 단계](#안전한-비밀번호-만들기-단계)
- [그 외](#그-외)
  - [Logging](#logging)
  - [Reporting and capture](#reporting-and-capture)
---
## 실행 방법

### 전제 조건
일단 python과 appium server가 설치되어있어야합니다. 설치가 되어있다면 레포지토리를 로컬로 클론해주시고 터미널에서 해당 프로젝트로 이동하신 후에 가상환경을 만드신 
라이브러리를 설치해주세요.

```
python3 -m venv venv
cd venv
source bin/activate

pip3 install -r requirements.txt
```

또한 로컬에서 allure report를 확인하시려면 별도로 allure를 설치하셔야합니다.

`brew install allure`

### 실행 커맨드
아래 실행 커맨드는 전체 케이스를 실행합니다.

본 과제물은 `allure report`를 지원하고 있으며, allure report는 pytest의 출력문자에 color옵션이 활성화되어있으면 일부문자에서 문자깨짐이 발생하므로 `--color=no` 옵션을 활성화해줍니다.
#### web
`pytest -s -v ./tests/run/web --platform=web --alluredir=./report --color=no`


Happy case만 실행하고자 하신다면 아래 커맨드를 이용해주세요.

- web : `pytest -s -v ./tests/run/web/test_google_signup_happycase.py --platform=web --alluredir=./report --color=no`


---

## 디렉토리 구조
디렉토리 구조는 아래와 같습니다.

```text
.
├── README.md
├── conftest.py
├── pytest.ini
├── requirements.txt
├── resources
│   └── desired_capabilities.ini
├── src
│   ├── base_page.py
│   └── web
│       ├── locators
│       │   ├── gmail_home_page_locator.py
│       │   ├── google_login_page_locator.py
│       │   └── google_signup_page_locator.py
│       └── pages
│           └── gmail_home_page.py
│           ├── google_login_page.py
│           └── google_signup_page.py
├── tests
│   ├── run
│   │   └── web
│   │       ├── test_01_google_create_account.py
│   │       ├── test_02_google_birthday_and_gender.py
│   │       ├── test_03_google_mail_address.py
│   │       ├── test_04_google_password.py
│   │       └── test_google_signup_happycase.py
│   └── suite
│       └── suite_gmail_signup.py
└── utilities.py

```
---


## 프로젝트 설계
본 프로젝트는 _Page Object Design_ 을 이용하였습니다. `src` 폴더 하위에 모든 페이지의 베이스가 될 `BasePage`가 존재하고, 그 외 `web`, `android` 디렉토리 하위에는 각각 플랫폼별 고유한 페이지들을 클래스로 만들었습니다.

`base` 폴더 하위에 존재하는 `google_login_page`(구글로그인페이지), `google_signup_page`(구글 회원가입페이지) 는 web과 aos 둘 다 UI가 동일하여 로케이터만 바꿔 사용하고 페이지 클래스 자체는 그대로 재사용하도록 하였습니다.

프로젝트를 작성하면서 신경 쓴 부분은 **코드의 재사용성** 입니다.

### `BasePage` 상속
모든 페이지의 기본적인 동작들을 따로 정의한 `BasePage` 라는 클래스를 만들었습니다. 이 클래스는 모든 페이지에서 상속받도록 하여 어떤 element를 찾는 동작은 물론,
click, input등의 기본적인 동작들도 재사용할 수 있도록 하였습니다.

![BasePage의 상속관계](https://velog.velcdn.com/images/dahunyoo/post/50523a6e-a712-4aa7-9b58-2fa6c57a11d4/image.png)
<p align="center"> BasePage의 상속관계 </p>


`BasePage`는 생성자 내에서 `WebDriverWait`객체와 [logger 객체](#logging)를 생성합니다. `WebDriverWait` 객체의 `timeout` 기본값은 `10초` 로 설정된 상태입니다.

```python
class BasePage:
    """
    BasePage 클래스는 페이지들에서 수행해야할 기본적인 행위들을 정의합니다.
    생성자에서는 드라이버, wait, logger 객체를 생성합니다.
    wait 객체는 기본 대기시간 10초입니다.

    """
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.logger = logger_factory(type(self).__name__)
```


`BasePage` 클래스에서는 상황에 따라 `driver` 혹은 명시적 대기 `wait`를 이용한 element 조작을 할 수 있도록 메소드들을 나누어 놓았습니다.

```python
def _find_element(self, locator: tuple) -> WebElement:
    """
    find_element를 수행하여 element를 return합니다.

    :param locator:
    :return:
    """
    return self.driver.find_element(*locator)

def _find_element_for_wait(self, locator: tuple) -> WebElement:
    """
    wait를 이용하여 element를 식별하고, 리턴합니다.
    대기시간은 10초이며 조건은 visibility_of_element_located() 입니다.
    :param locator:
    :return: WebElement
    """
    return self.wait.until(EC.visibility_of_element_located(locator))
```


### Locator 전략
로케이터는 일단 page에서 분리하여 별도의 locator파일로 관리하도록 하였으며 클래스로 만들어 Enum의 형태로 사용하도록 하였습니다. 이렇게 분리하는 것은 개발자들의 리팩토링으로 인하여 화면의 구성은 변경사항이 없으나 identifier값이나 로케이터의 구조가 바뀌게되는 경우, 로케이터파일만 수정하면 대응할 수 있도록 하기 위함입니다.

```python
class GoogleSignUpPageLocator():

    BUTTON_NEXT = (By.XPATH, '//span[contains(text(), "다음")]//parent::button')

    INPUT_LAST_NAME_FIELD = (By.ID, 'lastName')
    INPUT_FIRST_NAME_FIELD = (By.ID, 'firstName')
```

튜플의 형태로 사용한 것은, `wait`를 이용한 element 조작시에는 locator를 튜플의 형태로 넘겨야했기 때문에 튜플로 생성하였습니다. 만약 `driver` 를 이용한 element조작이 필요하다면, 로케이터를 사용할 때에 `*` 를 붙여 Unpacking해야합니다. (BasePage 사용 부분의 [예시코드](#basepage-상속)를 확인해주세요.)


```python
import time
from src.base_page import BasePage
from src.web.locators.google_signup_page_locator import GoogleSignUpPageLocator as WebGoogleSignUpPageLocator

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

        self.locator = WebGoogleSignUpPageLocator()
            
    def input_lastname(self, lastname: str):
        """
        계정 만들기 페이지에서 성 부분을 입력합니다.
        :param lastname:str
        :return:
        """
        self._input(self.locator.INPUT_LAST_NAME_FIELD, lastname) #생성된 로케이터 클래스에 따라 실제 로케이터값이 플랫폼에 맞게 설정됩니다.
            
    def input_month(self, month: str = "11"):
        """
        기본 정보 입력화면에서 월을 입력합니다.
        본 메소드의 경우는 플랫폼별로 조작해야하는 방식이 다르기 때문에 platform별로 값을 다시 정의해줍니다.
        web의 경우에는 Select태그에서 value값을 통해 바로 선택을 하고, aos의 경우에는 단계별로 클릭해가며 설정합니다.
        :param month: str
        :return:
        """
        time.sleep(0.3)
        self._get_select_tag_element(self.locator.SELECT_MONTH_FIELD).select_by_value(month)          

```

### Testsuite과 Testrun 구성
`tests` 하위에는 다시 `run` 과 `suite` 로 디렉토리를 분리하였으며 `run` 하위에는 실제 테스트가 수행될 코드들이 존재합니다.
```text
├── tests
│   ├── run
│   │   └── web
│   │       ├── test_01_google_create_account.py
│   │       ├── test_02_google_birthday_and_gender.py
│   │       ├── test_03_google_mail_address.py
│   │       ├── test_04_google_password.py
│   │       └── test_google_signup_happycase.py
│   └── suite
│       └── suite_gmail_signup.py

```

`suite`에는 일단 기본적인 happy case가 되는 테스트케이스들을 작성해놓았고, `run`에서 이 suite의 객체를 만들어 호출하는 식으로 구성하였습니다. 이렇게 하여 기존에 작성되어져있는 테스트 코드에 대해서도 재사용할 수 있게 하였습니다.
또한 회원가입페이지 후반부분인 생년월일/성별 입력이라던지 비밀번호 입력단계까지 가기위해서는 앞단계들을 반복적으로 수행해야하는데, suite의 케이스들을 호출하는 것으로 반복코드를 줄일 수 있습니다.

```python
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
```


```python
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
```
위 코드를 예시로 설명드리자면, 위 테스트케이스는 이메일주소를 생성하는 단계에서 아무것도 입력하지 않는 패턴을 확인하는 케이스입니다. 여기서 `SuiteGmailSignUp()` 객체를 생성한 후 이메일주소 생성하기 화면까지 이동할때 필요한 스텝들을
해당 suite로 부터 불러와 수행하고 있습니다.

---

## 커맨드라인 옵션과 드라이버 생성

### 커스텀 커맨드라인 명령어
기본적인 pytest의 실행커맨드 이외에도 커스텀 커맨드라인 명령어를 추가하여 플랫폼별 코드를 하나의 프로젝트 내에서 관리하면서 실행 시에는 각각 별도의 플랫폼별 테스트코드를 실행시킬 수 있도록 하였습니다.
```python
# conftest.py

def pytest_addoption(parser):
    """
    pytest 실행 시에 commandLine option을 설정합니다.
    :param parser:
    :return:
    """
    parser.addoption(
        "--platform", default="web", action="store", help="web/android"
    )

```

여기서 입력받은 option은 pytest의 `request` 변수를 이용하여 실제 실행되는 테스트케이스에서 직접 호출하여 사용할 수 있습니다.

### 드라이버 생성과 Desired Capabilities
현재 드라이버의 생명주기는 테스트케이스 구조상 **function(method)** 단위로 생성과 종료를 수행합니다. 

테스트케이스들의 형태는 클래스 내의 메소드의 형태로 작성되어있으나 클래스는 묶음역할만 할 뿐이고
실제로 실행될 테스트케이스는 method 단위입니다.

```python
# conftest.py

@pytest.fixture(scope="function", autouse=True)
def setup_and_teardown(request) -> webdriver:
    """
    driver 객체를 생성하고, 삭제합니다.
    class 단위로 실행되며, request 객체에 드라이버를 저장하여, 필요 시 request 객체에서 꺼내사용할 수 있습니다.
    :param request:
    :return:
    """

    platform = request.config.getoption('platform').lower()

    driver = driver_factory(platform)

    if platform == "web":
        driver.get("https://www.google.com/intl/ko/gmail/about/")

    request.cls.driver = driver

    if platform == "android":
        time.sleep(3)

    yield

    driver.quit()
    driver = None
    time.sleep(1)
```

드라이버 생성에 필요한 설정들은 `.ini` 파일에 저장한 설장값들을 `platform` 파라미터에 따라 분기처리 하고 있습니다.

`android`의 경우 실행 url을 별도로 설정해줍니다.
`web`의 경우 드라이버는 `webdriver_manager` 라이브러리를 사용하여 코드가 실행될 로컬 컴퓨터의 크롬버전에 맞추어 자동으로 드라이버가 설치되도록 하였습니다.
만일 로컬이 아니라 리모트나 별도의 device farm으로의 실행이 필요한 경우에는 아래 첨부한 코드중 `url_manager()` 에서 추가적인 분기처리를 할 수 있을 것입니다.

**현재 본 포트폴리오에서는 `android`의 경우는 드라이버 생성로직만 있으며 페이지클래스 및 테스트파일은 제거되어있는 상태입니다.**

```python
# utilities.py
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver as selenium_webdriver
from appium import webdriver as appium_driver

def driver_factory(platform: str):
    """
    platform값에 따라 생성해야할 드라이버 객체를 구분하여 리턴합니다.
    pc_web의 경우에는 ChromeDriverManager를 이용하여 자동으로 설치하도록 구현되어있습니다.
    리모트의 경우에는 다른 방법으로 설치해주어야합니다.
    :param platform: str
    :return:
    """
    if platform == "web":
        return selenium_webdriver.Chrome(
            options=desired_caps_manager(platform),
            service=ChromeService(ChromeDriverManager().install())
        )
    else:
        return appium_driver.Remote(
            url_manager(platform), options=desired_caps_manager(platform)
        )
```

```python
from appium.options.ios import XCUITestOptions
from appium.options.android import UiAutomator2Options
from selenium.webdriver.chrome.options import Options as WebChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver as selenium_webdriver
from appium import webdriver as appium_driver
from webdriver_manager.chrome import ChromeDriverManager

def url_manager(platform: str) -> str:
    """
    실행해야하는 url을 지정합니다.
    기본적으로는 로컬실행이고, web을 제외하는 경우는 appium server를 호출해야하므로 4723을 호출합니다.
    만약 리모트 실행을 하게 된다면 별도의 parameter로 분기처리가 필요하며, 호출주소 또한 localhost가 아닌 다른 주소를 선언해주어야 합니다.

    :param platform: str
    :return: str
    """
    if platform != "web":
        return "http://0.0.0.0:4723"


def desired_caps_manager(platform: str):
    """
    실행 시 드라이버에 설정한 desired_capabilties를 설정하는 함수입니다.
    실행하는 플랫폼에 따라 다르게 설정합니다.

    설정값들은 ./resources/desired_capabilities.ini 에서 읽어옵니다.
    :param platform:
    :return:
    """
    options = None

    if platform == "android":
        """
        안드로이드의 경우 기기 1대를 실행할 때에는 DEVICE_NAME, UDID는 지정해주지 않아도 되며,
        2대이상 실행이 필요한 경우에, 기기 구분을 위해 지정해주어야합니다.
        """
        options = UiAutomator2Options()
        desired_caps = config_factory("desired_capabilities")["ANDROID"]

        options.platform_name = desired_caps["PLATFORM_NAME"]
        options.automation_name = desired_caps["AUTOMATION_NAME"]
        options.app_activity = desired_caps["APP_ACTIVITY"]
        options.app_package = desired_caps["APP_PACKAGE"]
        options.device_name = desired_caps["DEVICE_NAME"]
        options.set_capability("appium:disableIdLocatorAutocompletion", True) #Gmail 앱 조작을 위한 설정값

    else:  # web
        """
        pc_web의 경우 시작 시에 최대화면설정을 하고, 시크릿모드를 활성화합니다.
        """
        options = WebChromeOptions()
        desired_caps = config_factory("desired_capabilities")["WEB"]

        options.add_argument("--start-fullscreen")
        options.add_argument("--incognito")
        options.add_argument(f"user-agent='{desired_caps['USER_AGENT']}'")
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument('--disable-blink-features=AutomationControlled')

    return options

```

`desired_capabilities.ini` 의 내용은 아래와 같습니다.

```ini
[WEB]
USER_AGENT = Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36

[ANDROID]
PLATFORM_NAME = Android
AUTOMATION_NAME = UiAutomator2
APP_ACTIVITY = com.google.android.gm.ConversationListActivityGmail
APP_PACKAGE = com.google.android.gm
```


---

## 테스트케이스 설계
실질적인 테스트를 수행하는 화면은 구글회원가입페이지에서의 `Google 계정만들기` 단계에서 부터 시작합니다.


### Happy case
- `tests/run/web/test_google_signup_happycase.py`

#### web
| No | Testcase method name                                  | remarks                                                                |
|----|-------------------------------------------------------|------------------------------------------------------------------------|
| 1  | step_check_home_image_and_click_login_button          | gmail 로고이미지를 확인하고 로그인 버튼을 클릭한다.                                        |
| 2  | step_check_login_page_and_click_create_account_button | 로그인페이지 내의 헤더텍슽르르 확인하고 개인용 계정만들기 버튼을 누른다.                               |
| 3  | step_check_and_input_name                             | `Google 계정만들기` 화면의 헤더텍스트를 확인하고 성과 이름을 입력한다.                            |
| 4  | step_check_and_input_birthday_and_gender              | `기본 정보` 화면의 헤더텍스트를 확인하고 생년월일과 성별 기본값을 입력한다.                            |
| 5  | step_check_and_create_mail_address                    | `Gmail 주소 선택하기` 화면의 헤더텍스트를 확인하고, `내 Gmail 주소 만들기` 를 클릭하여 임의의 주소를 입력한다. |
| 6  | step_check_and_create_password                        | `안전한 비밀번호 만들기` 화면의 헤더텍스트를 확인하고, 비밀번호와 비밀번호 확인란에 임의의 패스워드를 입력한다.        |
| 7  | step_check_phone_number_verification_title            | `보안문자 입력` 화면의 헤더텍스트를 확인한다.                                             |


### `Google 계정만들기` 단계
`Google 계정만들기` 단계에서부터 수행하는 테스트케이스는 `platform` 파라미터를 이용하여 로케이터를 구분해주면 테스트케이스 자체는 플랫폼 관계없이 동일하게 수행가능한 상태입니다. 
따라서 본 과제에서는 web 기준으로만 작성하였습니다.
- `tests/run/web/test_01_google_create_account.py`


|No|Testcase method name|remarks|
|---|---|---|
|1|test_create_account_not_input_name| 성과 이름을 아무것도 입력하지 않는 케이스|
|2|test_create_account_space_first_name| 이름 란에 공백을 넣는 케이스|
|3|test_create_account_space_between_character_first_name|성과 이름 사이에 공백을 넣는 케이스|
|4|test_create_account_special_character_first_name| 이름 란에 특수문자를 넣는 케이스|
|5|test_create_account_number_first_name|이름 란에 숫자를 넣는 케이스|
|6|test_create_account_character_and_number_first_name_1|이름란에 문자와 숫자를 넣는 케이스|
|7|test_create_account_character_and_number_first_name_2|이름란에 문자-숫자-문자 를 넣는 케이스|
|8|test_create_account_special_character_lastname_and_character_firstname| 성 란에 특수문자, 이름란에 문자를 넣는 케이스|
|9|test_create_account_special_character_lastname_and_number_firstname| 성 란에 특수문자, 이름 란에 숫자를 넣는 케이스

### `기본 정보` 단계
`기본 정보` 단계에서 수행하는 테스트케이스는, 일단 pairwise기법으로 각각의 입력들에 대한 조합들을 도출하였습니다. 케이스는 python의 `allpairspy` 를 사용하여 개별적으로 도출하였습니다.
- `tests/run/web/test_02_google_birthday_and_gender.py`

```text
    PAIRWISE:
         생년월일, 성별, (사용자 지정 입력 시) 커스텀 성별, 성별 대명사
     1: ['월', '남성', '없음', '없음']
     2: ['일', '공개안함', '없음', '없음']
     3: ['생년월일', '사용자 지정', '성별입력', '없음']
     4: ['생년월일', '공개안함', '없음', '없음']
     6: ['월', '공개안함', '없음', '없음']
     8: ['연도', '남성', '없음', '없음']
     9: ['월', '사용자 지정', '없음', '여성']
    10: ['일', '여성', '없음', '없음']
    11: ['일', '사용자 지정', '성별입력', '남성']
    12: ['연도', '사용자 지정', '성별입력', '기타']
    13: ['생년월일', '남성', '없음', '없음']
    14: ['생년월일', '여성', '없음', '없음']
    15: ['월', '여성', '없음', '없음']

```
이 이후에 각각의 입력란별로 테스트케이스를 작성하였으며, pairwise케이스와 중복되는 경우에는 docString에 명시하였습니다.

#### 생년월일 확인
|No|Testcase method name| remarks                                                 |
|---|---|---------------------------------------------------------|
|1|test_no_input_birthday_and_input_gender| 생년월일은 입력안하고 성별은 입력하는 케이스                                |
|2|test_no_input_year_and_other_input| 연도만 입력하고 나머지는 다 입력안하는 케이스                               |
|3|test_no_input_month_and_other_input| 생년월일 중 월 만 입력하고 나머지는 다 입력안하는 케이스                        |
|4|test_no_input_date_and_other_inpu| 생년월일 중 일 만 입력하고 나머지는 다 입력안하는 케이스                        |
|5|test_input_minus_year_and_other_input| 생년월일 중 연도를 마이너스 숫자로 입력하고 나머지는 다 정상값으로 입력하는 케이스          |
|6|test_input_past_old_year_and_other_input| 생년월일 중 연도를 아주 오래전 숫자로 입력하고 나머지를 다 정상값으로 입력하는 케이스        |
|7|test_input_three_character_year_and_other_input| 생년월일 중 연도를 세자리 숫자로 입력하고 나머지를 다 정상값으로 입력하는 케이스           |
|8|test_input_three_character_day_and_other_input| 생년월일 중 일 을 세자리 숫자로 입력하고 나머지는 다 정상값으로 입력하는 케이스           |
|9|test_input_leap_day_on_leap_year_and_other_inpu| 생년월일을 윤년의 날짜로 입력하고 나머지를 다 정상값으로 입력하는 케이스                |
|10|test_input_leap_day_on_not_leap_year_and_other_input| 생년월일을 윤년이 아닌 해에 윤년의 날짜(day)를 입력하고 나머지를 다 정상값으로 입력하는 케이스 |
|11|test_input_minus_day_and_other_input| 생년월일 중 일자를 마이너스 숫자를 넣고 나머지는 다 정상값으로 입력하는 케이스            |

#### 성별 확인
|No|Testcase method name|remarks|
|---|---|---|
|1|test_no_input_gender_and_other_input|성별을 입력 안하고 나머지는 다 정상값으로 입력하는 케이스|
|2|test_gender_woman_and_other_input| 성별을 여성으로 선택하고 나머지는 다 정상값으로 입력하는 케이스|
|3|test_not_open_and_other_input| 성별을 공개안함 으로 선택하고 나머지는 다 정상값으로 입력하는 케이스|
|4|test_custom_gender_no_input_and_other_input|성별을 사용자 지정 으로 선택하고, 사용자 지정성별은 입력하지 않고 나머지는 다 정상값으로 입력하는 케이스|
|5|test_custom_gender_character_and_no_input_genderpronoun_and_other_input|성별:사용자 지정 / 사용자 지정 성별은 입력하지만 성별 대명사는 입력하지 않는 경우|
#### 생년월일과 성별의 조합 확인
여기서 생년월일은, 기재한 값을 `입력하지 않습` 니다.

|No| 생년월일 / 성별선택 / 성별입력 / 성별대명사 |
|---|----------------------------|
|2| ['일', '공개안함', '없음', '없음']  |
|3|['생년월일', '사용자 지정', '성별입력', '없음']|
|4|['생년월일', '공개안함', '없음', '없음']|
|6|['월', '공개안함', '없음', '없음']|
|8|['연도', '남성', '없음', '없음']|
|9|['월', '사용자 지정', '없음', '여성']|
|10|['일', '여성', '없음', '없음']|
|11|['일', '사용자 지정', '성별입력', '남성']|
|12|['연도', '사용자 지정', '성별입력', '기타']
|13|['생년월일', '남성', '없음', '없음']|
|14|['생년월일', '여성', '없음', '없음']|
|15| ['월', '여성', '없음', '없음']|

#### 그 외 생년월일과 성별의 입력조합 확인
|No|Testcase method name|remarks|
|---|---|---|
|1|test_no_input_birthday_and_gender| 생년월일과 성별을 입력하지 않는 케이스|
|2|test_no_input_birthday_and_custom_gende| 생년월일과 사용자 지정 성별을 선택하고, 성별과 대명사는 입력하지 않는 케이스|
|3|test_custom_gender_character_and_no_input_genderpronoun_and_birthday|사용자 지정 성별을 선택하고, 성별은 입력하지만 생년월일과 대명사는 입력하지 않는 케이스|
|4|test_custom_gender_pronoun_and_other_no_input|사용자 지정 성별을 선택하고, 생별 대명사는 입력하고 생년월일과 성별 입력은 하지 않는 케이스 


### `Gmail 주소 선택하기` 단계

- `tests/run/web/test_03_google_mail_address.py`

또한 구글에서 제안해주는 자동생성되는 이메일 주소는 생략하였고, 무조건 `내 Gmail 주소 만들기` 를 선택하도록 하였습니다.

|No|Testcase method name|remarks|
|---|---|---|
|1|test_no_input_address|아무것도 입력하지 않는 케이스|
|2|test_input_blank_address|공백만 입력하는 케이스|
|3|test_input_special_character_address|특수문자만 입력하는 케이스|
|4|test_input_korean_address|한글만 입력하는 케이스|
|5|test_input_only_number_address|숫자만 입력하는 케이스|
|6|test_input_under_6_character_address|6자리 이하의 문자를 입력하는 경우|
|7|test_input_just_6_character_address|딱 6자리 문자를 입력하는 경우|
|8|test_input_just_30_character_address|딱 30자리 글자를 입력하는 경우|
|9|test_input_over_30_character_address|30자리 넘게 입력하는 경우|
|10|test_already_use_address|이미 사용중인 이메일 주소를 입력하는 경우|
|11|test_english_and_special_character_address|영어와 특수문자가 섞인 주소를 입력하는 경우|
|12|test_input_full_mail_address|도메인이 포함된 풀 주소를 입력하는 경우|
|13|test_input_only_upper_character_address|전부 대문자만 입력하는 경우|
|14|test_input_upper_and_lower_character_address|대소문자를 섞어서 입력하는 경우|
|15|test_input_upper_and_number_character_address|대문자와 숫자를 섞어 입력하는 경우|
|16|test_input_upper_and_number_and_dot_address|대문자, 구둣점과 숫자를 섞어 입력하는 경우|


### `안전한 비밀번호 만들기` 단계

- `tests/run/web/test_04_google_password.py`

|No|Testcase method name| remarks                                                                                   |
|---|---|-------------------------------------------------------------------------------------------|
|1|test_no_input_password_and_password_again| 아무것도 입력하지 않는 케이스                                                                          |
|2|test_input_password_and_no_password_again| 비밀번호는 입력하지만 비밀번호 확인을 입력하지 않는 케이스                                                          |
|3|test_input_password_and_no_password_again| 비밀번호는 입력하지않고 비밀번호 확인을 입력하는 케이스                                                            |
|4|test_input_password_and_input_different_password_again| 비밀번호와 비밀번호 확인을 다르게 입력하는 경우                                                                |
|5|test_input_blank_password_and_input_blank_password_again| 비밀번호와 비밀번호 확인을 공백을 입력하는 경우                                                                
|6|test_input_first_blank_and_character_password_and_password_again| 비밀번호 첫번째 글자를 공백으로 입력하늕 경우                                                                 |
|7|test_input_one_character_password_and_password_again| 비밀번호와 비밀번호 확인을 한 글자만 입력하는 경우                                                              |
|8|test_input_just_eight_character_password_and_password_again| 비밀번호와 비밀번호 확인을 8글자를 입력하는 경우                                                               |
|9|test_input_over_30_character_password_and_password_again| 비밀번호와 비밀번호 확인을 30글자 이상 입력하는 경우                                                            |
|10|test_just_english_character_password_and_password_again| 비밀번호를 영어만 입력하는 경우                                                                         |
|11|test_english_and_number_character_password_and_password_again| 비밀번호와 비밀번호 확인을 영어와 숫자를 섞어 입력하는 경우                                                         |
|12|test_special_character_and_number_character_password_and_password_again| 비밀번호와 비밀번호 확인을 특수문자와 숫자를 섞어 입력하는 경우                                                       |
|13|test_input_only_number_character_password_and_password_again| 비밀번호를 숫자만 입력하는 경우                                                                         |
|14|test_input_only_upper_english_character_password_and_password_again| 비밀번호를 대문자 영어만 입력하는 경우                                                                     |
|15|test_input_blank_between_character| 비밀번호로 입력하는 문자들 사이에 공백이 들어있는 경우                                                            |
|16|test_click_check_visible_password_and_check_password_and_password_again| 비밀번호 입력 후 비밀번호 표시를 눌렀을 때 내가 입력한 비밀번호가 제대로 입력되어있는지 확인하는 케이스                                |
|17|test_click_check_visible_password_and_input_wrong_pattern_password_1| 비밀번호 표시를 체크하고, 잘못된 패턴의 비밀번호를 입력 후에 비밀번호 표시 클릭 후 다음 버튼을 누르면 에러가 노출되고 입력필드가 클리어되는지 확인하는 케이스 |
|18|test_click_check_visible_password_and_input_wrong_pattern_password_2| 비밀번호 표시를 체크하고, 짧은 비밀번호를 입력한 후에 비밀번호 표시를 누르고 다음 버튼을 눌렀을 때, 클리어되지 않는 것을 확인                                 
|19|test_click_check_visible_password_and_input_wrong_pattern_password_3| 비밀번호 표시를 체크하고, 비밀번호와 비밀번호 확인이 일치하지 않을 때, 확인 필드가 클리어 되는 것을 확인|


---

## 그 외

### Logging
본 프로젝트에서는 파이썬 내장 로깅 라이브러리를 이용해 로그를 사용할 수 있습니다.

```python
# utilities.py
def logger_factory(class_name: str) -> logging.Logger:
    """
    logger 객체를 생성해서 리턴합니다.
    :param class_name: str
    :return:
    """
    logger = logging.getLogger(class_name)
    logger.setLevel(logging.INFO)

    return logger

```
위 함수에 대해 이미 `BasePage` 클래스에서 객체를 생성하고 있습니다. 따라서 `BasePage`를 상속받는 페이지들은 기본적으로 로깅을 사용할 수 있습니다.


```python
class BasePage:
    """
    BasePage 클래스는 페이지들에서 수행해야할 기본적인 행위들을 정의합니다.
    생성자에서는 드라이버, wait, logger 객체를 생성합니다.
    wait 객체는 기본 대기시간 10초입니다.

    """
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.logger = logger_factory(type(self).__name__)
```
실제 사용은 각각의 페이지클래스 내에서 로그를 남기고자 하는 곳에서 `self.logger` 객체를 이용하여 남길 수 있습니다.

```python
try:
    text = self._get_text((By.ID, "headingText"))
    self.logger.info("화면별 헤더 텍스트 : %s", text)
    if text == header_text:
        return True
    else:
        time.sleep(1)
```
기록되는 로그는 아래와 같이 `실행시간대 : 로그레벨 : 실행 클래스 : 실행 메소드 :실행 라인번호 - 로그내용` 으로 기록할 수 있습니다.

```text
2023-10-22 15:35:56 INFO [GoogleSignUpPage : check_title_text : line 43] - 화면별 헤더 텍스트 : Google 계정 만들기
2023-10-22 15:35:57 INFO [GoogleSignUpPage : check_title_sub_text : line 62] - 화면별 서브헤더 텍스트 : 생일과 성별을 입력하세요.
2023-10-22 15:36:00 INFO [GoogleSignUpPage : check_title_text : line 43] - 화면별 헤더 텍스트 : 기본 정보
2023-10-22 15:36:01 INFO [GoogleSignUpPage : check_title_sub_text : line 62] - 화면별 서브헤더 텍스트 : Gmail 주소를 선택하거나 새 Gmail 주소를 만드세요.
2023-10-22 15:36:02 INFO [GoogleSignUpPage : check_title_text : line 43] - 화면별 헤더 텍스트 : Gmail 주소 선택하기
2023-10-22 15:36:03 INFO [GoogleSignUpPage : check_title_sub_text : line 62] - 화면별 서브헤더 텍스트 : 문자, 숫자, 기호를 조합하여 안전한 비밀번호를 만드세요.
```

로깅의 포맷은 `pytest.ini`에 선언되어있습니다.

```ini
[pytest]
addopts = --color=no

log_format = %(asctime)s %(levelname)s [%(name)s : %(funcName)s : line %(lineno)d] - %(message)s
log_date_format = %Y-%m-%d %H:%M:%S
```

### Reporting and Screen capture
본 프로젝트에는 allure 라이브러리를 이용한 report생성이 가능합니다. 앞서 [말씀드린 것](#전제-조건) 처럼 리포트생성을 위해선 brew를 통해 별도로 allure 라이브러리가 설치되어있어야 합니다.

실행 시 커맨드라인에 `--alluredir={FILE_PATH_TO_SAVE_REPORT_AFTER_RUN_TEST}`를 넣어주면 됩니다.

allure report에는 생성된 로그들과 함께, 실패한 케이스에 대해서는 마지막 실행화면을 첨부할 수 있도록 되어있습니다.

```python
# conftest.py
_test_failed_incremental: Dict[str, Dict[Tuple[int, ...], str]] = {}

def pytest_runtest_makereport(item, call):
    """
    테스트가 실패했을 시에 리포트에 캡쳐를 첨부하도록 합니다.
    https://docs.pytest.org/en/7.1.x/example/simple.html?highlight=test_failed_incremental#incremental-testing-test-steps
    :param item:
    :param call:
    :return:
    """
    if call.excinfo is not None:
        # the test has failed
        # retrieve the class name of the test
        cls_name = str(item.cls)
        # retrieve the index of the test (if parametrize is used in combination with incremental)
        parametrize_index = (
            tuple(item.callspec.indices.values())
            if hasattr(item, "callspec")
            else ()
        )
        # retrieve the name of the test function
        test_name = item.originalname or item.name
        # store in _test_failed_incremental the original name of the failed test
        _test_failed_incremental.setdefault(cls_name, {}).setdefault(
            parametrize_index, test_name
        )
        allure.attach(
            item.cls.driver.get_screenshot_as_png(),
            "Screenshot",
            attachment_type=AttachmentType.PNG
        )
```

리포트 결과를 확인하려면, 확인 테스트케이스 실행 후, `--alluredir` 옵션으로 지정한 경로에 report파일이 생성한 것을 확인한 후에 아래 커맨드를 실행해주세요. `brew`로 `allure` 라이브러리가 설치되어있어야 합니다.
`allure serve {저장한 리포트 경로}`

![](https://velog.velcdn.com/images/dahunyoo/post/20233a5f-5701-42f4-9d22-92d1ca3682a0/image.png)