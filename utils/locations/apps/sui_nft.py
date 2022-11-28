from selenium.webdriver.common.by import By


class Home:
    CONNECT_BUTTON = (By.XPATH, "/html/body/div[1]/div/main/div/button")
    NAME_INPUT = (By.XPATH, "/html/body/div[1]/div/main/div/div/label[1]/input")
    DESCRIPTION_INPUT = (By.XPATH, "/html/body/div[1]/div/main/div/div/label[2]/input")
    IMAGE_URL_INPUT = (By.XPATH, "/html/body/div[1]/div/main/div/div/label[3]/input")
    CREATE_BUTTON = (By.XPATH, "/html/body/div[1]/div/main/div/div/button")
