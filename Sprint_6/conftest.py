from selenium import webdriver
import pytest
from selenium.webdriver.support import expected_conditions as EC
from page.question_about_important_page import MainPage
from page.order_page_step1 import OrderPageStep1
from page.order_page_step2 import OrderPageStep2
from page.order_page_succes_form import OrderPageSuccessForm
from page.base_page import BasePage
from data import urls


# Фикстура
@pytest.fixture(scope='function')
def setup_driver():
    driver = webdriver.Firefox()
    driver.get(urls.main_page_samokat_url)
    yield driver
    driver.quit()   

@pytest.fixture(scope='function')
def open_question(setup_driver):
    driver = setup_driver 
    main_page = MainPage(driver)
    main_page.wait_questions_about_important()
    main_page.accept_cookie() 
    main_page.scroll_to_question()
    main_page.wait_questions_about_important()
    return main_page

