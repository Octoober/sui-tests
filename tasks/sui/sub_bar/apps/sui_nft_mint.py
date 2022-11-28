from typing import NoReturn

from selenium.webdriver.remote.webdriver import WebDriver

from core.task import TaskBase
from constants import PERSONAL_SUI_URL, SuiUrlParams


class SuiNftMint(TaskBase):
    def __init__(self, driver: WebDriver) -> NoReturn:
        super().__init__(driver)
        self._url = PERSONAL_SUI_URL + SuiUrlParams.Menu.NETWORK

    def select_apps(self) -> NoReturn:
        self._driver.get(self._url)

        # testnet_item = WebDriverWait(self._driver, 10).until(
        #     EC.presence_of_element_located(Menu.Network.SUI_TESTNET_ITEM))
        #
        # testnet_item.click()
