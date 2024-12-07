import pytest
import time

from config import MAIN_URL, LOGIN_URL, DROPDOWN_PET_TYPE_OPTIONS
from pages.main_page import MainPage


def test_go_to_login_page(browser):
    page = MainPage(browser, MAIN_URL)
    page.open()
    page.go_to_login_page()
    time.sleep(2)
    expected_url = LOGIN_URL
    actual_url = browser.current_url
    browser.save_screenshot('result7.png')
    assert actual_url == expected_url, f"URL mismatch! Expected: {expected_url}, got: {actual_url}"

@pytest.mark.regression
@pytest.mark.parametrize("pet_type", DROPDOWN_PET_TYPE_OPTIONS)
def test_filter_by_pet_type_pets_exist(browser, pet_type):
    page = MainPage(browser, MAIN_URL)
    page.open()
    page.open_dropdown_pet_type()
    time.sleep(1)
    page.select_pet_type_option(pet_type['index'])
    browser.save_screenshot('result8.png')
    pet_type_filter_result = page.get_all_pets_types()
    expected_pet_type = pet_type['pet_type_option']
    assert len(pet_type_filter_result) == 1 and expected_pet_type in pet_type_filter_result, \
        f"Expected: {expected_pet_type}, but got: {pet_type_filter_result}"


@pytest.mark.regression
@pytest.mark.parametrize("pet_name", ["bik", "Bobik"])
def test_filter_by_pet_name_existing_names(browser, pet_name):
    page = MainPage(browser, MAIN_URL)
    page.open()
    page.enter_pet_name(pet_name)
    browser.save_screenshot('result9.png')
    pet_name_filter_result = page.get_all_pets_names()
    actual_result = False
    for item in pet_name_filter_result:
        if pet_name not in item:
            actual_result = False
            break
        else:
            actual_result = True
    assert actual_result, f"Expected: Substring {pet_name}, but got: {pet_name_filter_result}"
