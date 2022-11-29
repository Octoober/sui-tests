import logging
from typing import NoReturn


class Logcat:
    def __init__(self, name: str) -> NoReturn:
        self._logger = logging.getLogger(name)
        self._format = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"

        logging.basicConfig(format=self._format)
        self._logger.setLevel(logging.DEBUG)

    @property
    def logger(self) -> logging:
        return self._logger
