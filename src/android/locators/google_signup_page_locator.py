from appium.webdriver.common.appiumby import AppiumBy


class GoogleSignUpPageLocator():

    BUTTON_NEXT = (AppiumBy.XPATH, '//android.widget.Button[@text="다음"]')

    INPUT_LAST_NAME_FIELD = (AppiumBy.ID, 'lastName')
    INPUT_FIRST_NAME_FIELD = (AppiumBy.ID, 'firstName')

    INPUT_YEAR_FIELD = (AppiumBy.ID, 'year')
    SELECT_MONTH_FIELD = (AppiumBy.ID, 'month-label')
    INPUT_DAY_FIELD = (AppiumBy.ID, 'day')
    SELECT_GENDER_FIELD = (AppiumBy.ID, 'gender')
    INPUT_CUSTOM_GENDER_FIELD = (AppiumBy.ID, 'customGender')

    LABEL_CREATE_MY_GMAIL_ADDRESS = (AppiumBy.XPATH, '//android.widget.TextView[contains(@resource-id, "selection") and contains(@text, "Gmail 주소 만들기")]')
    INPUT_GMAIL_ADDRESS_FIELD = (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="domainSuffix"]/preceding-sibling::android.view.View//android.widget.EditText')
    ADDRESS_ERROR_MESSAGE = (AppiumBy.XPATH, '//div[contains(text(), "문자, 숫자, 마침표")]/following-sibling::div//div')

    INPUT_PASSWORD_FILED = (AppiumBy.XPATH, '//android.view.View[@resource-id="password"]//android.widget.EditText')
    INPUT_PASSWORD_CONFIRM_FILED = (AppiumBy.NAME, 'PasswdAgain')
    CHECKBOX_VIEW_PASWORD = (AppiumBy.XPATH, '//div[contains(@id, "selection")]')
    PASSWORD_ERROR_MESSAGE = (AppiumBy.XPATH, '//*[local-name()="svg"]/parent::div/following-sibling::div//span')

    WARNING_MESSAGE = (AppiumBy.XPATH, '//div[@aria-atomic="true" and @aria-live="assertive"]//div')
