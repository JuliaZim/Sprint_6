import allure
from locators import main_page_locators
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
        self.scroll_to_element(main_page_locators.HOW_MUCH_BUTTON)
    # Кликнуть на вопрос парам
    @allure.step('Кликаем на вопрос')    
    def click_quiestion_param(self, question_locator):
        self.click_element(question_locator)
    #Ожидание текста
    @allure.step('Ждем отображение текста ответа на вопрос')    
    def wait_text_param(self, answer_locator):
        self.wait_for_element_to_be_visible(answer_locator)
    # Получить текст ответа на вопрос Сколько стоит
    @allure.step('возвращаем ответ на вопрос')    
    def get_answer_param(self, answer_locator):
        answer = self.get_text_from_element(answer_locator)
        return answer
   