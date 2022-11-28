from typing import NoReturn

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from core.task import TaskBase
from utils.locations.sui import LockWallet
from utils.random_sleep import random_sleep
from constants import PASSWORD
from settings import RANDOM_SLEEP


class UnlockWallet(TaskBase):
    def __init__(self, driver: WebDriver) -> NoReturn:
        super().__init__(driver)
        self._locked = True

    @property
    def is_locked_wallet(self) -> bool:
        return self._locked

    def __is_locked_walled(self) -> NoReturn:
        random_sleep(*RANDOM_SLEEP)
        try:
            WebDriverWait(self._driver, 1).until(EC.presence_of_element_located(LockWallet.TITLE_TEXT))
        except TimeoutException:
            self._locked = False
            return False

        return True

    def unlock(self) -> NoReturn:
        if not self.__is_locked_walled():
            return

        password_input = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located(LockWallet.PASSWORD_INPUT))
        unlock_button = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located(LockWallet.UNLOCK_BUTTON))

        password_input.send_keys(PASSWORD)
        unlock_button.click()
