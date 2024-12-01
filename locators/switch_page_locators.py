from selenium.webdriver.common.by import By

class SwitchPageLocators:
    SCOOTER = (By.XPATH, "//img[@alt='Scooter']")
    YANDEX = (By.XPATH, "//img[@alt='Yandex']")
    EXPECTED_SCOOTER = (By.XPATH, "//div[text()='Учебный тренажер']")
    EXPECTED_YANDEX = (By.XPATH, "//div[text()='Новости']")