from page.question_about_important_page import MainPage
from page.base_page import BasePage
from page.order_page_step1 import OrderPageStep1
from page.order_page_step2 import OrderPageStep2
from page.order_page_succes_form import OrderPageSuccessForm
from selenium import webdriver
import allure
import pytest


class TestOrderPage:
    @allure.title("Проверка успешного заказа по верхней кнопке Заказать")
    @allure.description(
        "На странице самоката ищем кнопку Заказать в верхней части страницы, кликаем, заполняем шаг1, заполняем шаг2, кликаем Заказать, проверяем, что появилось окно успешно сформированного заказа. Проверяем, что по клику на самокат происходит переход на страницу самоката, по клику на Яндекс происходит переход на Дзен"
    )
    @allure.feature("Заказ")
    @pytest.mark.parametrize("order_data",
    [
        ("Ия", "Москва, ул.Часовая, д5, кв15", "Комментарий для курьера"),
        ("Александр", "Санкт-Петербург, Невский проспект, д10", ""),
    ],)
    def test_order_with_above_order_button(self, setup_driver, order_data):
        self.driver = setup_driver
        main_page = MainPage(self.driver)
        main_page.accept_cookie()
        base_page = BasePage(self.driver)
        base_page.click_order_button_above_with_wait()
        order_page = OrderPageStep1(self.driver)
        name, address, comment = order_data
        order_page.fill_first_step(name, address)
        order_page2 = OrderPageStep2(self.driver)
        order_page2.fill_second_step(comment)
        order_page2.click_next_button_second_step()
        order_page2.click_yes_button()
        success_page = OrderPageSuccessForm(self.driver)
        act_result_header = success_page.get_header_result()
        assert "Заказ оформлен" in act_result_header and success_page.get_status_form()
        success_page.click_see_status()
        base_page.click_samokat_logo()
        act_result_main_page = base_page.get_current_url()
        assert act_result_main_page == "https://qa-scooter.praktikum-services.ru/"
        base_page.click_ya_logo()
        base_page.switch_to_new_window()
        act_result_ya_url = base_page.get_current_url()
        assert act_result_ya_url == "https://dzen.ru/?yredirect=true" or 'dzen' in act_result_ya_url

    @allure.title("Проверка успешного заказа по нижней кнопке Заказать")
    @allure.description(
        "На странице самоката ищем кнопку Заказать в нижней части страницы, кликаем, заполняем шаг1, заполняем шаг2, кликаем Заказать, проверяем, что появилось окно успешно сформированного заказа. Проверяем, что по клику на самокат происходит переход на страницу самоката, по клику на Яндекс происходит переход на Дзен"
    )
    @allure.feature("Заказ")
    def test_order_with_below_order_button(self, setup_driver, name="Юля", address='Екатеринбург', comment = 'Комментарий'):
        self.driver = setup_driver
        main_page = MainPage(self.driver)
        main_page.accept_cookie()
        base_page = BasePage(self.driver)
        base_page.click_order_button_below_with_wait()
        order_page = OrderPageStep1(self.driver)
        order_page.fill_first_step(name, address)
        order_page2 = OrderPageStep2(self.driver)
        order_page2.fill_second_step(comment)
        order_page2.click_next_button_second_step()
        order_page2.click_yes_button()
        success_page = OrderPageSuccessForm(self.driver)
        act_result_header = success_page.get_header_result()
        assert "Заказ оформлен" in act_result_header and success_page.get_status_form()
        success_page.click_see_status()
        base_page.click_samokat_logo()
        act_result_main_page = base_page.get_current_url()
        assert act_result_main_page == "https://qa-scooter.praktikum-services.ru/"
        base_page.click_ya_logo()
        base_page.switch_to_new_window()
        act_result_ya_url = base_page.get_current_url()
        assert act_result_ya_url == "https://dzen.ru/?yredirect=true" or 'dzen' in act_result_ya_url