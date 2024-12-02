from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
import allure

class OrderPage(BasePage):
    @allure.step('Заполнение формы')
    def set_order(self, order_data):
        self.add_text_to_element(OrderPageLocators.NAME, order_data["name"])
        self.add_text_to_element(OrderPageLocators.LAST_NAME, order_data["last_name"])
        self.add_text_to_element(OrderPageLocators.ADDRESS, order_data["address"])
        self.click_to_element(OrderPageLocators.STATION_CLICK)

        if "station" in order_data:
            if order_data["station"] == "Бульвар":
                self.click_to_element(OrderPageLocators.STATION_BULVAR)
            elif order_data["station"] == "Воробьёвы горы":
                self.click_to_element(OrderPageLocators.STATION_VOROBYEVY_GORY)

        self.add_text_to_element(OrderPageLocators.PHONE_NUMBER, order_data["phone"])
        self.click_to_element(OrderPageLocators.NEXT_BUTTON)
        self.click_to_element(OrderPageLocators.DATE_CLICK)
        self.click_to_element(OrderPageLocators.DATE)
        self.click_to_element(OrderPageLocators.DAY_CLICK)
        self.click_to_element(OrderPageLocators.DAY)
        if "color" in order_data:
            if order_data["color"] == "серый":
                self.click_to_element(OrderPageLocators.COLOR_GRAY)
            elif order_data["color"] == "чёрный":
                self.click_to_element(OrderPageLocators.COLOR_BLACK)

        self.add_text_to_element(OrderPageLocators.COMMENT, order_data["comment"])
        self.click_to_element(OrderPageLocators.ORDER_BUTTON)
        self.click_to_element(OrderPageLocators.APPROVE_BUTTON)

    @allure.step('Проверка заказа')
    def check_order(self):
        return self.get_text_from_element(OrderPageLocators.TEXT_SUCCESS_ORDER)