from selenium.webdriver.common.by import By

class MainPageLocators:
    QUESTION_LOCATOR = (By.XPATH, "(//div[contains(@class, 'accordion__button')])[{}]")
    ANSWER_LOCATOR = (By.XPATH,"(//div[contains(@class, 'accordion__panel')])[{}]")
    QUESTION_LOCATOR_TO_SCROLL = (By.XPATH, "(//div[contains(@class, 'accordion__button')])[8]")
    ORDER_BUTTON_UP = (By.XPATH, "(//button[text()='Заказать'])[1]")
    ORDER_BUTTON_DOWN = (By.XPATH, "(//button[text()='Заказать'])[2]")
    KUKI = (By.XPATH, "//button[@class='App_CookieButton__3cvqF']")


