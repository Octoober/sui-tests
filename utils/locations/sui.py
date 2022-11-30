from selenium.webdriver.common.by import By


class Register:
    # **** BUTTONS ****
    GET_STARTED_BUTTON = (By.CLASS_NAME, "uDUBihzsBafACO5RMGr7")
    CREATE_NEW_WALLET_BUTTON = (By.CLASS_NAME, "MuTCPVF5Yv8Jw2J3JDL1")
    OPEN_SUI_WALLET_BUTTON = (By.XPATH, "/html/body/div/div/div/button")

    # After PRIVACY_CHECKBOX
    CREATE_WALLET_BUTTON = (By.XPATH, "/html/body/div/div/div/form/button")

    # **** INPUTS ****
    CREATE_PASSWORD_INPUT = (By.XPATH, '//*[@id="root"]/div/div/form/div/fieldset/label[1]/input')
    CONFIRM_PASSWORD_INPUT = (By.CSS_SELECTOR, "#root > div > div > form > div > fieldset > label:nth-child(2) > input")

    # **** CHECKBOX ****
    PRIVACY_CHECKBOX = (By.XPATH, '//*[@id="root"]/div/div/form/div/fieldset/label[3]/span[1]')

    # **** DIVS ****
    RECOVERY_PHRASE_DIV = (By.CSS_SELECTOR, "#root > div > div > div.FcQQKvA6jyUfX4nnitAd")


class ImportAccount:
    # **** INPUTS ****
    RECOVERY_PHRASE_INPUT = (By.XPATH, '/html/body/div/div/div/form/label/textarea')
    CREATE_PASSWORD_INPUT = (By.XPATH, '/html/body/div/div/div/form/label[1]/input')
    CONFIRM_PASSWORD_INPUT = (By.XPATH, '/html/body/div/div/div/form/label[2]/input')

    # **** BUTTONS ****
    CONTINUE_BUTTON = (By.XPATH, '/html/body/div/div/div/form/div[2]/button')
    IMPORT_BUTTON = (By.XPATH, '/html/body/div/div/div/form/div[2]/button[2]')


class SuiHome:
    # **** BUTTONS ****
    # **** INPUTS ****
    # **** CHECKBOX ****
    # **** DIVS ****
    # **** LINKS ****
    MAIN_MENU_LINK = (By.XPATH, "/html/body/div/div/div/div[1]/a[2]")
    NETWORK_LIST_LINK = (By.XPATH, "/html/body/div/div/div/div[2]/div/div[2]/div/a[2]")
    WALLET_HASH_DIV = (
    By.CSS_SELECTOR, "#root > div > div > div.wOjQeIStBhElmmumhY7o > main > div > span > span > span")


class LockWallet:
    TITLE_TEXT = (By.XPATH, "//h1[text()='Welcome Back']")
    UNLOCK_BUTTON = (By.XPATH, "/html/body/div/div/div/div[2]/main/div/form/button")
    PASSWORD_INPUT = (By.XPATH, "/html/body/div/div/div/div[2]/main/div/form/label/input")


class Menu:
    REQUEST_SUI_TOKENS_BUTTON = (By.XPATH, "/html/body/div/div/div/div[2]/div/div[2]/div/div[2]/button[1]")
    REQUEST_IN_PROGRESS_DIV = (By.XPATH, "/html/body/div/div/div/div[2]/div/div[2]/div/div[3]")

    # REQUEST_STATE_RECIVED = ()

    class Account:
        LOGOUT_BUTTON = (By.XPATH, "/html/body/div/div/div/div[2]/div/div[2]/div/button")

    class Network:
        SUI_TESTNET_ITEM = (By.XPATH, "/html/body/div/div/div/div[2]/div/div[2]/div/div[2]/ul/li[4]/button")


class ConnectWallet:
    CONNECT_BUTTON = (By.XPATH, "/html/body/div/div/div/div[2]/main/div/div[2]/div/button[2]")
    APPROVE_BUTTON = (By.XPATH, "/html/body/div/div/div/div[2]/main/div/div[2]/div/button[2]")


class SubBar:
    class Apps:
        MINT_AN_NFT_BUTTON = (By.XPATH, "//button[contains(@class, 'qvmPyb8NdzsMrFWoHAEN')]")
        MINT_AN_NFT_SPINNER_DIV = (By.XPATH, "//span[contains(@class, 'eQNi4h96O1NXP1BYspBM')]")
