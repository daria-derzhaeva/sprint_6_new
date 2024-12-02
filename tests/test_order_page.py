import pytest
from pages.main_page import MainPage
from data import ORDER_DATA_1, ORDER_DATA_2
from locators.main_page_locators import MainPageLocators
from pages.order_page import OrderPage

class TestOrderPage:
    @pytest.mark.parametrize(
        'locator, order_data',
        [
            (MainPageLocators.ORDER_BUTTON_UP, ORDER_DATA_1),
            (MainPageLocators.ORDER_BUTTON_DOWN, ORDER_DATA_2)
        ]
    )
    def test_create_order(self, driver, locator, order_data):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.click_to_kuki(MainPageLocators.KUKI)
        main_page.click_to_order_button(locator)
        order_page.set_order(order_data)
        assert order_page.check_order().startswith("Заказ оформлен")


