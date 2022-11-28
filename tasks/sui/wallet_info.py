from typing import NoReturn

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from core.task import TaskBase
from utils.locations.sui import SuiHome
from utils.random_sleep import random_sleep
from constants import PERSONAL_SUI_URL
from settings import RANDOM_SLEEP


class WalletInfo(TaskBase):
    def __init__(self, driver: WebDriver) -> NoReturn:
        super().__init__(driver)
        self._url = PERSONAL_SUI_URL

    def open(self):
        random_sleep(*RANDOM_SLEEP)
        self._driver.get(self._url)
        return self

    @property
    def wallet_hash(self):
        wallet_hash_div = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located(SuiHome.WALLET_HASH_DIV))

        wallet_hash_text = wallet_hash_div.get_attribute('title')

        return wallet_hash_text
