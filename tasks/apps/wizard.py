# https://test-wizardland.vercel.app/

from typing import NoReturn

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from core.task import TaskBase
from tasks.sui.popup import Popup
from utils.random_sleep import random_sleep
from utils.locations.apps.wizard import Home
from settings import RANDOM_SLEEP


class Wizard(TaskBase):
    def __init__(self, driver: WebDriver, url: str) -> NoReturn:
        super().__init__(driver)
        self._url = url
        self._phrase = ''

    def open(self):
        random_sleep(*RANDOM_SLEEP)
        self._driver.get(self._url)
        return self

    def run_tasks(self):
        print('RUN WIZARD')
        print(self._driver.current_window_handle)
        self.connect_sui()
        self.mint_nft()
        print(self._driver.current_window_handle)

    def connect_sui(self):
        connect_button = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located(Home.CONNECT_BUTTON))

        connect_button.click()

        sui_wallet_button = WebDriverWait(self._driver, 20).until(
            EC.presence_of_element_located(Home.Modal.SUI_WALLET_BUTTON))
        sui_wallet_button.click()

        sui_popup = Popup(self._driver)
        sui_popup.switch_to_popup_window()
        sui_popup.click_connect()
        sui_popup.switch_to_main_window()

    def mint_nft(self):
        mint_wizard_button = WebDriverWait(self._driver, 20).until(
            EC.presence_of_element_located(Home.MINT_WIZARD_BUTTON))
        mint_wizard_button.click()

        sui_popup = Popup(self._driver)
        sui_popup.switch_to_popup_window()
        sui_popup.click_approve()
        sui_popup.switch_to_main_window()

        random_sleep(*RANDOM_SLEEP)
        self._driver.switch_to.alert.accept()
