from typing import NoReturn
from selenium.webdriver.remote.webdriver import WebDriver
# from utils.random_sleep import random_sleep
# from settings import RANDOM_SLEEP


class TaskBase:
    def __init__(self, driver: WebDriver) -> NoReturn:
        self._driver: WebDriver = driver
        self._url: str = ''

    @property
    def driver(self) -> WebDriver:
        return self._driver

    @driver.setter
    def driver(self, value: WebDriver) -> NoReturn:
        self._driver = value

    @property
    def url(self) -> str:
        return self._url

    @url.setter
    def url(self, value: str) -> NoReturn:
        self._url = value

    def open(self):
        # random_sleep(*RANDOM_SLEEP)
        self._driver.get(self._url)
        return self
