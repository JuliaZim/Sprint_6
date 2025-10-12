import allure
from data import answer_text
import pytest
from locators import main_page_locators



class TestMainPage:

    @allure.title('Проверка ответа на вопрос о стоимости')
    @allure.description('На странице ищем блок с вопросами, нажимаем на кнопку с вопросом о стоимости, проверяем, что ответ совпадает с ожидаемым')
    @allure.feature('Вопросы о важном')
    @pytest.mark.parametrize('question_data',
                             [
        (main_page_locators.HOW_MUCH_BUTTON, main_page_locators.HOW_MUCH_TEXT, answer_text.exp_answer_how_much),
        (main_page_locators.WANT_SOME_SCOOTER_BUTTON, main_page_locators.WANT_SOME_SCOOTER_TEXT, answer_text.exp_answer_want_some_scooter),
        (main_page_locators.ABOUT_RENT_TIME_BUTTON, main_page_locators.ABOUT_RENT_TIME_TEXT, answer_text.exp_answer_about_rent_time),
        (main_page_locators.TAKE_SCOOTER_TODAY_BUTTON, main_page_locators.TAKE_SCOOTER_TODAY_TEXT, answer_text.exp_answer_take_scooter_today),
        (main_page_locators.PROLONG_OR_END_EARLY_BUTTON, main_page_locators.PROLONG_OR_END_EARLY_TEXT, answer_text.exp_answer_prolong_or_end_early),
        (main_page_locators.ABOUT_CHARGER_BUTTON, main_page_locators.ABOUT_CHARGER_TEXT, answer_text.exp_answer_about_charger),
        (main_page_locators.ABOUT_CANCEL_BUTTON, main_page_locators.ABOUT_CANCEL_TEXT, answer_text.exp_answer_about_cancel),
        (main_page_locators.ABOUT_OUT_OF_MKAD_BUTTON, main_page_locators.ABOUT_OUT_OF_MKAD_TEXT, answer_text.exp_answer_about_out_of_mkad),
    ])
    def test_question(self, open_question, question_data):
        question_locator, answer_locator, actual_text = question_data
        open_question.click_quiestion_param(question_locator)
        open_question.wait_text_param(answer_locator)
        act_result = str(open_question.get_answer_param(answer_locator))
        assert (
            act_result == actual_text
        ), f"{act_result} не равен ожидаемому {actual_text}"
