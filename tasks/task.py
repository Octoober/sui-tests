from typing import NoReturn
from selenium.webdriver.remote.webdriver import WebDriver


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

    def open(self): pass
