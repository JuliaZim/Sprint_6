import allure
from locators import order_page_locators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from page.base_page import BasePage
import random
from selenium.webdriver.common.by import By


class OrderPageStep1(BasePage):
    @allure.step('Ожидаем отображения поля ввода имени') 
    def wait_name_input(self):
        self.wait_for_element_to_be_visible(order_page_locators.NAME_INPUT)
  
    @allure.step('Заполняем поле Имя') 
    def set_name(self, name):
        self.send_keys_element(order_page_locators.NAME_INPUT, name)

    @allure.step('Заполняем поле Фамилия') 
    def set_lastname(self):
        self.send_keys_element(order_page_locators.LASTNAME_INPUT, "Фамилия")

    @allure.step('Заполняем поле Адрес') 
    def set_address(self, address):
        self.send_keys_element(order_page_locators.ADDRESS_INPUT, address)

    @allure.step('Заполняем поле Станция метро') 
    def set_subway_station(self):
        number_station = random.randint(1,10)
        self.click_element(order_page_locators.SUBWAY_STATION_INPUT)
        station_locator = (By.XPATH, order_page_locators.SUBWAY_STATION_ELEMENT[1].format(number_station)) # Форматируем XPATH
        self.click_element(station_locator)

    @allure.step('Заполняем поле телефон') 
    def set_telephone(self):
        telephone = f'89{random.randint(1000000000,1000000000)}'
        self.send_keys_element(order_page_locators.TELEPHONE_INPUT, telephone)
    
    @allure.step('Нажимаем кнопку Далее на первом шаге') 
    def click_next_button_first_step(self):
        self.click_element(order_page_locators.NEXT_BUTTON)

    @allure.step('Заполняем форму заказа на шаге 1') 
    def fill_first_step(self, name, address):
        self.wait_name_input
        self.set_name(name)
        self.set_lastname()
        self.set_address(address)
        self.set_subway_station()
        self.set_telephone()
        self.click_next_button_first_step()