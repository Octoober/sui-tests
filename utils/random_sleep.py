from random import randint, uniform
from typing import Union, NoReturn
from time import sleep
# from settings import SLEEP


def random_sleep(min_value: Union[float, int], max_value: Union[float, int]) -> NoReturn:
    # if not SLEEP:
    #     return

    if type(min_value) == float and type(max_value) == float:
        sleep(uniform(min_value, max_value))
    else:
        sleep(randint(min_value, max_value))
