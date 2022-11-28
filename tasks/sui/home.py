from typing import NoReturn

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tasks.task import TaskBase
from utils.locations.sui import ImportAccount as ImportAccountElements
from utils.random_sleep import random_sleep
from constants import PASSWORD, PERSONAL_SUI_URL, SuiUrlParams
from settings import RANDOM_SLEEP, PASSWORD


class Home(TaskBase):
    def __init__(self, driver: WebDriver) -> NoReturn:
        super().__init__(driver)
        self._url = PERSONAL_SUI_URL + SuiUrlParams.IMPORT_ACCOUNT
        self._phrase = ''

    def open(self):
        random_sleep(*RANDOM_SLEEP)
        self._driver.get(self._url)
        return self
