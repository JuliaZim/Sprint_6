import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)
    
    def wait_for_element_to_be_clickable(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator))

    def wait_for_element_to_be_visible(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))

    def find_element(self, locator):
        return self.driver.find_element(*locator)
    def click_element(self, locator):
        return self.find_element(locator).click()
    def send_keys_element(self, locator, value):
        return self.find_element(locator).send_keys(value)
    
    def get_text_from_element(self, locator):
        return self.find_element(locator).text
        
    
    #Локаторы Заказать
    ORDER_BUTTON_ABOVE = [By.CSS_SELECTOR, '.Header_Nav__AGCXC > button:nth-child(1)'] 
    ORDER_BUTTON_BELOW = [By.CSS_SELECTOR, '.Button_Middle__1CSJM'] 
    YA_LOGO = [By.CSS_SELECTOR, ".Header_LogoYandex__3TSOI"]
    SAMOKAT_LOGO = [By.CSS_SELECTOR, ".Header_LogoScooter__3lsAR"]

    # Ожидание кнопки Заказать вверху страницы
    @allure.step('Ожидаем пока кнопка Заказать вверху страницы станет кликабельной') 
    def wait_order_button_above(self):  
        self.wait_for_element_to_be_clickable(self.ORDER_BUTTON_ABOVE)
    # Ожидание кнопки Заказать внизу страницы
    @allure.step('Ожидаем пока кнопка Заказать внизу страницы станет кликабельной') 
    def wait_order_button_below(self):  
        self.wait_for_element_to_be_clickable(self.ORDER_BUTTON_BELOW)
    # Кликнуть на кнопку Заказать вверху страницы
    @allure.step('Клик на кнопку Заказать вверху страницы') 
    def click_order_button_above(self):
        self.click_element(self.ORDER_BUTTON_ABOVE)
    # Кликнуть на кнопку Заказать внизу страницы
    @allure.step('Клик на кнопку Заказать вверху страницы') 
    def click_order_button_below(self):
        self.click_element(self.ORDER_BUTTON_BELOW)
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
        self.wait_for_element_to_be_clickable(self.SAMOKAT_LOGO)
        self.click_element(self.SAMOKAT_LOGO)

    @allure.step('Кликаем на кнопку Яндекс') 
    def click_ya_logo(self):
        self.wait_for_element_to_be_clickable(self.YA_LOGO)
        self.click_element(self.YA_LOGO)


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

    @allure.step('ждем загрузки страницы Дзен') 
    def wait_load_page_ya(self):
        self.wait.until(EC.url_contains('http'))
        
            
