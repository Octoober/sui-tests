import itertools

from tasks.sui.menu import Account, Network, Items
from tasks.sui import UnlockWallet, NewAccount, WalletInfo
from tasks.sui.sub_bar import Apps

from apps import APPS
from settings import COUNT, INTERVAL
from utils import Browser, Logcat
from helpers import save_wallet, create_default_wallets_file, close_last_window, random_sleep

logger = Logcat(__name__).logger


def main():
    create_default_wallets_file()

    browser = Browser()
    driver = browser.driver
    driver.get(browser.start_page)

    close_last_window(driver)

    # Unlock
    # unlock_wallet = UnlockWallet(driver)
    # unlock_wallet.unlock()
    #
    # logger.debug('wallet is lock' if unlock_wallet.is_locked_wallet else 'wallet unlock')
    #
    # if unlock_wallet.is_locked_wallet:
    #     Account(driver).open().logout()
    #     random_sleep(0.3, 1.5)

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

        # Switch to testnet
        Network(driver).open().select_testnet()

        # Request tokens
        request_status = Items(driver).open().request_sui_tokens()
        logger.debug(f'requests status: {request_status}')

        save_wallet(wallet_hash,
                    recovery_phrase,
                    'error' if not request_status else 'success')

        if request_status:
            # Mint first nft
            Apps(driver).open().mint_nft()

            random_sleep(5, 10)
            for app in APPS:
                app['worker'](driver, app['url']).open().run_tasks()

        # Logout
        Account(driver).open().logout()
        random_sleep(INTERVAL, INTERVAL)


if __name__ == '__main__':
    main()
