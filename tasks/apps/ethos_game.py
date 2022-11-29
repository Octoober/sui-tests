import logging
import random
from typing import NoReturn

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

from core.task import TaskBase
from tasks.sui.popup import Popup
from utils.random_sleep import random_sleep
from utils.locations.apps import ethos_game
from settings import RANDOM_SLEEP
from utils import Logcat

logger = Logcat(__name__).logger


class EthosGame(TaskBase):
    def __init__(self, driver: WebDriver, url: str) -> NoReturn:
        super().__init__(driver)
        logger.info(f'init {self.__class__.__name__}')
        self._url = url
        self._phrase = ''
        self._images = [
            'https://arweave.net/sv0csl4RG5ikMBuaACrvojm-EzcbTi-3ThScTTsVBdc',
            'https://arweave.net/_t8bsaO1Q7RjoxRIZSXQRwtl916L7m8XwSjeWg1fBa8',
            'https://arweave.net/2fTevWYameF4ZJtu9NxgWqa_fGjQ_f8Da0qTwTOI_Dg',
            'https://arweave.net/1z_SHqdfIQBb6QvIKkhvVn14PmxjltZnRdFSdsoJIDQ',
            'https://arweave.net/b7o0WJcyD0BHVvQvlqbgy1HRUQW7iuHpxLalzyL061E',
            'https://arweave.net/ql44u1TetxqFQLYW2f-VDGQGS_ZwC9o68USpdEuwKbs',
            'https://arweave.net/_SOBVh01rBEEnbXxF5rx9MaQBKFbtM5tZdvq0qzoC7A',
            'https://arweave.net/QW9doLmmWdQ-7t8GZ85HtY8yzutoir8lGEJP9zOPQqA'
        ]

    def open(self):
        random_sleep(*RANDOM_SLEEP)
        self._driver.get(self._url)
        return self

    def run_tasks(self):
        self.get_started()
        self.connect_sui()
        # self.start_game()
        self.claim()
        self.approve()

    def get_started(self):
        logger.info('')

        try:
            WebDriverWait(self.driver, 120).until(
                EC.presence_of_element_located(ethos_game.START_LOADER_DIV))
        except TimeoutException:
            logger.critical('loading time out')
            return

        random_sleep(*RANDOM_SLEEP)
        try:
            get_started_button = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(ethos_game.GET_STARTED_BUTTON))
            get_started_button.click()
        except TimeoutException:
            logger.critical('get_started_button not found')

    def connect_sui(self):
        try:
            connect_button = WebDriverWait(self._driver, 30).until(
                EC.presence_of_element_located(ethos_game.CONNECT_SUI_BUTTON))
            connect_button.click()
        except TimeoutException:
            logger.critical('connect button not found')

        sui_popup = Popup(self._driver)
        sui_popup.switch_to_popup_window()
        sui_popup.click_connect()
        sui_popup.switch_to_main_window()

    def start_game(self):
        """
        Randomly click on buttons in the hope of winning

        WAR: No longer relevant
        :return:
        """
        body_element = WebDriverWait(self._driver, 30).until(
            EC.presence_of_element_located(ethos_game.BODY_ELEMENT))
        try:
            WebDriverWait(self._driver, 60).until(
                EC.presence_of_element_located(ethos_game.GAME_CONTAINER_DIV))
        except TimeoutException:
            logger.critical('game container not found')
            return
        else:
            keys_list = [Keys.LEFT, Keys.UP, Keys.RIGHT, Keys.DOWN]
            is_movement = True
            count_iteration = 0
            while True:
                current_key = random.choice(keys_list)
                body_element.send_keys(current_key)
                try:
                    self.driver.find_element(*ethos_game.BADGE_DIV)
                except Exception:
                    logger.debug('next step')
                    count_iteration += 1
                    random_sleep(0.2, 1.5)
                    continue
                else:
                    logger.debug('game over')
                    break

            logger.info(f'number of steps: {count_iteration}')

    def claim(self):
        random_sleep(*RANDOM_SLEEP)
        try:
            claim_button = WebDriverWait(self._driver, 30).until(
                EC.presence_of_element_located(ethos_game.CLAIM_BUTTON))
            self.driver.execute_script("arguments[0].click();", claim_button)
        except TimeoutException:
            logger.critical('claim button not found')

    def approve(self):
        logger.info('approve nft')
        sui_popup = Popup(self._driver)
        sui_popup.switch_to_popup_window()
        sui_popup.click_approve()
        sui_popup.switch_to_main_window()
