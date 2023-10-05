from behave import *
from selenium.webdriver.common.by import By
from locators.moneyhelper_dtt import moneyhelper_dtt_locators
import time

@when('we click the button to start the debt advice journey')
def step_impl(context):
    driver = context.driver
    driver.find_elements(By.CSS_SELECTOR, moneyhelper_dtt_locators.primary_button)[0].click()

@then('we should reach the first step of the tool with the title {title}')
def step_impl(context, title):
    driver = context.driver
    page_title = driver.find_element(By.CSS_SELECTOR, moneyhelper_dtt_locators.h1).text
    assert page_title == title

@when('we select {option_selector}')
def step_impl(context, option_selector):
    driver = context.driver
    driver.find_element(By.CSS_SELECTOR, option_selector).click()

