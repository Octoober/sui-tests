import os

PASSWORD: str = "TestPass101"
ROOT_PATH: str = os.path.dirname(__file__)
USER_DATA_PATH: str = os.path.join(ROOT_PATH, 'user_data')
WALLETS_JSON_FILE: str = os.path.join(ROOT_PATH, 'wallets.json')
SUI_EXTENSION_URL: str = "https://chrome.google.com/webstore/detail/sui-wallet/opcgpfmipidbgpenhmajoajpbobppdil"
PERSONAL_SUI_URL: str = "chrome-extension://opcgpfmipidbgpenhmajoajpbobppdil/ui.html"
SUI_EXTENSION_PATH: str = os.path.join(ROOT_PATH, 'assets/sui_extension.crx')
RANDOM_SLEEP: list = [2, 8]
RANDOM_SLEEP_WRITE: list = [1, 2]


class SuiUrlParams:
    CREATE_WALLET: str = "#/initialize/create"
    IMPORT_ACCOUNT: str = "#/initialize/import"

    class Menu:
        INIT: str = "#/tokens?menu=%2F"
        NETWORK: str = "#/tokens?menu=%2Fnetwork"
        ACCOUNT: str = "#/tokens?menu=%2Faccount"

    class SubBar:
        APPS: str = "#/apps"
