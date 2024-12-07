from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#app > header > div > ul > li:nth-child(1) > a > span")
    PET_TYPE_DROPDOWN = (By.XPATH, "//div[@id='pv_id_2']/div/span")
    PET_TYPE_DROPDOWN_ITEMS = (By.CLASS_NAME, 'p-dropdown-item')
    PET_PROFILE_PET_TYPE = (By.CSS_SELECTOR, "span.product-category")
    PET_NAME_INPUT = (By.CSS_SELECTOR, "#petName")
    PET_PROFILE_NAME = (By.CSS_SELECTOR, "div.product-name")
    NEXT_PAGE_PAGINATOR_ENABLED = (By.CSS_SELECTOR, ".p-paginator-next.p-paginator-element.p-link")

class LoginPageLocators:
    LOGIN_EMAIL = (By.ID, 'login')
    LOGIN_PASSWORD = (By.CSS_SELECTOR, '#password > input')
    LOGIN_BUTTON = (By.CLASS_NAME, 'p-button-label')
    LOGIN_ERROR_MESSAGE = (By.CSS_SELECTOR, '.p-message-text')

class UserProfilePageLocators:
    LOGO_LINK = (By.CLASS_NAME,'p-menubar-start')
    CREATE_PET_BUTTON = (By.CSS_SELECTOR, '#app > main > div > div > div.p-dataview-header > div > div:nth-child(1) '
                                          '> button')
    EMPTY_PET_LIST_MESSAGE = (By.CLASS_NAME, 'p-dataview-emptymessage')
    EDIT_PET_BUTTON = (By.CSS_SELECTOR, '#app > main > div > div > div.p-dataview-content > div > div:nth-child(1) '
                                        '> div > div.product-list-action > button:nth-child(1)')
    DELETE_PET_BUTTON = (By.CSS_SELECTOR, '#app > main > div > div > div.p-dataview-content > div > div:nth-child(1)'
                                          ' > div > div.product-list-action > button.p-button.p-component.p-button-danger')
    DELETE_CONFIRM_POPUP = (By.CSS_SELECTOR, ".p-confirm-popup.p-component.p-ripple-disabled")
    CANCEL_DELETE_PET_BUTTON = (By.CSS_SELECTOR, "button.p-button.p-component.p-confirm-popup-reject.p-button-sm.p-button-text")
    CONFIRM_DELETE_PET_BUTTON = (By.CSS_SELECTOR, "button.p-button.p-component.p-confirm-popup-accept.p-button-sm")
    PETS_LIST = (By.CLASS_NAME, 'product-list-item')
    PET_TYPE = (By.XPATH, "//span[@class='product-category']")

class PetCreatePageLocators:
    PET_CREATE_NAME = (By.ID, 'name')
    PET_CREATE_TYPE_DROPDOWN = (By.ID, 'typeSelector')
    PET_CREATE_TYPE_DROPDOWN_ITEMS = (By.CLASS_NAME, 'p-dropdown-item')
    PET_CREATE_SUBMIT = (By.CSS_SELECTOR, 'button.p-button.p-component.p-button-success')
    PET_CREATE_ADD_IMAGE = (By.CSS_SELECTOR, 'span.p-button.p-component.p-fileupload-choose')
