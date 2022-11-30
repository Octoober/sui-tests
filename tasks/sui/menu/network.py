from typing import NoReturn

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from core.task import TaskBase
from utils.locations.sui import Menu
from constants import PERSONAL_SUI_URL, SuiUrlParams

from helpers import random_sleep
from settings import RANDOM_SLEEP


class Network(TaskBase):
    def __init__(self, driver: WebDriver) -> NoReturn:
        super().__init__(driver)
        self._url = PERSONAL_SUI_URL + SuiUrlParams.Menu.NETWORK

    def select_testnet(self) -> NoReturn:
        testnet_item = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located(Menu.Network.SUI_TESTNET_ITEM))
        random_sleep(*RANDOM_SLEEP)
        testnet_item.click()
