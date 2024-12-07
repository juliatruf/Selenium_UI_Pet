import pytest
import time

from config import LOGIN_URL, USER_PROFILE_URL, valid_credentials, invalid_credentials
from pages.login_page import LoginPage

@pytest.mark.smoke
@pytest.mark.parametrize('email, password', valid_credentials)
def test_valid_login(browser, email, password):
    page = LoginPage(browser, LOGIN_URL)
    page.open()
    page.go_to_login(email)
    page.go_to_password(password)
    page.go_to_submit_button()
    time.sleep(1)
    expected_url = USER_PROFILE_URL
    actual_url = browser.current_url
    browser.save_screenshot('result5.png')
    assert actual_url == expected_url, f"URL mismatch! Expected: {expected_url}, got: {actual_url}"

@pytest.mark.regression
@pytest.mark.parametrize('email, password', invalid_credentials)
def test_invalid_login(browser, email, password):
    page = LoginPage(browser, LOGIN_URL)
    page.open()
    page.go_to_login(email)
    page.go_to_password(password)
    page.go_to_submit_button()
    time.sleep(1)
    browser.save_screenshot('result6.png')
    actual_url = browser.current_url
    error_element = page.go_to_error_message()
    actual_error_message = error_element.text
    expected_error_message = "Something went wrong"
    assert error_element.is_displayed(), "No error message is shown!"
    assert actual_error_message == expected_error_message, f"Unexpected error message: {actual_error_message}"
    assert actual_url == LOGIN_URL, f"User was redirected from login page to {actual_url}"
    assert actual_url != USER_PROFILE_URL, "User was unexpectedly logged in!"
