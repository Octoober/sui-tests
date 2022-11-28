from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from utils.locations import chrome_store
from utils.random_sleep import random_sleep

from core import TaskBase
from constants import SUI_EXTENSION_URL
from settings import RANDOM_SLEEP


class Extension(TaskBase):
    def __init__(self, driver: WebDriver):
        super(Extension, self).__init__(driver)

        self._exist = False
        self.url = SUI_EXTENSION_URL

    def install(self):
        main_tab = self.driver.current_window_handle

        try:
            add_to_chrome_button = WebDriverWait(self._driver, 10).until(
                EC.presence_of_element_located(chrome_store.ADD_TO_CHROME_BUTTON))

            random_sleep(*RANDOM_SLEEP)
            add_to_chrome_button.click()
        except TimeoutException:
            print('ADD_TO_CHROME_BUTTON not found')

        try:
            WebDriverWait(self._driver, 300).until(
                EC.presence_of_element_located(chrome_store.REMOVE_FROM_CHROME_BUTTON)
            )
        except TimeoutException:
            print('Extension no installed')

        try:
            WebDriverWait(self.driver, 10).until(
                EC.number_of_windows_to_be(2)
            )
            random_sleep(1, 3)
            self.driver.switch_to.window(self.driver.window_handles[-1])
            self.driver.close()
            self.driver.switch_to.window(main_tab)
        except TimeoutException:
            pass

        self._exist = True
