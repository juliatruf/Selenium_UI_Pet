import time
import pytest

from config import CREATE_PET_PAGE_URL, DROPDOWN_PET_TYPE_OPTIONS, USER_PROFILE_URL, TEST_USER_WITHOUT_PETS
from pages.pet_create_page import PetCreatePage
from pages.user_profile_page import UserProfilePage


@pytest.mark.xfail
@pytest.mark.parametrize("login", TEST_USER_WITHOUT_PETS, indirect=True)
@pytest.mark.parametrize("pet_type", DROPDOWN_PET_TYPE_OPTIONS)
@pytest.mark.parametrize("pet_name", ["Kesha"])
def test_create_pet_with_selected_type(browser, login, pet_type, pet_name):
    page = UserProfilePage(browser, USER_PROFILE_URL)
    initial_pet_number = page.get_pets_list_length()
    assert initial_pet_number == 0, (f"The pet list was expected to be empty, "
                                     f"but contains {initial_pet_number}")
    page = PetCreatePage(browser, CREATE_PET_PAGE_URL)
    page.open()
    page.go_to_pet_name(pet_name)
    page.open_pet_type_dropdown()
    page.select_pet_type_option(pet_type['index'])
    page.go_to_submit_button()
    page.go_to_add_pet_image_button("utils/dog_1.jpg")
    page = UserProfilePage(browser, USER_PROFILE_URL)
    page.open()
    final_pet_number = page.get_pets_list_length()
    actual_pet_type = page.get_pet_type()
    expected_pet_type = pet_type['pet_type_option']
    assert final_pet_number == 1, "The pet has not been created"
    assert actual_pet_type == expected_pet_type, f"Pets type mismatch: expected {expected_pet_type}, got {actual_pet_type}"
    page.go_to_delete_pet_button()
    time.sleep(5)
    page.go_to_confirm_delete_pet_button()
    time.sleep(5)
    assert page.go_to_empty_pet_message().is_displayed(), "The created pet has not been deleted"
