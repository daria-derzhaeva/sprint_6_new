from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class MainPage(BasePage):

    @allure.step('Клик на вопрос')
    def click_to_question(self, num):
        locator_q_formatted = self.format_locators(MainPageLocators.QUESTION_LOCATOR, num)
        if num == 8:
            self.scroll_to_element(MainPageLocators.QUESTION_LOCATOR_TO_SCROLL)
        self.click_to_element(locator_q_formatted)

    @allure.step('Получение ответа на вопрос')
    def get_answer_text(self, num):
        locator_a_formatted = self.format_locators(MainPageLocators.ANSWER_LOCATOR, num)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator_a_formatted))
        return self.get_text_from_element(locator_a_formatted)

    @allure.step('Проверяем ответ')
    def check_question_and_answer(self, num):
        self.click_to_question(num)
        return self.get_answer_text(num)

    @allure.step('Получение текста элемента')
    def get_text_from_element(self, locator):
        element = self.driver.find_element(*locator)
        return element.text

    @allure.step("Клик по кнопке заказа")
    def click_to_order_button(self, locator):
        self.click_to_element(locator)

