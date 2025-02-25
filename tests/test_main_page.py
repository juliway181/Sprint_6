import allure
import pytest
from conftest import driver
from constants import Constants
from data import Answer
from pages.main_page import MainPage


class TestMainPage:
    @allure.title("Тестирование ответов на вопросы")
    @pytest.mark.parametrize(
        "q_num, expected_result",
        [
            (0, Answer.ANSWER_1),
            (1, Answer.ANSWER_2),
            (2, Answer.ANSWER_3),
            (3, Answer.ANSWER_4),
            (4, Answer.ANSWER_5),
            (5, Answer.ANSWER_6),
            (6, Answer.ANSWER_7),
            (7, Answer.ANSWER_8)
        ]
    )
    def test_question(self, q_num, driver, expected_result):
        main_page = MainPage(driver)
        main_page.get_url(Constants.URL)
        result = main_page.click_to_question_and_get_answer_text(q_num)
        assert main_page.check_result(result, expected_result)

