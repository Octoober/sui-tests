import os
import json
from time import sleep
from random import randint, uniform
from typing import Union, NoReturn
from selenium.webdriver.remote.webdriver import WebDriver

from constants import WALLETS_JSON_FILE


def get_wallets() -> dict:
    if not os.path.exists(WALLETS_JSON_FILE):
        return {}
    with open(WALLETS_JSON_FILE, 'r') as file:
        wallets = json.loads(file.read())['wallets']

    return wallets


def create_default_wallets_file():
    default_object = {
        'wallets': []
    }
    if not os.path.exists(WALLETS_JSON_FILE):
        with open(WALLETS_JSON_FILE, 'w') as json_file:
            json.dump(default_object, json_file)


def save_wallet(wallet_hash: str, recovery_phrase: str):
    with open(WALLETS_JSON_FILE, 'r') as json_file:
        data = json.load(json_file)

    data['wallets'].append({
        "hash": wallet_hash,
        "phrase": recovery_phrase
    })

    with open(WALLETS_JSON_FILE, 'w') as json_file:
        json.dump(data, json_file, indent=4)


def close_last_window(driver: WebDriver) -> NoReturn:
    main_window = driver.current_window_handle
    last_window = driver.window_handles[-1]
    driver.switch_to.window(last_window)
    driver.close()
    driver.switch_to.window(main_window)


def random_sleep(min_value: Union[float, int], max_value: Union[float, int]) -> NoReturn:
    # if not SLEEP:
    #     return

    if type(min_value) == float and type(max_value) == float:
        sleep(uniform(min_value, max_value))
    else:
        sleep(randint(min_value, max_value))


def check_login():
    pass
