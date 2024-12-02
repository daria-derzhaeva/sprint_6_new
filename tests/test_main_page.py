import pytest
import allure
from data import test_data_main_page
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators

@allure.title('Тесты на проверку вопросов')
class TestMainPage:
    @pytest.mark.parametrize("num", test_data_main_page.keys())
    def test_questions_and_answers(self, driver, num):
        main_page = MainPage(driver)

        with allure.step("Принимаем куки"):
            main_page.click_to_kuki(MainPageLocators.KUKI)

        with allure.step(f"Проверяем вопрос №{num} и его ответ"):
            locator_q = main_page.format_locators(MainPageLocators.QUESTION_LOCATOR, num)
            locator_a = main_page.format_locators(MainPageLocators.ANSWER_LOCATOR, num)

            main_page.scroll_to_element(locator_q)
            answer_text = main_page.check_question_and_answer(num)

            assert answer_text == test_data_main_page[num], (
                f"Ответ для вопроса №{num} не совпадает с ожидаемым."
                f"\nПолучено: {answer_text}\nОжидалось: {test_data_main_page[num]}"
            )
