import random
from typing import NoReturn

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from core.task import TaskBase
from helpers import random_sleep
from utils.locations.apps.sui_nft import Home
from settings import RANDOM_SLEEP, RANDOM_SLEEP_WRITE

_word_list = ['decorate', "cigarette",
               "clinic", "distribute",
               "truth", "hesitate",
               "harsh", "frown",
               "wage", "wire",
               "rush", "stumble",
               "technique", "balanced",
               "ballot", "baltimore",
               "backgrounds", "beats",
               "bibliographic", "celebration",
               "briefing", "cancelled"]


class SuiNft(TaskBase):
    def __init__(self, driver: WebDriver, url: str) -> NoReturn:
        super().__init__(driver)
        self._url = url
        self._name = random.choice(_word_list)
        self._description = random.choice(_word_list)
        self._url_nft = "https://picsum.photos/400"

    def open(self):
        random_sleep(*RANDOM_SLEEP)
        self._driver.get(self._url)
        return self

    def run_tasks(self):
        self.connecting()
        self.write_name()
        self.write_description()
        self.write_image_url()
        self.minting()

    def connecting(self):
        connect_button = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located(Home.CONNECT_BUTTON))

        connect_button.click()

        self.connect_task()

    def write_name(self):
        name_input = WebDriverWait(self._driver, 20).until(
            EC.presence_of_element_located(Home.NAME_INPUT))

        for letter in self._name:
            name_input.send_keys(letter)
            random_sleep(*RANDOM_SLEEP_WRITE)

    def write_description(self):
        description_input = WebDriverWait(self._driver, 20).until(
            EC.presence_of_element_located(Home.DESCRIPTION_INPUT))

        for letter in self._name:
            description_input.send_keys(letter)
            random_sleep(*RANDOM_SLEEP_WRITE)

    def write_image_url(self):
        image_url_input = WebDriverWait(self._driver, 20).until(
            EC.presence_of_element_located(Home.IMAGE_URL_INPUT))
        image_url_input.send_keys(self._url)

    def minting(self):
        create_button = WebDriverWait(self._driver, 20).until(
            EC.presence_of_element_located(Home.CREATE_BUTTON))
        create_button.click()

        self.approve_task()
