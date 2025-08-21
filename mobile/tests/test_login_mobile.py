import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from mobile.pages.login import Login
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

def test_login_success(driver):
    login = Login(driver)

    login.enter_company_id("5049209")
    login.enter_username("qatestsalesman")
    login.enter_password("it.QA2025")
    login.click_login()
    time.sleep(15)

    assert login.get_success_login(), "Dashboard should be visible."
    time.sleep(5)

def test_login_invalid_company_id(driver):
    login = Login(driver)

    login.enter_company_id("504920912")
    login.enter_username("qatestsalesman")
    login.enter_password("it.QA2025")
    login.click_login()

    time.sleep(5)
    assert login.get_error_message(), "Error message should be visible."
    login.click_OK_message()

def test_login_invalid_username(driver):
    login = Login(driver)

    login.enter_company_id("5049209")
    login.enter_username("qatestsalesman01")
    login.enter_password("it.QA2025")
    login.click_login()

    time.sleep(5)
    assert login.get_error_message(), "Error message should be visible."
    login.click_OK_message()

def test_login_invalid_password(driver):
    login = Login(driver)

    login.enter_company_id("5049209")
    login.enter_username("qatestsalesman")
    login.enter_password("it.QA202525")
    login.click_login()

    time.sleep(5)
    assert login.get_error_message(), "Error message should be visible."
    login.click_OK_message()

def test_login_invalid_company_id_username_password(driver):
    login = Login(driver)

    login.enter_company_id("504920912")
    login.enter_username("qatestsalesman01")
    login.enter_password("it.QA202525")
    login.click_login()

    time.sleep(5)
    assert login.get_error_message(), "Error message should be visible."
    login.click_OK_message()