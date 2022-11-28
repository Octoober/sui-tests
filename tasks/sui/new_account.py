from typing import NoReturn

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.locations.sui import Register
from utils.random_sleep import random_sleep
from core.task import TaskBase

from constants import (PASSWORD,
                       PERSONAL_SUI_URL,
                       SuiUrlParams)

from settings import RANDOM_SLEEP, RANDOM_SLEEP_WRITE


class NewAccount(TaskBase):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self._url = PERSONAL_SUI_URL + SuiUrlParams.CREATE_WALLET
        self._recovery_phrase: str = ''

    def open(self):
        random_sleep(*RANDOM_SLEEP)
        self._driver.get(self._url)
        return self

    @property
    def recovery_phrase_text(self):
        return self._recovery_phrase

    def create_password(self) -> NoReturn:
        create_password_input = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located(Register.CREATE_PASSWORD_INPUT))
        confirm_password_input = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located(Register.CONFIRM_PASSWORD_INPUT))
        privacy_checkbox = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located(Register.PRIVACY_CHECKBOX))
        create_wallet_button = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located(Register.CREATE_WALLET_BUTTON))

        for word in PASSWORD:
            random_sleep(*RANDOM_SLEEP_WRITE)
            create_password_input.send_keys(word)

        for word in PASSWORD:
            random_sleep(*RANDOM_SLEEP_WRITE)
            confirm_password_input.send_keys(word)

        privacy_checkbox.click()
        random_sleep(*RANDOM_SLEEP)
        create_wallet_button.click()

    def recovery_phrase(self) -> NoReturn:
        recovery_phrase_div = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located(Register.RECOVERY_PHRASE_DIV))
        open_sui_wallet_button = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located(Register.OPEN_SUI_WALLET_BUTTON))

        recovery_phrase = str(recovery_phrase_div.text).split('\n')[0]
        self._recovery_phrase = recovery_phrase

        random_sleep(*RANDOM_SLEEP)
        open_sui_wallet_button.click()
