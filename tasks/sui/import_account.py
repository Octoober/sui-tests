from typing import NoReturn

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from core import TaskBase
from utils.locations.sui import ImportAccount as ImportAccountElements
from helpers import random_sleep
from constants import PASSWORD, PERSONAL_SUI_URL, SuiUrlParams
from settings import RANDOM_SLEEP, PASSWORD


class ImportAccount(TaskBase):
    def __init__(self, driver: WebDriver) -> NoReturn:
        super().__init__(driver)
        self._url = PERSONAL_SUI_URL + SuiUrlParams.IMPORT_ACCOUNT
        self._phrase = ''

    def send_recovery_phrase(self, phrase: str) -> NoReturn:
        recovery_phrase_input = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located(ImportAccountElements.RECOVERY_PHRASE_INPUT))
        continue_button = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located(ImportAccountElements.CONTINUE_BUTTON))

        # TODO: checking phrase
        recovery_phrase_input.send_keys(phrase)
        random_sleep(*RANDOM_SLEEP)
        continue_button.click()

    def create_password(self) -> NoReturn:
        create_password_input = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located(ImportAccountElements.CREATE_PASSWORD_INPUT))
        confirm_password_input = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located(ImportAccountElements.CONFIRM_PASSWORD_INPUT))
        import_button = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located(ImportAccountElements.IMPORT_BUTTON))

        create_password_input.send_keys(PASSWORD)
        random_sleep(*RANDOM_SLEEP)
        confirm_password_input.send_keys(PASSWORD)
        random_sleep(*RANDOM_SLEEP)

        import_button.click()
