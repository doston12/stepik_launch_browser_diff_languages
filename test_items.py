import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def test_basket_is_present(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(url)
    
    add_to_basket_xpath = "//*[@id='add_to_basket_form']//button"

    try:
        add_to_basket_btn = browser.find_element(By.XPATH, add_to_basket_xpath)
        assert add_to_basket_btn.is_displayed(), "Add to basket button is present on the screen"
    except NoSuchElementException:
        assert False, "Add to basket button is not present on the screen"
