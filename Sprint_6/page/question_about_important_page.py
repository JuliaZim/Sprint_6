import allure
from locators import main_page_locators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from page.base_page import BasePage



class MainPage(BasePage):
    # Согласиться на куки
    @allure.step('Принимаем куки')    
    def accept_cookie(self):
        self.wait_for_element_to_be_clickable(main_page_locators.COOCKIE_ACCEPT_BUTTON)
        self.click_element(main_page_locators.COOCKIE_ACCEPT_BUTTON)


    #Ожидание элементов списка вопросов на странице
    @allure.step('Ждем загрузку вопросов')    
    def wait_questions_about_important(self):
        self.wait_for_element_to_be_visible(main_page_locators.ABOUT_OUT_OF_MKAD_BUTTON)
    #Проскролить вниз до элемента
    @allure.step('Скролим до элемента с вопросами')    
    def scroll_to_question(self):
        element = self.find_element(main_page_locators.HOW_MUCH_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
    # Кликнуть на вопрос Сколько стоит
    @allure.step('Кликаем на вопрос о стоимости')    
    def click_quiestion_how_much(self):
        self.click_element(main_page_locators.HOW_MUCH_BUTTON)
    #Ожидание текста
    @allure.step('Ждем отображение текста о стоимости')    
    def wait_text_how_much(self):
        self.wait_for_element_to_be_visible(main_page_locators.HOW_MUCH_TEXT)
    # Получить текст ответа на вопрос Сколько стоит
    @allure.step('возвращаем ответ на вопрос о стоимости')    
    def get_answer_how_much(self):
        answer = self.get_text_from_element(main_page_locators.HOW_MUCH_TEXT)
        return answer

    
    # Кликнуть на вопрос Хочу взять несколько самокатов  
    @allure.step('Кликаем на вопрос Хочу взять несколько самокатов')
    def click_want_some_scooter(self):
        self.click_element(main_page_locators.WANT_SOME_SCOOTER_BUTTON)
    #Ожидание текста
    @allure.step('Ожидаем отображение текста на вопрос Хочу взять несколько самокатов')
    def wait_text_want_some_scooter(self):
        self.wait_for_element_to_be_visible(main_page_locators.WANT_SOME_SCOOTER_TEXT)
    # Вернуть ответ на вопрос Хочу взять несколько самокатов
    @allure.step('Возвращаем ответ на вопрос Хочу взять несколько самокатов')
    def get_answer_want_some_scooter(self):
        answer = self.get_text_from_element(main_page_locators.WANT_SOME_SCOOTER_TEXT)
        return answer
    
    # Кликнуть на вопрос о расчете времени аренды
    @allure.step('Кликаем на вопрос о расчете времени аренды')
    def click_quiestion_rent_time(self):
        self.click_element(main_page_locators.ABOUT_RENT_TIME_BUTTON)
    #Ожидание текста
    @allure.step('Ожидаем отображение текста на вопрос о расчете времени аренды')
    def wait_text_rent_time(self):
        self.wait_for_element_to_be_visible(main_page_locators.ABOUT_RENT_TIME_TEXT)
    # Получить ответ на вопрос о расчете времени аренды
    @allure.step('Возвращаем ответ на вопрос о расчете времени аренды')
    def get_answer_about_time(self):
        return self.get_text_from_element(main_page_locators.ABOUT_RENT_TIME_TEXT)
    
    # Кликнуть на вопрос взять самокат сегодня
    @allure.step('Кликаем на вопрос взять самокат сегодня')
    def click_quiestion_take_scooter_today(self):
        self.click_element(main_page_locators.TAKE_SCOOTER_TODAY_BUTTON)
    #Ожидание текста
    @allure.step('Ожидаем отображение текста на вопрос взять самокат сегодня')
    def wait_text_take_scooter_today(self):
        self.wait_for_element_to_be_visible(main_page_locators.TAKE_SCOOTER_TODAY_TEXT)
    # Получить ответ на вопрос взять самокат сегодня
    @allure.step('Возвращаем ответ на вопрос взять самокат сегодня')
    def get_answer_take_scooter_today(self):
        return self.get_text_from_element(main_page_locators.TAKE_SCOOTER_TODAY_TEXT)
    
    # Кликнуть на вопрос продлить или завершить раньше
    @allure.step('Кликаем на вопрос продлить или завершить раньше')
    def click_quiestion_prolong_or_end_early(self):
        self.click_element(main_page_locators.PROLONG_OR_END_EARLY_BUTTON)
    #Ожидание текста
    @allure.step('Ожидаем отображение текста на вопрос продлить или завершить раньше')
    def wait_text_prolong_or_end_early(self):
        self.wait_for_element_to_be_visible(main_page_locators.PROLONG_OR_END_EARLY_TEXT)
    # Получить ответ на вопрос продлить или завершить раньше
    @allure.step('Возвращаем ответ на вопрос продлить или завершить раньше')
    def get_answer_prolong_or_end_early(self):
        return self.get_text_from_element(main_page_locators.PROLONG_OR_END_EARLY_TEXT)
    
    # Кликнуть на вопрос о зарядке
    @allure.step('Кликаем на вопрос о зарядке')
    def click_quiestion_about_charger(self):
        self.click_element(main_page_locators.ABOUT_CHARGER_BUTTON)
    #Ожидание текста
    @allure.step('Ожидаем отображение текста на вопрос о зарядке')
    def wait_text_about_charger(self):
        self.wait_for_element_to_be_visibled(main_page_locators.ABOUT_CHARGER_TEXT)
    # Получить ответ на вопрос о зарядке
    @allure.step('Возвращаем ответ на вопрос о зарядке')
    def get_answer_about_charger(self):
        return self.get_text_from_element(main_page_locators.ABOUT_CHARGER_TEXT)
    
    # Кликнуть на вопрос об отмене
    @allure.step('Кликаем на вопрос об отмене')
    def click_quiestion_about_cancel(self):
        self.click_element(main_page_locators.ABOUT_CANCEL_BUTTON)
    #Ожидание текста
    @allure.step('Ожидаем отображение текста на вопрос об отмене')
    def wait_text_about_cancel(self):
        self.wait_for_element_to_be_visible(main_page_locators.ABOUT_CANCEL_TEXT)
    # Получить ответ на вопрос об отмене
    @allure.step('Возвращаем ответ на вопрос об отмене')
    def get_answer_about_cancel(self):
        return self.get_text_from_element(main_page_locators.ABOUT_CANCEL_TEXT)
    
    # Кликнуть на вопрос ою аренде за МКАДом
    @allure.step('Кликаем на вопрос об аренде за МКАД')
    def click_quiestion_about_out_of_mkad(self):
        self.click_element(main_page_locators.ABOUT_OUT_OF_MKAD_BUTTON)
    #Ожидание текста
    @allure.step('Ожидаем отображение текста на вопрос об аренде за МКАД')
    def wait_text_about_out_of_mkad(self):
        self.wait_for_element_to_be_visible(main_page_locators.ABOUT_OUT_OF_MKAD_TEXT)
    # Получить ответ на вопрос об аренде за МКАДом
    @allure.step('Возвращаем ответ на вопрос об аренде за МКАД')
    def get_answer_about_out_of_mkad(self):
        return self.get_text_from_element(main_page_locators.ABOUT_OUT_OF_MKAD_TEXT)