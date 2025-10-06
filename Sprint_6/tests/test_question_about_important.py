from page.question_about_important_page import MainPage
from selenium import webdriver
import allure



class TestMainPage:
    driver = None

    @classmethod
    def setup_class(cls):
        # создали драйвер для браузера Chrome
        cls.driver = webdriver.Firefox()
        cls.driver.get("https://qa-scooter.praktikum-services.ru/")

    @classmethod
    def teardown_class(cls):
        # закрой браузер
        cls.driver.quit()


    @allure.title('Проверка ответа на вопрос о стоимости')
    @allure.description('На странице ищем блок с вопросами, нажимаем на кнопку с вопросом о стоимости, проверяем, что ответ совпадает с ожидаемым')
    @allure.feature('Вопросы о важном')
    def test_question_how_much(self, open_question):
        open_question.accept_cookie()
        open_question.click_quiestion_how_much()
        open_question.wait_text_how_much()
        act_result = str(open_question.get_answer_how_much())
        assert (
            act_result == "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
        ), f"{act_result} не равен ожидаемому 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'"


    @allure.title('Проверка ответа на вопрос о вохможности взять несколько самокатов')
    @allure.description('На странице ищем блок с вопросами, нажимаем на кнопку с вопросом о возможности взять несколько самокатов, проверяем, что ответ совпадает с ожидаемым')
    @allure.feature('Вопросы о важном')   
    def test_question_want_some_scooter(self, open_question):
        open_question.click_want_some_scooter()
        open_question.wait_text_want_some_scooter()
        act_result = str(open_question.get_answer_want_some_scooter())
        assert (
            act_result
            == "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."
        ), f"{act_result} не равен ожидаемому "

    @allure.title('Проверка ответа на вопрос о времени аренды')
    @allure.description('На странице ищем блок с вопросами, нажимаем на кнопку с вопросом о времени аренды, проверяем, что ответ совпадает с ожидаемым')
    @allure.feature('Вопросы о важном')
    def test_question_about_rent_time(self, open_question):
        open_question.click_quiestion_rent_time()
        open_question.wait_text_rent_time()
        act_result = str(open_question.get_answer_about_time())
        assert (
            act_result
            == "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."
        ), f"{act_result} не равен ожидаемому "

    @allure.title('Проверка ответа на вопрос о возможности взять самокат сегодня')
    @allure.description('На странице ищем блок с вопросами, нажимаем на кнопку с вопросом о возможности взять самокат сегодня, проверяем, что ответ совпадает с ожидаемым')
    @allure.feature('Вопросы о важном')
    def test_question_take_scooter_today(self, open_question):
        open_question.click_quiestion_take_scooter_today()
        open_question.wait_text_take_scooter_today()
        act_result = str(open_question.get_answer_take_scooter_today())
        assert (
            act_result
            == "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
        ), f"{act_result} не равен ожидаемому "

    @allure.title('Проверка ответа на вопрос о продлении или завершении раньше')
    @allure.description('На странице ищем блок с вопросами, нажимаем на кнопку с вопросом о продлении или завершении раньше, проверяем, что ответ совпадает с ожидаемым')
    @allure.feature('Вопросы о важном')
    def test_question_prolong_or_end_early(self, open_question):
        open_question.click_quiestion_prolong_or_end_early()
        open_question.wait_text_prolong_or_end_early()
        act_result = str(open_question.get_answer_prolong_or_end_early())
        assert (
            act_result
            == "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."
        ), f"{act_result} не равен ожидаемому "

    @allure.title('Проверка ответа на вопрос о зарядке')
    @allure.description('На странице ищем блок с вопросами, нажимаем на кнопку с вопросом о зарядке, проверяем, что ответ совпадает с ожидаемым')
    @allure.feature('Вопросы о важном')
    def test_question_about_charger(self, open_question):
        open_question.click_quiestion_about_charger()
        open_question.wait_text_about_charger()
        act_result = str(open_question.get_answer_about_charger())
        assert (
            act_result
            == "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."
        ), f"{act_result} не равен ожидаемому "

    @allure.title('Проверка ответа на вопрос об отмене')
    @allure.description('На странице ищем блок с вопросами, нажимаем на кнопку с вопросом об отмене, проверяем, что ответ совпадает с ожидаемым')
    @allure.feature('Вопросы о важном')
    def test_question_about_cancel(self, open_question):
        open_question.click_quiestion_about_cancel()
        open_question.wait_text_about_cancel()
        act_result = str(open_question.get_answer_about_cancel())
        assert (
            act_result
            == "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."
        ), f"{act_result} не равен ожидаемому "

    @allure.title('Проверка ответа на вопрос о аренде за МКАДом')
    @allure.description('На странице ищем блок с вопросами, нажимаем на кнопку с вопросом о аренде за МКАДом, проверяем, что ответ совпадает с ожидаемым')
    @allure.feature('Вопросы о важном')
    def test_question_about_out_of_mkad(self, open_question):
        open_question.click_quiestion_about_out_of_mkad()
        open_question.wait_text_about_out_of_mkad()
        act_result = str(open_question.get_answer_about_out_of_mkad())
        assert (
            act_result
            == "Да, обязательно. Всем самокатов! И Москве, и Московской области."
        ), f"{act_result} не равен ожидаемому "

    