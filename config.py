MAIN_URL = 'http://34.141.58.52:8080/#/'
LOGIN_URL = 'http://34.141.58.52:8080/#/login'
USER_PROFILE_URL = "http://34.141.58.52:8080/#/profile"
CREATE_PET_PAGE_URL = 'http://34.141.58.52:8080/#/pet-new/pet'
EDIT_PET_PAGE_URL_PATTERN = r"http://34\.141\.58\.52:8080/#/pet-edit/\d+"


DROPDOWN_PET_TYPE_OPTIONS = [
    {"index": 0, "pet_type_option": "dog"},
    {"index": 1, "pet_type_option": "cat"},
    {"index": 2, "pet_type_option": "reptile"},
    {"index": 3, "pet_type_option": "hamster"},
    {"index": 4, "pet_type_option": "parrot"}
]


TEST_USER_WITHOUT_PETS = [
    {"email": "test1@mail.com", "password": "1234"}
]


TEST_USER_2_PETS = [
    {"email": "test2j@mail.com", "password": "12345"}
]


valid_credentials = [
    ("test1@mail.com", "1234")
]


invalid_credentials = [
    ("user_not_exist@mail.com", "1234"),
    ("test1@mail.com", "wrongpassword")
]
