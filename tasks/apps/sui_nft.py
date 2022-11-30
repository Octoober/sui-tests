import random
from typing import NoReturn

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from core.task import TaskBase
from helpers import random_sleep
from utils.locations.apps.sui_nft import Home
from settings import RANDOM_SLEEP, RANDOM_SLEEP_WRITE

WORD_LIST = ['decorate', "cigarette",
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

IMAGE_LIST = [
    'https://loremflickr.com/cache/resized/65535_51922208154_94957bf6a4_z_400_400_nofilter.jpg',
    'https://loremflickr.com/cache/resized/3834_10458256845_b73c9399b0_z_400_400_nofilter.jpg',
    'https://loremflickr.com/cache/resized/8218_8374482445_d10dab2072_z_400_400_nofilter.jpg',
    'https://loremflickr.com/cache/resized/65535_51789143123_9a6766a5f5_z_400_400_nofilter.jpg',
    'https://loremflickr.com/cache/resized/65535_52294428543_2d04971c12_z_400_400_nofilter.jpg',
    'https://loremflickr.com/cache/resized/65535_51946578247_d5fef148a0_z_400_400_nofilter.jpg',
    'https://loremflickr.com/cache/resized/65535_52007833850_d72c395d67_400_400_nofilter.jpg',
    'https://loremflickr.com/cache/resized/65535_52342652910_6729b8a007_400_400_nofilter.jpg',
    'https://loremflickr.com/cache/resized/65535_52388619447_8589c49d5d_c_400_400_nofilter.jpg',
    'https://loremflickr.com/cache/resized/65535_52218364875_68c776ab20_z_400_400_nofilter.jpg',
    'https://loremflickr.com/cache/resized/65535_51696326178_96581e9ab7_z_400_400_nofilter.jpg',
    'https://loremflickr.com/cache/resized/65535_51923601496_2649a4c0ce_z_400_400_nofilter.jpg'
]


class SuiNft(TaskBase):
    def __init__(self, driver: WebDriver, url: str) -> NoReturn:
        super().__init__(driver)
        self._url = url

    def run_tasks(self, iteration: int = 0):
        if iteration == 0:
            self.connecting()

        for i in range(7):
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
        name_text = random.choice(WORD_LIST)
        name_input = WebDriverWait(self._driver, 20).until(
            EC.presence_of_element_located(Home.NAME_INPUT))

        for letter in name_text:
            name_input.send_keys(letter)
            random_sleep(*RANDOM_SLEEP_WRITE)

    def write_description(self):
        description_text = random.choice(WORD_LIST)
        description_input = WebDriverWait(self._driver, 20).until(
            EC.presence_of_element_located(Home.DESCRIPTION_INPUT))

        for letter in description_text:
            description_input.send_keys(letter)
            random_sleep(*RANDOM_SLEEP_WRITE)

    def write_image_url(self):
        image_url = random.choice(IMAGE_LIST)
        image_url_input = WebDriverWait(self._driver, 20).until(
            EC.presence_of_element_located(Home.IMAGE_URL_INPUT))
        image_url_input.send_keys(image_url)

    def minting(self):
        create_button = WebDriverWait(self._driver, 20).until(
            EC.presence_of_element_located(Home.CREATE_BUTTON))
        create_button.click()

        self.approve_task()
