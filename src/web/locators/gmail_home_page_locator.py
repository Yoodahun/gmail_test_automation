from selenium.webdriver.common.by import By


class GmailHomePageLocator:
    HOME_IMAGE = (By.XPATH, "//a[contains(@class, 'header__logo')]")
    LOGIN_BUTTON = (By.XPATH, "//a[contains(@href, 'accounts.google.com/AccountChooser')]")
