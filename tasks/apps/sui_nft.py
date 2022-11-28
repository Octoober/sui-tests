from typing import NoReturn

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from core.task import TaskBase
from tasks.sui.popup import Popup
from utils.random_sleep import random_sleep
from utils.locations.apps.sui_nft import Home
from settings import RANDOM_SLEEP


class SuiNft(TaskBase):
    def __init__(self, driver: WebDriver, url: str) -> NoReturn:
        super().__init__(driver)
        self._url = url
        self._phrase = ''

    def open(self):
        random_sleep(*RANDOM_SLEEP)
        self._driver.get(self._url)
        return self

    def run_tasks(self):
        self.connect_sui()
        self.write_name('')
        self.write_description('')
        self.write_image_url('')
        self.click_create()
        self.approve()

    def connect_sui(self):
        connect_button = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located(Home.CONNECT_BUTTON))

        connect_button.click()

        sui_popup = Popup(self._driver)
        sui_popup.switch_to_popup_window()
        sui_popup.click_connect()
        sui_popup.switch_to_main_window()

    def write_name(self, name: str):
        name_input = WebDriverWait(self._driver, 20).until(
            EC.presence_of_element_located(Home.NAME_INPUT))
        name_input.send_keys('Hello Sui Nft')

    def write_description(self, description: str):
        description_input = WebDriverWait(self._driver, 20).until(
            EC.presence_of_element_located(Home.DESCRIPTION_INPUT))
        description_input.send_keys('description nft')

    def write_image_url(self, url: str):
        image_url_input = WebDriverWait(self._driver, 20).until(
            EC.presence_of_element_located(Home.IMAGE_URL_INPUT))
        image_url_input.send_keys('url')

    def click_create(self):
        create_button = WebDriverWait(self._driver, 20).until(
            EC.presence_of_element_located(Home.CREATE_BUTTON))
        create_button.click()

    def approve(self):
        sui_popup = Popup(self._driver)
        sui_popup.switch_to_popup_window()
        sui_popup.click_approve()
        sui_popup.switch_to_main_window()
