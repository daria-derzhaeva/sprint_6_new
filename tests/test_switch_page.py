import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.switch_page import SwitchPage
from locators.switch_page_locators import SwitchPageLocators


class TestSwitchOrderPage:
    @pytest.mark.parametrize(
        'locator, expected_locator',
        [
            (SwitchPageLocators.SCOOTER, SwitchPageLocators.EXPECTED_SCOOTER),
            (SwitchPageLocators.YANDEX, SwitchPageLocators.EXPECTED_YANDEX),
        ]
    )
    def test_switch_page(self, driver, locator, expected_locator):
        switch_page = SwitchPage(driver)

        switch_page.click_to_element(locator)

        if locator == SwitchPageLocators.SCOOTER:
            wait = WebDriverWait(driver, 10)
            element = wait.until(EC.presence_of_element_located(expected_locator))
            page_text = element.text
            assert page_text.lower().startswith("учебный тренажер".lower())

        elif locator == SwitchPageLocators.YANDEX:
            original_window = driver.current_window_handle
            all_windows = driver.window_handles
            assert len(all_windows) == 2

            for window in all_windows:
                if window != original_window:
                    driver.switch_to.window(window)
                    break

            wait = WebDriverWait(driver, 10)
            element = wait.until(EC.presence_of_element_located(expected_locator))
            page_text = element.text
            assert "Новости" in page_text
