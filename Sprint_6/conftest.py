from selenium import webdriver
import pytest
from selenium.webdriver.support import expected_conditions as EC
from page.question_about_important_page import MainPage
from page.order_page_step1 import OrderPageStep1
from page.order_page_step2 import OrderPageStep2
from page.order_page_succes_form import OrderPageSuccessForm
from page.base_page import BasePage


# Фикстура
@pytest.fixture(scope='function')
def open_question(request):
    driver = request.cls.driver 
    main_page = MainPage(driver)   
    main_page.scroll_to_question()
    main_page.wait_questions_about_important()
    return main_page

