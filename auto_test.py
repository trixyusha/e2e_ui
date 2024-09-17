from selenium import webdriver as wd
from selenium.webdriver.common.by import By

options = wd.ChromeOptions()
options.add_argument('--log-level=3')
browser = wd.Chrome(options=options)

URL = 'https://www.saucedemo.com/'

FIRST_NAME = 'Ksenia'
LAST_NAME = 'Shanyushkina'
POSTAL_CODE = '101000'

browser.get(URL)

def auth(username: str, password: str) -> None:
    browser.find_element(By.ID, 'user-name').send_keys(username)
    browser.find_element(By.ID, 'password').send_keys(password)
    browser.find_element(By.ID, 'login-button').click()
    sel_product()


def sel_product() -> None:
    prices = browser.find_elements(By.CLASS_NAME, 'inventory_item_price')
    prices_list = [float(price.text[1:]) for price in prices]
    max_price_idx = prices_list.index(max(prices_list))
    pricebar = prices[max_price_idx].find_element(By.XPATH, '..')
    inventory_item_name = pricebar.find_element(By.XPATH, '..').find_element(By.CLASS_NAME, 'inventory_item_name').text
    pricebar.find_element(By.TAG_NAME, 'button').click()
    purchase(inventory_item_name)
    


def purchase(item_name: str) -> None:
    browser.find_element(By.ID, 'shopping_cart_container').click()
    cart_list = browser.find_element(By.CLASS_NAME, 'cart_list')
    if(item_name == cart_list.find_element(By.CLASS_NAME, 'inventory_item_name').text):
        print('Добавлен нужный товар')
        browser.find_element(By.ID, 'checkout').click()
        browser.find_element(By.ID, 'first-name').send_keys(FIRST_NAME)
        browser.find_element(By.ID, 'last-name').send_keys(LAST_NAME)
        browser.find_element(By.ID, 'postal-code').send_keys(POSTAL_CODE)
        browser.find_element(By.ID, 'continue').click()
        browser.find_element(By.ID, 'finish').click()
    check()
    


def check():
    if ('complete' in browser.find_element(By.CLASS_NAME, 'header_secondary_container').text.lower()):
        print('Покупка завершена успешно!')


auth('standard_user','secret_sauce')