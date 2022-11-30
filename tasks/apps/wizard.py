from typing import NoReturn

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from core.task import TaskBase
from tasks.sui.popup import Popup
from helpers import random_sleep
from utils.locations.apps.wizard import Home
from settings import RANDOM_SLEEP
from utils import Logcat

logger = Logcat(__name__).logger


class Wizard(TaskBase):
    def __init__(self, driver: WebDriver, url: str) -> NoReturn:
        super().__init__(driver)
        logger.info('')
        self._url = url
        self._phrase = ''

    def run_tasks(self, iteration: int = 0):
        self.connecting()
        self.minting()

    def connecting(self):
        connect_button = WebDriverWait(self._driver, 20).until(
            EC.presence_of_element_located(Home.CONNECT_BUTTON))
        random_sleep(*RANDOM_SLEEP)
        connect_button.click()

        sui_wallet_button = WebDriverWait(self._driver, 20).until(
            EC.presence_of_element_located(Home.Modal.SUI_WALLET_BUTTON))
        random_sleep(*RANDOM_SLEEP)
        sui_wallet_button.click()

        self.connect_task()

    def minting(self):
        mint_wizard_button = WebDriverWait(self._driver, 20).until(
            EC.presence_of_element_located(Home.MINT_WIZARD_BUTTON))
        mint_wizard_button.click()

        self.approve_task()

        random_sleep(*RANDOM_SLEEP)
        self.driver.switch_to.alert.accept()
