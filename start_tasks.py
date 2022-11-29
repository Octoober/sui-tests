import os
import itertools
import logging

from tasks.sui.menu.account import Account
from tasks.sui.menu.network import Network
from tasks.sui.unlock_wallet import UnlockWallet
from tasks.sui.new_account import NewAccount
from tasks.sui.menu.items import Items
from tasks.sui.wallet_info import WalletInfo

from tasks import Extension

from utils.random_sleep import random_sleep

from apps import APPS
from utils.browser import Browser
from _helpers import save_wallet, create_default_wallets_file
from settings import COUNT
from constants import USER_DATA_PATH


logger = logging.getLogger('main')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())


def main():
    create_default_wallets_file()
    is_cold_start = not os.path.exists(USER_DATA_PATH)

    browser = Browser()
    driver = browser.driver
    driver.get(browser.start_page)

    if is_cold_start:
        # Check and install extension
        logger.debug(f'not found user_data: {USER_DATA_PATH}')
        logger.debug('add extension...')
        extension = Extension(driver).open()
        extension.install()

    # Unlock
    unlock_wallet = UnlockWallet(driver)
    unlock_wallet.unlock()
    logger.debug('wallet is lock' if unlock_wallet.is_locked_wallet else 'wallet unlock')

    if unlock_wallet.is_locked_wallet:
        Account(driver).open().logout()
        random_sleep(0.3, 1.5)

    count = range(COUNT) if COUNT > 0 else itertools.count(0)

    for _ in count:
        random_sleep(0.3, 1.5)
        # Create new account
        new_account = NewAccount(driver).open()
        new_account.create_password()
        new_account.recovery_phrase()

        wallet_info = WalletInfo(driver)
        recovery_phrase = new_account.recovery_phrase_text
        wallet_hash = wallet_info.wallet_hash

        save_wallet(wallet_hash, recovery_phrase)

        # Switch to testnet
        Network(driver).open().select_testnet()

        # Request tokens
        status = Items(driver).open().request_sui_tokens()

        if status:
            random_sleep(1, 3)
            for app in APPS:
                app['context'](driver, app['url']).open().run_tasks()

        # Logout
        Account(driver).open().logout()


if __name__ == '__main__':
    main()
