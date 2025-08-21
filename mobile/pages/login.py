from mobile.locators.login import LoginLocators

class Login:
    def __init__(self, driver):
        self.driver = driver
        self.locators = LoginLocators

    def enter_company_id(self, company_id):
        self.driver.find_element(*self.locators.COMPANY_ID_INPUT).send_keys(company_id)
    def enter_username(self, username):
        self.driver.find_element(*self.locators.USERNAME_INPUT).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.locators.PASSWORD_INPUT).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.locators.LOGIN_BUTTON).click()

    def get_success_login(self):
        return self.driver.find_element(*self.locators.SUCCESS_LOGIN).text

    def get_error_message(self):
        return self.driver.find_element(*self.locators.ERROR_MESSAGE).text

    def click_OK_message(self):
        self.driver.find_element(*self.locators.OK_ERROR).click()

