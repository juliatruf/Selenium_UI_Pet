import pytest
import time
from selenium import webdriver
from config import LOGIN_URL, USER_PROFILE_URL
from pages.login_page import LoginPage


@pytest.fixture(autouse=True)
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

@pytest.fixture
def login(browser, request):
    user = request.param
    login_page = LoginPage(browser, LOGIN_URL)
    login_page.open()
    login_page.go_to_login(user['email'])
    login_page.go_to_password(user['password'])
    login_page.go_to_submit_button()
    time.sleep(2)
    assert browser.current_url == USER_PROFILE_URL, "Login failed!"
    return user
