from appium.webdriver.common.appiumby import AppiumBy


class GmailHomePageLocator:

    GMAIL_HOME_CONFIRM_BUTTON = (AppiumBy.ID, "com.google.android.gm:id/welcome_tour_got_it")
    ADD_NEW_EMAIL_ADDRESS_BUTTON = (AppiumBy.ID, "com.google.android.gm:id/setup_addresses_add_another")
    ADD_NEW_GOOGLE_ADDRESS_BUTTON = (AppiumBy.XPATH, '//android.widget.TextView[@text="Google"]')