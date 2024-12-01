import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Найти элемент с ожиданием")
    def find_element_with_wait(self, method, locator, timeout=20):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((method, locator)))
        return self.driver.find_element(method, locator)

    @allure.step("Нажать на элемент")
    def click_to_element(self, locator):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))
        return self.driver.find_element(*locator).click()

    @allure.step("Добавить текст")
    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(*locator).send_keys(text)

    @allure.step("Получить текст от элемента")
    def get_text_from_element(self, locator):
        element = self.driver.find_element(*locator)
        return element.text

    @allure.step("Скролл до элемента")
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Формирование локаторов")
    def format_locators(self, locator_1, num):
        method, locator = locator_1
        locator = locator.format(num)
        return (method, locator)

    @allure.step("Принять куки")
    def click_to_kuki(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).click()


