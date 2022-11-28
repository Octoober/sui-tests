from typing import NoReturn
import time

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tasks.task import TaskBase
from utils.locations.sui import Menu
from utils.random_sleep import random_sleep
from constants import PASSWORD, PERSONAL_SUI_URL, SuiUrlParams
from settings import RANDOM_SLEEP


class Account(TaskBase):
    def __init__(self, driver: WebDriver) -> NoReturn:
        super().__init__(driver)
        self._url = PERSONAL_SUI_URL + SuiUrlParams.Menu.ACCOUNT

    def open(self):
        random_sleep(*RANDOM_SLEEP)
        self._driver.get(self._url)
        return self

    def logout(self) -> NoReturn:
        logout_button = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located(Menu.Account.LOGOUT_BUTTON))

        logout_button.click()
