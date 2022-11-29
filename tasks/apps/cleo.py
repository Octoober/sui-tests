import logging
import random
from typing import NoReturn

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

from core.task import TaskBase
# from tasks.sui.popup import Popup
from helpers import random_sleep
from utils.locations.apps import cleo
from settings import RANDOM_SLEEP
from utils import Logcat

logger = Logcat(__name__).logger


class Cleo(TaskBase):
    def __init__(self, driver: WebDriver, url: str) -> NoReturn:
        super().__init__(driver)
        logger.info(f'init {self.__class__.__name__}')
        self._url = url

    def run_tasks(self):
        self.connecting()
        self.minting()

    def connecting(self):
        try:
            connect_button = WebDriverWait(self._driver, 50).until(
                EC.presence_of_element_located(cleo.CONNECT_BUTTON))
            random_sleep(*RANDOM_SLEEP)
            connect_button.click()
        except TimeoutException:
            logger.critical('connect button not found')
            return

        try:
            sui_wallet_button = WebDriverWait(self._driver, 20).until(
                EC.presence_of_element_located(cleo.SUI_WALLET_BUTTON))
            random_sleep(*RANDOM_SLEEP)
            sui_wallet_button.click()
        except TimeoutException:
            logger.critical('sui wallet button not found')
            return

        logger.debug('connecting...')
        self.connect_task()

    def minting(self):
        try:
            mint_button = WebDriverWait(self._driver, 30).until(
                EC.presence_of_element_located(cleo.MINT_BUTTON))
            random_sleep(*RANDOM_SLEEP)
            mint_button.click()
        except TimeoutException:
            logger.critical('mint button not found')
            return

        logger.debug('approving...')
        self.approve_task()
