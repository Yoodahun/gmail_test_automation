from typing import List

from appium.webdriver import Remote, WebElement
from selenium.common import TimeoutException
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC

from utilities import logger_factory


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

    def _find_element(self, locator: tuple) -> WebElement:
        """
        find_element를 수행하여 element를 return합니다.

        :param locator:
        :return:
        """
        return self.driver.find_element(*locator)

    def _find_elements(self, locator: tuple) -> List[WebElement]:
        """
        find_elements를 수행하여 list형태의 element들을 리턴합니다.
        :param locator:
        :return: List[WebElement]
        """
        return self.driver.find_elements(*locator)

    def _find_element_for_wait(self, locator: tuple) -> WebElement:
        """
        wait를 이용하여 element를 식별하고, 리턴합니다.
        대기시간은 10초이며 조건은 visibility_of_element_located() 입니다.
        :param locator:
        :return: WebElement
        """
        return self.wait.until(EC.visibility_of_element_located(locator))

    def _find_elements_for_wait(self, locator: tuple) -> List[WebElement]:
        """
        wait를 이용하여 element를 식별하고, 찾아낸 element들을 list에 담아 리턴합니다.
        대기시간은 10초이며 조건은 visibility_of_elements_located() 입니다.
        :param locator:
        :return:
        """
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    def _get_text(self, locator: tuple) -> str:
        """
        wait를 이용하여 element를 식별한다음, text를 리턴합니다.

        :param locator:
        :return: str
        """
        text = self._find_element_for_wait(locator).text
        self.logger.info(f"text : {text}")
        return text

    def _input(self, locator: tuple, text: str):
        """
        wait를 이용하여 element를 식별한 다음, 텍스트값을 입력합니다.


        :param locator:
        :param text:
        :return:
        """
        input_element = self._find_element_for_wait(locator)
        input_element.send_keys(text)

    def _click(self, locator: tuple):
        """
        wait를 이용하여 element를 식별한다음, click()을 수행합니다.
        :param locator:
        :return:
        """
        self._find_element_for_wait(locator).click()

    def _is_visible(self, locator: tuple) -> bool:
        """
        wait를 이용하여 element를 식별한다음 is_displayed()를 수행합니다.
        TimeoutException이 발생하는 경우에는 False를 리턴합니다.

        :param locator:
        :return: bool
        """
        try:
            return self._find_element_for_wait(locator).is_displayed()
        except TimeoutException:
            return False

    def _get_select_tag_element(self, locator: tuple) -> Select:
        """
        wait를 이용하여 element를 식별한다음, Select객체를 생성하여 리턴합니다.

        :param locator:
        :return: selenium.webdriver.support.select.Select
        """
        return Select(self._find_element_for_wait(locator))

