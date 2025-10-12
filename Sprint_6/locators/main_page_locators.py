from selenium.webdriver.common.by import By

COOCKIE_ACCEPT_BUTTON = [By.XPATH, "//*[@id='rcc-confirm-button']"]
#Вопросы о важном
# Кнопки
HOW_MUCH_BUTTON = [By.ID, "accordion__heading-0"]
WANT_SOME_SCOOTER_BUTTON = [By.ID, "accordion__heading-1"] 
ABOUT_RENT_TIME_BUTTON = [By.ID, "accordion__heading-2"]
TAKE_SCOOTER_TODAY_BUTTON = [By.ID, "accordion__heading-3"]
PROLONG_OR_END_EARLY_BUTTON = [By.ID, "accordion__heading-4"]
ABOUT_CHARGER_BUTTON = [By.ID, "accordion__heading-5"]
ABOUT_CANCEL_BUTTON = [By.ID, "accordion__heading-6"]
ABOUT_OUT_OF_MKAD_BUTTON = [By.ID, "accordion__heading-7"]

#Текст
HOW_MUCH_TEXT = [By.CSS_SELECTOR, "#accordion__panel-0 > p:nth-child(1)"] 
WANT_SOME_SCOOTER_TEXT = [By.CSS_SELECTOR, "#accordion__panel-1 > p:nth-child(1)"]
ABOUT_RENT_TIME_TEXT = [By.CSS_SELECTOR, "#accordion__panel-2 > p:nth-child(1)"]
TAKE_SCOOTER_TODAY_TEXT = [By.CSS_SELECTOR, "#accordion__panel-3 > p:nth-child(1)"]
PROLONG_OR_END_EARLY_TEXT = [By.CSS_SELECTOR, "#accordion__panel-4 > p:nth-child(1)"]
ABOUT_CHARGER_TEXT = [By.CSS_SELECTOR, "#accordion__panel-5 > p:nth-child(1)"]
ABOUT_CANCEL_TEXT = [By.CSS_SELECTOR, "#accordion__panel-6 > p:nth-child(1)"]
ABOUT_OUT_OF_MKAD_TEXT = [By.CSS_SELECTOR, "#accordion__panel-7 > p:nth-child(1)"]



