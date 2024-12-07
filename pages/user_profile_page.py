from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from pages.locators import UserProfilePageLocators


class UserProfilePage(BasePage):
    def go_to_empty_pet_message(self):
        empty_pet_message = self.browser.find_element(*UserProfilePageLocators.EMPTY_PET_LIST_MESSAGE)
        return empty_pet_message

    def go_to_create_pet_button(self):
        create_pet_button = self.browser.find_element(*UserProfilePageLocators.CREATE_PET_BUTTON)
        create_pet_button.click()

    def go_to_edit_pet_button(self):
        edit_pet_button = self.browser.find_element(*UserProfilePageLocators.EDIT_PET_BUTTON)
        edit_pet_button.click()

    def go_to_delete_pet_button(self):
        delete_pet_button = self.browser.find_element(*UserProfilePageLocators.DELETE_PET_BUTTON)
        delete_pet_button.click()

    def go_to_confirm_delete_pet_button(self):
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.element_to_be_clickable(UserProfilePageLocators.DELETE_CONFIRM_POPUP))
        modal_confirm_delete_pet_button = self.browser.find_element(*UserProfilePageLocators.CONFIRM_DELETE_PET_BUTTON)
        modal_confirm_delete_pet_button.click()

    def go_to_cancel_delete_pet_button(self):
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.element_to_be_clickable(UserProfilePageLocators.DELETE_CONFIRM_POPUP))
        modal_cancel_delete_pet_button = self.browser.find_element(*UserProfilePageLocators.CANCEL_DELETE_PET_BUTTON)
        modal_cancel_delete_pet_button.click()

    def get_pets_list_length(self):
        pets_list = self.browser.find_elements(*UserProfilePageLocators.PETS_LIST)
        return len(pets_list)

    def get_pet_type(self):
        pet_type_list = self.browser.find_elements(*UserProfilePageLocators.PET_TYPE)
        pet_type = pet_type_list[-1]
        return pet_type.text
