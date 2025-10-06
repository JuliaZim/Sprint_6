import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    #Локаторы Заказать
    ORDER_BUTTON_ABOVE = [By.CSS_SELECTOR, '.Header_Nav__AGCXC > button:nth-child(1)'] 
    ORDER_BUTTON_BELOW = [By.CSS_SELECTOR, '.Button_Middle__1CSJM'] 
    YA_LOGO = [By.CSS_SELECTOR, ".Header_LogoYandex__3TSOI"]
    SAMOKAT_LOGO = [By.CSS_SELECTOR, ".Header_LogoScooter__3lsAR"]
    YA_SERCH = [By.CSS_SELECTOR, '.arrow__input']

    # Ожидание кнопки Заказать вверху страницы
    def wait_order_button_above(self):  
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.ORDER_BUTTON_ABOVE))  
    # Ожидание кнопки Заказать внизу страницы
    def wait_order_button_below(self):  
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.ORDER_BUTTON_BELOW))
    # Кликнуть на кнопку Заказать вверху страницы
    def click_order_button_above(self):
        self.driver.find_element(*self.ORDER_BUTTON_ABOVE).click()
    # Кликнуть на кнопку Заказать внизу страницы
    def click_order_button_below(self):
        self.driver.find_element(*self.ORDER_BUTTON_BELOW).click()
    @allure.step('Кликаем на кнопку Заказать вверху страницы') 
    def click_order_button_above_with_wait(self):
        self.wait_order_button_above()
        self.click_order_button_above()

    @allure.step('Кликаем на кнопку Заказать внизу страницы') 
    def click_order_button_below_with_wait(self):
        self.wait_order_button_below()
        self.click_order_button_below()

    @allure.step('Кликаем на кнопку Самокат') 
    def click_samokat_logo(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.SAMOKAT_LOGO))
        self.driver.find_element(*self.SAMOKAT_LOGO).click()

    @allure.step('Кликаем на кнопку Яндекс') 
    def click_ya_logo(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.YA_LOGO))
        self.driver.find_element(*self.YA_LOGO).click()
        time.sleep(2)

    @allure.step('Получаем урл текущей страницы') 
    def get_current_url(self):
           return self.driver.current_url
    
    @allure.step('Переключаемся на новое окно') 
    def switch_to_new_window(self):
        windows = self.driver.window_handles
        if len(windows) > 1:
            self.driver.switch_to.window(windows[1])  # Индексация с нуля, windows[0] - стартовое окно
        else:
            print("Новое окно не было найдено")
        
            
