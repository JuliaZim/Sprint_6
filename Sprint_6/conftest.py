from selenium import webdriver
import pytest
from page.question_about_important_page import MainPage
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

