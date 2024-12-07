import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from selenium.common import NoSuchElementException

from pages.base_page import BasePage
from pages.locators import MainPageLocators


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def open_dropdown_pet_type(self):
        pet_type_dropdown = self.browser.find_element(*MainPageLocators.PET_TYPE_DROPDOWN)
        pet_type_dropdown.click()

    def select_pet_type_option(self, index):
        dropdown_items = self.browser.find_elements(*MainPageLocators.PET_TYPE_DROPDOWN_ITEMS)
        self.browser.execute_script("arguments[0].scrollIntoView(true);", dropdown_items[index])
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.element_to_be_clickable(dropdown_items[index]))
        dropdown_items[index].click()

    def enter_pet_name(self, search_query):
        pet_name_input = self.browser.find_element(*MainPageLocators.PET_NAME_INPUT)
        pet_name_input.send_keys(search_query, Keys.ENTER)

    def paginate_and_collect(self, element_locator, next_page_locator):
        all_elements = []
        while True:
            elements_on_page = self.browser.find_elements(*element_locator)
            elements_on_page_text = [element.text for element in elements_on_page]
            all_elements.extend(elements_on_page_text)
            try:
                next_button = self.browser.find_element(*next_page_locator)
                if not next_button.is_enabled():
                    break
                next_button.click()
                time.sleep(1)
            except NoSuchElementException:
                break
        return all_elements

    def get_all_pets_types(self):
        element_locator = MainPageLocators.PET_PROFILE_PET_TYPE
        next_page_locator = MainPageLocators.NEXT_PAGE_PAGINATOR_ENABLED
        pet_profile_pet_type_text = self.paginate_and_collect(element_locator, next_page_locator)
        return set(pet_profile_pet_type_text)

    def get_all_pets_names(self):
        element_locator = MainPageLocators.PET_PROFILE_NAME
        next_page_locator = MainPageLocators.NEXT_PAGE_PAGINATOR_ENABLED
        pet_profile_pet_name_text = self.paginate_and_collect(element_locator, next_page_locator)
        return set(pet_profile_pet_name_text)
