from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from core import TaskBase
from constants import PERSONAL_SUI_URL, SuiUrlParams
from utils.locations import sui
from helpers import random_sleep
from settings import RANDOM_SLEEP
from utils import Logcat

logger = Logcat(__name__).logger


class Apps(TaskBase):
    def __init__(self, driver):
        super().__init__(driver)
        logger.info('')
        self.url = PERSONAL_SUI_URL + SuiUrlParams.SubBar.APPS

    def mint_nft(self):
        logger.info('first mint nft')
        random_sleep(*RANDOM_SLEEP)
        mint_an_nft_button = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located(sui.SubBar.Apps.MINT_AN_NFT_BUTTON))
        mint_an_nft_button.click()

        try:
            WebDriverWait(self._driver, 3).until(
                EC.presence_of_element_located(sui.SubBar.Apps.MINT_AN_NFT_SPINNER_DIV))
            WebDriverWait(self._driver, 120).until_not(
                EC.presence_of_element_located(sui.SubBar.Apps.MINT_AN_NFT_SPINNER_DIV))
        except TimeoutException:
            logger.info('spinner mint nft hide')
