import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from mobile.pages.login import Login
from mobile.pages.create_customer import CreateCustomer

from appium.options.android import UiAutomator2Options
import time

@pytest.fixture
def driver():
    options = UiAutomator2Options().load_capabilities({
        "platformName": "Android",
        "appium:automationName": "UiAutomator2",
        "appium:deviceName": "Android Device",
        "appium:udid": "c2890ca8",
        "appium:appPackage": "id.edot.ework",
        "appium:appActivity": "id.edot.onboarding.ui.splash.SplashScreenActivity",
        "appium:noReset": False,
        "appium:autoGrantPermissions": True,
        "appium:gpsEnabled": True,

    })

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)
    yield driver
    driver.quit()

def test_login_success_create_customer(driver):
    login = Login(driver)
    customer = CreateCustomer(driver)

    login.enter_company_id("5049209")
    login.enter_username("qatestsalesman")
    login.enter_password("it.QA2025")
    login.click_login()
    time.sleep(15)

    assert login.get_success_login(), "Dashboard should be visible."
    time.sleep(5)

    customer.click_new_customer()
    time.sleep(5)
    customer.click_new_customer_registration()
    time.sleep(5)
    customer.enter_outlet_name("test")
    customer.enter_outlet_phone("084847433744")
    customer.enter_outlet_email("test@gmail.com")
    customer.enter_contact_person("test")
    time.sleep(5)
    customer.click_channel_type()
    customer.click_mt()
    customer.click_customer_type()
    time.sleep(5)
    customer.click_grosir()
    time.sleep(5)
    customer.click_pricelist()
    time.sleep(5)
    customer.click_default()
    time.sleep(5)
    customer.click_continue()