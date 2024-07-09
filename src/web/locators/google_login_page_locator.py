from selenium.webdriver.common.by import By


class GoogleLoginPageLocator:
    LOGIN_PAGE_HEADER_TEXT = (By.ID, "headingText")

    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[@aria-expanded='false']")
    CREATE_ACCOUNT_OPTION_PERSONAL = (By.XPATH, '//span[contains(text(), "개인용")]//parent::li')
