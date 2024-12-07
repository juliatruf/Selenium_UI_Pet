from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from pages.locators import PetCreatePageLocators


class PetCreatePage(BasePage):
    def go_to_pet_name(self, pet_name):
        pet_name_input = self.browser.find_element(*PetCreatePageLocators.PET_CREATE_NAME)
        pet_name_input.send_keys(pet_name)

    def open_pet_type_dropdown(self):
        create_pet_type_dropdown = self.browser.find_element(*PetCreatePageLocators.PET_CREATE_TYPE_DROPDOWN)
        create_pet_type_dropdown.click()

    def select_pet_type_option(self, index):
        dropdown_items = self.browser.find_elements(*PetCreatePageLocators.PET_CREATE_TYPE_DROPDOWN_ITEMS)
        self.browser.execute_script("arguments[0].scrollIntoView(true);", dropdown_items[index])
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.element_to_be_clickable(dropdown_items[index]))
        dropdown_items[index].click()

    def go_to_submit_button(self):
        create_pet_confirm_button = self.browser.find_element(*PetCreatePageLocators.PET_CREATE_SUBMIT)
        create_pet_confirm_button.submit()

    def go_to_add_pet_image_button(self, pet_image):
        add_pet_image_button = self.browser.find_element(*PetCreatePageLocators.PET_CREATE_ADD_IMAGE)
        add_pet_image_button.send_keys(pet_image)
