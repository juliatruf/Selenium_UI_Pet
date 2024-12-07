from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def go_to_login(self, email):
        login_email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        login_email.send_keys(email)

    def go_to_password(self, password):
        login_password = self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD)
        login_password.send_keys(password)

    def go_to_submit_button(self):
        login_button = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_button.submit()

    def go_to_error_message(self):
        login_error_message = self.browser.find_element(*LoginPageLocators.LOGIN_ERROR_MESSAGE)
        return login_error_message
