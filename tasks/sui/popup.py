from typing import NoReturn

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from core.task import TaskBase
from utils.locations.sui import ConnectWallet
from constants import PERSONAL_SUI_URL, SuiUrlParams

from utils.random_sleep import random_sleep
from settings import RANDOM_SLEEP


class Popup(TaskBase):
    def __init__(self, driver: WebDriver) -> NoReturn:
        super().__init__(driver)
        self._url = PERSONAL_SUI_URL + SuiUrlParams.Menu.NETWORK
        self._current_window = self._driver.current_window_handle
        # self._popup_window = self._driver.window_handles[-1]

    def open(self):
        pass

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
        connect_wallet_button.click()

    def click_approve(self) -> NoReturn:
        approve_button = WebDriverWait(self._driver, 20).until(
            EC.presence_of_element_located(ConnectWallet.APPROVE_BUTTON))
        approve_button.click()

