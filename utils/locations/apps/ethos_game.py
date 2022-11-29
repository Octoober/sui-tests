from selenium.webdriver.common.by import By

BODY_ELEMENT = (By.XPATH, '//body')

GET_STARTED_BUTTON = (By.CLASS_NAME, 'start-button')
CONNECT_SUI_BUTTON = (By.CSS_SELECTOR, '#ethos-close-on-click > div > div:nth-child(2) > div:nth-child(4) > div > button:nth-child(2)')
# CLAIM_BUTTON = (By.XPATH, '//button[contains(@id, "claim-button") and text() = "Claim!"]')
CLAIM_BUTTON = (By.XPATH, '//button[@id="claim-button"]')


BADGE_DIV = (By.XPATH, '//div[@id="badge"][contains(@style, "")]')
GAME_CONTAINER_DIV = (By.CLASS_NAME, 'game-container')
START_LOADER_DIV = (By.XPATH, '//span[@id="start-loader"][contains(@style, "display: none")]')
GAME_OVER_DIV = (By.CLASS_NAME, 'game-over')
