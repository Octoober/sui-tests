from typing import NoReturn

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

from core.task import TaskBase
from utils.locations.sui import Menu
from utils.random_sleep import random_sleep

from constants import PERSONAL_SUI_URL, SuiUrlParams
from settings import RANDOM_SLEEP
from utils import Logcat

logger = Logcat(__name__).logger


class Items(TaskBase):
    def __init__(self, driver: WebDriver) -> NoReturn:
        super().__init__(driver)
        logger.info('')
        self._url = PERSONAL_SUI_URL + SuiUrlParams.Menu.INIT

    def open(self):
        random_sleep(*RANDOM_SLEEP)
        self._driver.get(self._url)
        return self

    def request_sui_tokens(self) -> bool:
        logger.info('request sui tokens')
        random_sleep(*RANDOM_SLEEP)

        request_sui_tokens_button = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located(Menu.REQUEST_SUI_TOKENS_BUTTON))
        random_sleep(*RANDOM_SLEEP)
        request_sui_tokens_button.click()

        status = self.request_token_message()

        return status

    def request_token_message(self):
        WebDriverWait(self._driver, 20).until(EC.presence_of_element_located(Menu.REQUEST_IN_PROGRESS_DIV))
        while True:
            try:
                progress_message = self.driver.find_element(*Menu.REQUEST_IN_PROGRESS_DIV)
                if 'limit' in progress_message.text:
                    logger.error(progress_message.text)
                    return False
            except Exception:
                return True
