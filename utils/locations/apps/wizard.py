from selenium.webdriver.common.by import By


class Home:
    CONNECT_BUTTON = (By.XPATH, '/html/body/div[1]/div/div[2]/button')
    MINT_WIZARD_BUTTON = (By.XPATH, '/html/body/div/div/div[2]/div[2]/div/button')

    BALANCE_DIV = (By.XPATH, '/html/body/div/div/div[2]/div[1]/button/div[2]')

    class Modal:
        SUI_WALLET_BUTTON = (By.CSS_SELECTOR, '#radix-\:r0\: > div.wkit-select__scroll > div > div:nth-child(3)')
