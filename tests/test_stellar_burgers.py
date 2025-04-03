from selenium.webdriver.support import expected_conditions
from src.locators.locators import Locators
from helpers import random_int
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import pytest


class TestStellarBurgers:

    def test_after_user_fill_name_its_not_empty(self, random_int, chrome_browser, config):

        chrome_browser.get(config["base_url"])
        chrome_browser.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON).click()
        chrome_browser.find_element(*Locators.REGISTER_LINK).click()
        chrome_browser.find_element(*Locators.NAME_FIELD).send_keys('Damir')
        input_len = len(chrome_browser.find_element(*Locators.NAME_FIELD).get_attribute('value'))
        name = chrome_browser.find_element(*Locators.NAME_FIELD).get_attribute('value')
        assert input_len > 1 and name == 'Damir'

    def test_user_can_fill_correct_email_field_success(self, random_int, chrome_browser, config):

        user_email = f'damir_davlikanov_20_qa{random_int}@yandex.ru'
        chrome_browser.get(config["base_url"])
        chrome_browser.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON).click()
        chrome_browser.find_element(*Locators.REGISTER_LINK).click()
        chrome_browser.find_element(*Locators.EMAIL_FIELD).send_keys(user_email)
        assert chrome_browser.find_element(*Locators.EMAIL_FIELD).get_attribute('value') == user_email

    @pytest.mark.parametrize("password", [1, 12, 12345])
    def test_user_cant_create_account_with_password_less_5_success(self, random_int, chrome_browser,
                                                                   password, config):

        user_email = f'damir_davlikanov_20_qa{random_int}@yandex.ru'
        chrome_browser.get(config["base_url"])
        chrome_browser.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON).click()
        chrome_browser.find_element(*Locators.REGISTER_LINK).click()
        chrome_browser.find_element(*Locators.NAME_FIELD).send_keys('damir_davlikanov')
        chrome_browser.find_element(*Locators.EMAIL_FIELD).send_keys(user_email)
        chrome_browser.find_element(*Locators.PASSWORD_FIELD).send_keys(password)
        chrome_browser.find_element(*Locators.REGISTER_BUTTON).click()
        hint = chrome_browser.find_element(*Locators.INCORRECT_PASSWORD_HINT).text
        password_len = len(chrome_browser.find_element(*Locators.PASSWORD_FIELD).get_attribute('value'))
        assert password_len <= 5 and hint == 'Некорректный пароль'

    def test_user_cant_register_with_incorrect_password_show_error(self, random_int, chrome_browser, config):

        user_email = f'damir_davlikanov_20_qa{random_int}@yandex.ru'
        chrome_browser.get(config["base_url"])
        chrome_browser.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON).click()
        chrome_browser.find_element(*Locators.REGISTER_LINK).click()
        chrome_browser.find_element(*Locators.NAME_FIELD).send_keys('damir_davlikanov')
        chrome_browser.find_element(*Locators.EMAIL_FIELD).send_keys(user_email)
        chrome_browser.find_element(*Locators.PASSWORD_FIELD).send_keys('12312')
        chrome_browser.find_element(*Locators.REGISTER_BUTTON).click()
        assert chrome_browser.find_element(*Locators.INCORRECT_PASSWORD_HINT).text == 'Некорректный пароль'

    def test_user_can_sign_up_via_enter_in_account_button_success(self, random_int, chrome_browser, config):

        user_email = f'damir_davlikanov_20_qa{random_int}@yandex.ru'
        chrome_browser.get(config["base_url"])
        chrome_browser.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON).click()
        chrome_browser.find_element(*Locators.REGISTER_LINK).click()
        chrome_browser.find_element(*Locators.NAME_FIELD).send_keys('damir_davlikanov')
        chrome_browser.find_element(*Locators.EMAIL_FIELD).send_keys(user_email)
        chrome_browser.find_element(*Locators.PASSWORD_FIELD).send_keys('123123')
        chrome_browser.find_element(*Locators.REGISTER_BUTTON).click()
        WebDriverWait(chrome_browser, 3).until(expected_conditions.
                                               visibility_of_element_located(Locators.ENTRANCE_TITLE))
        assert chrome_browser.find_element(*Locators.ENTER_TITLE).text == 'Вход'

    def test_user_can_sign_in_via_enter_an_account_button_success(self, chrome_browser, config):

        chrome_browser.get(config["base_url"])
        chrome_browser.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON).click()
        chrome_browser.find_element(*Locators.EMAIL_FIELD_SIGH_IN).send_keys('damir_davlikanov_20_qa123@yandex.ru')
        chrome_browser.find_element(*Locators.PASSWORD_FIELD_SIGH_IN).send_keys('123123')
        chrome_browser.find_element(*Locators.ENTER_BUTTON).click()
        chrome_browser.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(chrome_browser, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, '//a[@href="/account/profile"]')))
        name = chrome_browser.find_element(*Locators.PERSONAL_NAME_FIELD).get_attribute('value')
        login = chrome_browser.find_element(*Locators.PERSONAL_LOGIN_FIELD).get_attribute('value')
        assert name == 'damir_davlikanov' and login == 'damir_davlikanov_20_qa123@yandex.ru'

    def test_user_can_sign_in_via_personal_account_button_success(self, chrome_browser, config):

        chrome_browser.get(config["base_url"])
        chrome_browser.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        chrome_browser.find_element(*Locators.EMAIL_FIELD_SIGH_IN).send_keys('damir_davlikanov_20_qa123@yandex.ru')
        chrome_browser.find_element(*Locators.PASSWORD_FIELD_SIGH_IN).send_keys('123123')
        chrome_browser.find_element(*Locators.ENTER_BUTTON).click()
        WebDriverWait(chrome_browser, 3).until(
            expected_conditions.visibility_of_element_located(Locators.PLACE_AN_ORDER_BUTTON))
        chrome_browser.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(chrome_browser, 3).until(
            expected_conditions.visibility_of_element_located(Locators.PROFILE_BUTTON))
        name = chrome_browser.find_element(*Locators.PERSONAL_NAME_FIELD).get_attribute('value')
        login = chrome_browser.find_element(*Locators.PERSONAL_LOGIN_FIELD).get_attribute('value')
        assert name == 'damir_davlikanov' and login == 'damir_davlikanov_20_qa123@yandex.ru'

    def test_user_can_sign_in_via_registration_form_success(self, chrome_browser, config):

        chrome_browser.get(config["base_url"])
        chrome_browser.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON).click()
        chrome_browser.find_element(*Locators.REGISTER_LINK).click()
        chrome_browser.find_element(*Locators.ENTER_LINK).click()
        chrome_browser.find_element(*Locators.EMAIL_FIELD_SIGH_IN).send_keys('damir_davlikanov_20_qa123@yandex.ru')
        chrome_browser.find_element(*Locators.PASSWORD_FIELD_SIGH_IN).send_keys('123123')
        chrome_browser.find_element(*Locators.ENTER_BUTTON).click()
        WebDriverWait(chrome_browser, 3).until(
            expected_conditions.visibility_of_element_located(Locators.PLACE_AN_ORDER_BUTTON))
        chrome_browser.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(chrome_browser, 3).until(
            expected_conditions.visibility_of_element_located(Locators.PROFILE_BUTTON))
        name = chrome_browser.find_element(*Locators.PERSONAL_NAME_FIELD).get_attribute('value')
        login = chrome_browser.find_element(*Locators.PERSONAL_LOGIN_FIELD).get_attribute('value')
        assert name == 'damir_davlikanov' and login == 'damir_davlikanov_20_qa123@yandex.ru'

    def test_user_can_sign_in_via_password_recovery_form_success(self, chrome_browser, config):

        chrome_browser.get(config["base_url"])
        chrome_browser.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON).click()
        chrome_browser.find_element(*Locators.RECOVERY_PASSWORD_LINK).click()
        chrome_browser.find_element(*Locators.ENTER_LINK).click()
        chrome_browser.find_element(*Locators.EMAIL_FIELD_SIGH_IN).send_keys('damir_davlikanov_20_qa123@yandex.ru')
        chrome_browser.find_element(*Locators.PASSWORD_FIELD_SIGH_IN).send_keys('123123')
        chrome_browser.find_element(*Locators.ENTER_BUTTON).click()
        WebDriverWait(chrome_browser, 3).until(
            expected_conditions.visibility_of_element_located(Locators.PLACE_AN_ORDER_BUTTON))
        chrome_browser.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(chrome_browser, 3).until(
            expected_conditions.visibility_of_element_located(Locators.PROFILE_BUTTON))
        name = chrome_browser.find_element(*Locators.PERSONAL_NAME_FIELD).get_attribute('value')
        login = chrome_browser.find_element(*Locators.PERSONAL_LOGIN_FIELD).get_attribute('value')
        assert name == 'damir_davlikanov' and login == 'damir_davlikanov_20_qa123@yandex.ru'

    def test_registered_user_can_go_to_personal_account_success(self, chrome_browser, config):

        chrome_browser.get(config["base_url"])
        chrome_browser.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON).click()
        chrome_browser.find_element(*Locators.EMAIL_FIELD_SIGH_IN).send_keys('damir_davlikanov_20_qa123@yandex.ru')
        chrome_browser.find_element(*Locators.PASSWORD_FIELD_SIGH_IN).send_keys('123123')
        chrome_browser.find_element(*Locators.ENTER_BUTTON).click()
        WebDriverWait(chrome_browser, 3).until(
            expected_conditions.visibility_of_element_located(Locators.PLACE_AN_ORDER_BUTTON))
        chrome_browser.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(chrome_browser, 3).until(
            expected_conditions.visibility_of_element_located(Locators.PROFILE_SIDEBAR))
        hint = chrome_browser.find_element(*Locators.PERSONAL_ACCOUNT_HINT).text
        assert hint == 'В этом разделе вы можете изменить свои персональные данные'

    def test_registered_user_can_go_from_personal_account_to_constructor_success(self, chrome_browser, config):

        chrome_browser.get(config["base_url"])
        chrome_browser.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON).click()
        chrome_browser.find_element(*Locators.EMAIL_FIELD_SIGH_IN).send_keys('damir_davlikanov_20_qa123@yandex.ru')
        chrome_browser.find_element(*Locators.PASSWORD_FIELD_SIGH_IN).send_keys('123123')
        chrome_browser.find_element(*Locators.ENTER_BUTTON).click()
        WebDriverWait(chrome_browser, 3).until(
            expected_conditions.visibility_of_element_located(Locators.PLACE_AN_ORDER_BUTTON))
        chrome_browser.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(chrome_browser, 3).until(
            expected_conditions.visibility_of_element_located(Locators.PROFILE_SIDEBAR))
        chrome_browser.find_element(*Locators.CONSTRUCTION_BUTTON).click()
        burger_title = chrome_browser.find_element(*Locators.ASSEMBLE_A_BURGER_TITLE).text
        assert burger_title == 'Соберите бургер'

    def test_registered_user_can_go_from_personal_account_to_constructor_via_burger_button_success(self, chrome_browser,
                                                                                                   config):

        chrome_browser.get(config["base_url"])
        chrome_browser.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON).click()
        chrome_browser.find_element(*Locators.EMAIL_FIELD_SIGH_IN).send_keys('damir_davlikanov_20_qa123@yandex.ru')
        chrome_browser.find_element(*Locators.PASSWORD_FIELD_SIGH_IN).send_keys('123123')
        chrome_browser.find_element(*Locators.ENTER_BUTTON).click()
        chrome_browser.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(chrome_browser, 3).until(
            expected_conditions.visibility_of_element_located(Locators.PROFILE_SIDEBAR))
        chrome_browser.find_element(*Locators.STELLAR_BURGERS_BUTTON).click()
        burger_title = chrome_browser.find_element(*Locators.ASSEMBLE_A_BURGER_TITLE).text
        assert burger_title == 'Соберите бургер'

    def test_registered_user_can_logout_success(self, chrome_browser, config):

        chrome_browser.get(config["base_url"])
        chrome_browser.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON).click()
        chrome_browser.find_element(*Locators.EMAIL_FIELD_SIGH_IN).send_keys('damir_davlikanov_20_qa123@yandex.ru')
        chrome_browser.find_element(*Locators.PASSWORD_FIELD_SIGH_IN).send_keys('123123')
        chrome_browser.find_element(*Locators.ENTER_BUTTON).click()
        chrome_browser.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(chrome_browser, 3).until(
            expected_conditions.visibility_of_element_located(Locators.EXIT_BUTTON))
        chrome_browser.find_element(*Locators.EXIT_BUTTON).click()
        WebDriverWait(chrome_browser, 3).until(
            expected_conditions.visibility_of_element_located(Locators.ENTER_BUTTON))
        enter_button_text = chrome_browser.find_element(*Locators.ENTER_BUTTON).text
        new_user_hint = chrome_browser.find_element(*Locators.NEW_USER_HINT).text
        assert enter_button_text == 'Войти' and new_user_hint == 'Вы — новый пользователь? Зарегистрироваться'

    def test_registered_user_can_open_fillings_section_success(self, chrome_browser, config):

        chrome_browser.get(config["base_url"])
        chrome_browser.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON).click()
        chrome_browser.find_element(*Locators.EMAIL_FIELD_SIGH_IN).send_keys('damir_davlikanov_20_qa123@yandex.ru')
        chrome_browser.find_element(*Locators.PASSWORD_FIELD_SIGH_IN).send_keys('123123')
        chrome_browser.find_element(*Locators.ENTER_BUTTON).click()
        WebDriverWait(chrome_browser, 3).until(
            expected_conditions.visibility_of_element_located(Locators.FILLINGS_SECTION_BUTTON))
        chrome_browser.find_element(*Locators.FILLINGS_SECTION_BUTTON).click()
        fillings_table = chrome_browser.find_element(*Locators.CURRENT_TABLE).get_attribute('class')
        assert 'current' in fillings_table

    def test_registered_user_can_open_sauces_section_success(self, chrome_browser, config):

        chrome_browser.get(config["base_url"])
        chrome_browser.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON).click()
        chrome_browser.find_element(*Locators.EMAIL_FIELD_SIGH_IN).send_keys('damir_davlikanov_20_qa123@yandex.ru')
        chrome_browser.find_element(*Locators.PASSWORD_FIELD_SIGH_IN).send_keys('123123')
        chrome_browser.find_element(*Locators.ENTER_BUTTON).click()
        WebDriverWait(chrome_browser, 3).until(
            expected_conditions.visibility_of_element_located(Locators.SAUCES_SECTION_BUTTON))
        chrome_browser.find_element(*Locators.SAUCES_SECTION_BUTTON).click()
        sauces_table = chrome_browser.find_element(*Locators.CURRENT_TABLE).get_attribute('class')
        assert 'current' in sauces_table

    def test_registered_user_can_open_buns_section_success(self, chrome_browser, config):

        chrome_browser.get(config["base_url"])
        chrome_browser.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON).click()
        chrome_browser.find_element(*Locators.EMAIL_FIELD_SIGH_IN).send_keys('damir_davlikanov_20_qa123@yandex.ru')
        chrome_browser.find_element(*Locators.PASSWORD_FIELD_SIGH_IN).send_keys('123123')
        chrome_browser.find_element(*Locators.ENTER_BUTTON).click()
        WebDriverWait(chrome_browser, 3).until(
            expected_conditions.visibility_of_element_located(Locators.BUNS_SECTION_BUTTON))
        chrome_browser.find_element(*Locators.FILLINGS_SECTION_BUTTON).click()
        chrome_browser.find_element(*Locators.BUNS_SECTION_BUTTON).click()
        buns_table = chrome_browser.find_element(*Locators.CURRENT_TABLE).get_attribute('class')
        assert 'current' in buns_table
