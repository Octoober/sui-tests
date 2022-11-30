from typing import NoReturn

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.random_sleep import random_sleep
from utils.locations.sui import ConnectWallet
from settings import RANDOM_SLEEP
from utils import Logcat

logger = Logcat(__name__).logger


class TaskBase:
    def __init__(self, driver: WebDriver) -> NoReturn:
        self._driver: WebDriver = driver

        self._current_window = self._driver.current_window_handle
        self._url = ''
        self._iteration = 0

    @property
    def iteration(self):
        return self._iteration

    @iteration.setter
    def iteration(self, value: int):
        self._iteration = value

    @property
    def driver(self) -> WebDriver:
        return self._driver

    @driver.setter
    def driver(self, value: WebDriver) -> NoReturn:
        self._driver = value

    @property
    def url(self) -> str:
        return self._url

    @url.setter
    def url(self, value: str) -> NoReturn:
        self._url = value

    def open(self):
        random_sleep(*RANDOM_SLEEP)
        self._driver.get(self._url)
        return self

    def switch_to_popup_window(self):
        random_sleep(*RANDOM_SLEEP)
        self._driver.switch_to.window(self._driver.window_handles[-1])
        random_sleep(*RANDOM_SLEEP)

    def switch_to_main_window(self):
        random_sleep(*RANDOM_SLEEP)
        self._driver.switch_to.window(self._current_window)
        random_sleep(*RANDOM_SLEEP)

    def click_connect(self) -> NoReturn:
        connect_wallet_button = WebDriverWait(self._driver, 20).until(
            EC.presence_of_element_located(ConnectWallet.CONNECT_BUTTON))
        random_sleep(*RANDOM_SLEEP)
        connect_wallet_button.click()

    def click_approve(self) -> NoReturn:
        approve_button = WebDriverWait(self._driver, 20).until(
            EC.presence_of_element_located(ConnectWallet.APPROVE_BUTTON))
        random_sleep(*RANDOM_SLEEP)
        approve_button.click()

    def connect_task(self) -> NoReturn:
        self.switch_to_popup_window()
        self.click_connect()
        self.switch_to_main_window()

    def approve_task(self) -> NoReturn:
        self.switch_to_popup_window()
        self.click_approve()
        self.switch_to_main_window()
