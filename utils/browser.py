from typing import NoReturn, Union

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.remote.webdriver import WebDriver

from constants import USER_DATA_PATH, PERSONAL_SUI_URL, SuiUrlParams, SUI_EXTENSION_URL


class Browser:
    def __init__(self) -> NoReturn:
        self._driver: Union[WebDriver, None] = None
        self._start_page: str = (PERSONAL_SUI_URL + SuiUrlParams.CREATE_WALLET) or SUI_EXTENSION_URL

    @staticmethod
    def __options() -> Options:
        chrome_options = Options()
        # chrome_options.add_argument(f'user-data-dir={USER_DATA_PATH}')

        return chrome_options

    @staticmethod
    def __service() -> ChromeService:
        chrome_driver_manager = ChromeDriverManager(cache_valid_range=360).install()
        chrome_service = ChromeService(chrome_driver_manager)

        return chrome_service

    @property
    def start_page(self) -> str:
        return self._start_page

    @start_page.setter
    def start_page(self, value: str) -> NoReturn:
        self._start_page = value

    @property
    def driver(self) -> WebDriver:
        chrome_options = self.__options()
        chrome_service = self.__service()

        self._driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

        return self._driver
