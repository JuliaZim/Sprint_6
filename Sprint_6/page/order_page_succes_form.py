import allure
from page.base_page import BasePage
from selenium.webdriver.common.by import By


class OrderPageSuccessForm(BasePage):
    STATUS_FORM = [By.CSS_SELECTOR, ".Order_Modal__YZ-d3"]
    SUCCESS_STATUS = [By.CSS_SELECTOR, ".Order_ModalHeader__3FDaJ"]
    SEE_STATUS_BUTTON = [By.CSS_SELECTOR, ".Order_NextButton__1_rCA > button:nth-child(1)"]

    @allure.step('Получаем заголовок формы') 
    def get_header_result(self):
        return self.get_text_from_element(self.SUCCESS_STATUS)
    
    @allure.step('Проверяем видимость формы успешной заявки') 
    def get_status_form(self):
        return self.find_element(self.STATUS_FORM).is_displayed()
    
    @allure.step('Нажимаем на кнопку Посмотреть статус') 
    def click_see_status(self):
        self.click_element(self.SEE_STATUS_BUTTON)


