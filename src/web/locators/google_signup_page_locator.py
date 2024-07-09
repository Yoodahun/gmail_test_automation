from selenium.webdriver.common.by import By


class GoogleSignUpPageLocator():

    BUTTON_NEXT = (By.XPATH, '//span[contains(text(), "다음")]//parent::button')

    INPUT_LAST_NAME_FIELD = (By.ID, 'lastName')
    INPUT_FIRST_NAME_FIELD = (By.ID, 'firstName')

    INPUT_YEAR_FIELD = (By.ID, 'year')
    SELECT_MONTH_FIELD = (By.ID, 'month')
    INPUT_DAY_FIELD = (By.ID, 'day')
    SELECT_GENDER_FIELD = (By.ID, 'gender')
    INPUT_CUSTOM_GENDER_FIELD = (By.ID, 'customGender')

    LABEL_CREATE_MY_GMAIL_ADDRESS = (By.XPATH, '//div[contains(@id, "selection") and contains(text(), "Gmail 주소 만들기")]')
    INPUT_GMAIL_ADDRESS_FIELD = (By.NAME, 'Username')
    ADDRESS_ERROR_MESSAGE = (By.XPATH, '//div[contains(text(), "문자, 숫자, 마침표")]/following-sibling::div//div')

    INPUT_PASSWORD_FILED = (By.NAME, 'Passwd')
    INPUT_PASSWORD_CONFIRM_FILED = (By.NAME, 'PasswdAgain')
    CHECKBOX_VIEW_PASWORD = (By.XPATH, '//div[contains(@id, "selection")]')
    PASSWORD_ERROR_MESSAGE = (By.XPATH, '//div[@id="confirm-passwd"]/../../../../following-sibling::div//span')

    WARNING_MESSAGE = (By.XPATH, '//div[@aria-atomic="true" and @aria-live="assertive"]//div')



