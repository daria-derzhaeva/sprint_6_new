from locators.switch_page_locators import SwitchPageLocators
from pages.base_page import BasePage
import allure

class SwitchPage(BasePage):
    @allure.step('Переход к главной странице из страницы регистрации')
    def click_scooter(self):
        self.click_to_element(SwitchPageLocators.SCOOTER)

    @allure.step('Переход на страницу Дзена')
    def click_yandex(self):
        self.click_to_element(SwitchPageLocators.YANDEX)
