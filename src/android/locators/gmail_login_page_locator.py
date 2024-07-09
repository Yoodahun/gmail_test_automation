from appium.webdriver.common.appiumby import AppiumBy


class GmailLoginPageLocator:
    LOGIN_PAGE_HEADER_TEXT = (AppiumBy.ID, "headingText")

    CREATE_ACCOUNT_BUTTON = (AppiumBy.XPATH, "//android.widget.Button[@text='계정 만들기']")
    CREATE_ACCOUNT_OPTION_PERSONAL = (AppiumBy.XPATH, '//android.view.MenuItem[@text="개인용"]')
