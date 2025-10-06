import allure
from locators import order_page_locators
from page.base_page import BasePage
import random
from selenium.webdriver.common.by import By


class OrderPageStep2(BasePage):
    @allure.step('Ожидаем загрузки поля даты доставки') 
    def wait_delivery_time_input(self):
        self.wait_for_element_to_be_visible(order_page_locators.DELIVERY_TIME_INPUT)

    @allure.step('Заполняем поле Когда привезти самокат') 
    def set_delivery_time_input(self):
        self.click_element(order_page_locators.DELIVERY_TIME_INPUT)
        date_element = self.find_element(
            order_page_locators.DELIVERY_DATE_BUTTON
        )
        date_element.click()

    @allure.step('Заполняем поле Время аренды') 
    def set_rent_time(self):
        rent_time = random.randint(1, 7)
        self.click_element(order_page_locators.RENT_TIME_INPUT)
        time_locator = (
            By.XPATH,
            order_page_locators.RENT_TIME_VALUE[1].format(rent_time),
        )
        self.wait_for_element_to_be_clickable(order_page_locators.RENT_TIME_VALUE)
        self.click_element(time_locator)

    @allure.step('Выбираем чек-бокс с черным цветом') 
    def set_black_color(self):
        self.click_element(order_page_locators.COLOR_BLACK_CHECKBOX)

    @allure.step('Выбираем чек-бокс с серым цветом') 
    def set_grey_color(self):
        self.click_element(order_page_locators.COLOR_GREY_CHECKBOX)

    @allure.step('Заполняем комментарий для курьера') 
    def set_comment(self, comment):
        self.send_keys_element(order_page_locators.COMMENT_INPUT, comment)

    @allure.step('Заполняем форму заказа на шаге 2') 
    def fill_second_step(self, comment):
        self.wait_delivery_time_input()
        self.set_delivery_time_input()
        self.set_rent_time()
        self.set_black_color()
        self.set_grey_color()
        self.set_comment(comment)

    @allure.step('Кликаем кнопку Заказать на втором шаге') 
    def click_next_button_second_step(self):
        self.wait_for_element_to_be_clickable(order_page_locators.ORDER_BUTTON)
        self.click_element(order_page_locators.ORDER_BUTTON)

    @allure.step('Нажимаем кнопку Да на вопрос о подтверждении заказа') 
    def click_yes_button(self):
        self.wait_for_element_to_be_clickable(order_page_locators.YES_BUTTON)
        self.click_element(order_page_locators.YES_BUTTON)