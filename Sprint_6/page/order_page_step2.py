import allure
from locators import order_page_locators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from page.base_page import BasePage
import random
from selenium.webdriver.common.by import By


class OrderPageStep2(BasePage):
    def wait_delivery_time_input(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(order_page_locators.DELIVERY_TIME_INPUT)
        )

    @allure.step('Заполняем поле Когда привезти самокат') 
    def set_delivery_time_input(self):
        self.driver.find_element(*order_page_locators.DELIVERY_TIME_INPUT).click()
        date_element = self.driver.find_element(
            *order_page_locators.DELIVERY_DATE_BUTTON
        )
        date_element.click()

    @allure.step('Заполняем поле Время аренды') 
    def set_rent_time(self):
        rent_time = random.randint(1, 7)
        self.driver.find_element(*order_page_locators.RENT_TIME_INPUT).click()
        time_locator = (
            By.XPATH,
            order_page_locators.RENT_TIME_VALUE[1].format(rent_time),
        )
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(order_page_locators.RENT_TIME_VALUE)
        )
        self.driver.find_element(*time_locator).click()

    @allure.step('Выбираем чек-бокс с черным цветом') 
    def set_black_color(self):
        self.driver.find_element(*order_page_locators.COLOR_BLACK_CHECKBOX).click()

    @allure.step('Выбираем чек-бокс с серым цветом') 
    def set_grey_color(self):
        self.driver.find_element(*order_page_locators.COLOR_GREY_CHECKBOX).click()

    @allure.step('Заполняем комментарий для курьера') 
    def set_comment(self, comment):
        self.driver.find_element(*order_page_locators.COMMENT_INPUT).send_keys(comment)

    def fill_second_step(self, comment):
        self.wait_delivery_time_input()
        self.set_delivery_time_input()
        self.set_rent_time()
        self.set_black_color()
        self.set_grey_color()
        self.set_comment(comment)

    @allure.step('Кликаем кнопку Заказать на втором шаге') 
    def click_next_button_second_step(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(order_page_locators.ORDER_BUTTON)
        )
        self.driver.find_element(*order_page_locators.ORDER_BUTTON).click()

    @allure.step('Нажимаем кнопку Да на вопрос о подтверждении заказа') 
    def click_yes_button(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(order_page_locators.YES_BUTTON)
        )
        self.driver.find_element(*order_page_locators.YES_BUTTON).click()
