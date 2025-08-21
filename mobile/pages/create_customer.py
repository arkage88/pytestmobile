from mobile.locators.create_customer import CreateCustomerLocators

class CreateCustomer:
    def __init__(self, driver):
        self.driver = driver
        self.locators = CreateCustomerLocators

    def click_new_customer(self):
        self.driver.find_element(*self.locators.NEW_CUSTOMER).click()

    def click_new_customer_registration(self):
        self.driver.find_element(*self.locators.NEW_CUSTOMER_REGISTRATION).click()

    def enter_outlet_name(self, outlet_name):
        self.driver.find_element(*self.locators.OUTLET_NAME).send_keys(outlet_name)

    def enter_outlet_phone(self, phone):
        self.driver.find_element(*self.locators.OUTLET_PHONE).send_keys(phone)

    def enter_outlet_email(self, email):
        self.driver.find_element(*self.locators.OUTLET_EMAIL).send_keys(email)

    def enter_contact_person(self, contact_person):
        self.driver.find_element(*self.locators.CONTACT_PERSON).send_keys(contact_person)

        self.driver.swipe(582, 1385, 608, 500)
    def click_channel_type(self):
        self.driver.find_element(*self.locators.CHANNEL_TYPE).click()

    def click_mt(self):
        self.driver.find_element(*self.locators.MT).click()

    def click_customer_type(self):
        self.driver.find_element(*self.locators.CUSTOMER_TYPE).click()

    def click_grosir(self):
        self.driver.find_element(*self.locators.GROSIR).click()


    def click_pricelist(self):
        self.driver.find_element(*self.locators.PRICELIST).click()

    def click_default(self):
        self.driver.find_element(*self.locators.DEFAULT).click()

    def click_continue(self):
        self.driver.find_element(*self.locators.CONTINUE).click()

    def click_new_customer_registration(self):
        self.driver.find_element(*self.locators.NEW_CUSTOMER_REGISTRATION).click()
