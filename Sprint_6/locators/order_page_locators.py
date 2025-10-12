from selenium.webdriver.common.by import By

# Поля шаг1
NAME_INPUT = [By.XPATH, './/input[@placeholder="* Имя"]']
LASTNAME_INPUT = [By.XPATH, './/input[@placeholder="* Фамилия"]']
ADDRESS_INPUT = [By.XPATH, './/input[@placeholder="* Адрес: куда привезти заказ"]']
SUBWAY_STATION_INPUT = [By.XPATH, './/input[@placeholder="* Станция метро"]']
SUBWAY_STATION_ELEMENT = [By.XPATH,  ".//ul[@class = 'select-search__options']/li[@data-value = '{}']/button"]
TELEPHONE_INPUT = [By.XPATH, './/input[@placeholder="* Телефон: на него позвонит курьер"]']

NEXT_BUTTON = [By.CLASS_NAME, "Button_Middle__1CSJM"]

# Поля шаг 2
DELIVERY_TIME_INPUT = [By.XPATH, './/input[@placeholder="* Когда привезти самокат"]']
DELIVERY_DATE_BUTTON = (By.XPATH, "//div[@aria-label='Choose четверг, 30-е октября 2025 г.']")
RENT_TIME_INPUT = [By.CLASS_NAME, "Dropdown-placeholder"]
RENT_TIME_VALUE = [By.XPATH, ".//div[@class = 'Dropdown-option']['{}']"]
COLOR_BLACK_CHECKBOX = [By.ID, 'black']
COLOR_GREY_CHECKBOX = [By.ID, 'grey']
COMMENT_INPUT = [By.XPATH, './/input[@placeholder="Комментарий для курьера"]']

ORDER_BUTTON = [By.CSS_SELECTOR, "button.Button_Middle__1CSJM:nth-child(2)"]
YES_BUTTON = [By.CSS_SELECTOR, 'div.Order_Buttons__1xGrp:nth-child(2) > button:nth-child(2)']


