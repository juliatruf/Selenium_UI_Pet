import re
import time
import pytest

from config import (USER_PROFILE_URL, CREATE_PET_PAGE_URL, EDIT_PET_PAGE_URL_PATTERN, TEST_USER_WITHOUT_PETS,
                    TEST_USER_2_PETS)
from pages.user_profile_page import UserProfilePage


@pytest.mark.regression
@pytest.mark.parametrize("login", TEST_USER_WITHOUT_PETS, indirect=True)
def test_go_to_create_pet_page(browser, login):
    page = UserProfilePage(browser, USER_PROFILE_URL)
    page.open()
    page.go_to_create_pet_button()
    time.sleep(1)
    expected_url = CREATE_PET_PAGE_URL
    actual_url = browser.current_url
    browser.save_screenshot('result10.png')
    assert actual_url == expected_url, f"URL mismatch! Expected: {expected_url}, got: {actual_url}"


@pytest.mark.skip
@pytest.mark.parametrize("login", TEST_USER_2_PETS, indirect=True)
def test_go_to_pet_edit_page(browser, login):
    page = UserProfilePage(browser, USER_PROFILE_URL)
    page.open()
    initial_pet_number = page.get_pets_list_length()
    assert initial_pet_number == 2, (f"Cannot proceed: the number of pets in the list is not 2, "
                                     f"but {initial_pet_number}")
    page.go_to_edit_pet_button()
    time.sleep(1)
    expected_url = EDIT_PET_PAGE_URL_PATTERN
    actual_url = browser.current_url
    browser.save_screenshot('result11.png')
    assert re.match(expected_url, actual_url), f"URL mismatch! Expected: {expected_url}, got: {actual_url}"


@pytest.mark.regression
@pytest.mark.parametrize("login", TEST_USER_2_PETS, indirect=True)
def test_cancel_delete_pet(browser, login):
    page = UserProfilePage(browser, USER_PROFILE_URL)
    page.open()
    initial_pet_number = page.get_pets_list_length()
    assert initial_pet_number == 2, (f"Cannot proceed: the number of pets in the list is not 2, "
                                     f"but {initial_pet_number}")
    page.go_to_delete_pet_button()
    browser.save_screenshot('result12.png')
    page.go_to_cancel_delete_pet_button()
    time.sleep(1)
    actual_pet_number = page.get_pets_list_length()
    browser.save_screenshot('result13.png')
    assert actual_pet_number == initial_pet_number, f"The pet has been unexpectedly deleted"


@pytest.mark.smoke
@pytest.mark.parametrize("login", TEST_USER_2_PETS, indirect=True)
def test_confirm_delete_pet(browser, login):
    page = UserProfilePage(browser, USER_PROFILE_URL)
    page.open()
    initial_pet_number = page.get_pets_list_length()
    assert initial_pet_number == 2, (f"Cannot proceed: the number of pets in the list is not 2, "
                                     f"but {initial_pet_number}")
    page.go_to_delete_pet_button()
    browser.save_screenshot('result14.png')
    page.go_to_confirm_delete_pet_button()
    time.sleep(1)
    actual_pet_number = page.get_pets_list_length()
    browser.save_screenshot('result15.png')
    assert actual_pet_number == 1, f"The pet has not been deleted"
