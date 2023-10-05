from behave import *
from selenium.webdriver.common.by import By
from locators.moneyhelper_dtt import moneyhelper_dtt_locators
import time

@when('we dismiss the emergency banner')
def step_impl(context):
    driver = context.driver
    driver.find_element(By.CSS_SELECTOR, moneyhelper_dtt_locators.emergency_banner_dismiss).click()

@then('the emergency banner should not be visible')
def step_impl(context):
    driver = context.driver
    try:
        emergency_banner = driver.find_element(By.CSS_SELECTOR, moneyhelper_dtt_locators.emergency_banner)
        if not emergency_banner.size['height'] == 0:
            raise AssertionError
    except AssertionError:
        raise AssertionError('> Emergency banner visible after dismissed and refreshed')
    except:
        pass

@when('we enter the search term {term} into the header search')
def step_impl(context, term):
    driver = context.driver
    driver.find_element(By.CSS_SELECTOR, moneyhelper_dtt_locators.header_search_input_desktop).send_keys(term)
    driver.find_element(By.CSS_SELECTOR, moneyhelper_dtt_locators.header_search_button).click()

@then('we should reach the search results page with the title {expected_search_title}')
def step_impl(context, expected_search_title):
    driver = context.driver
    page_title = driver.find_element(By.CSS_SELECTOR, moneyhelper_dtt_locators.h1_page_title)
    page_title_text = page_title.text
    assert page_title_text == expected_search_title

@when('we expand the email panel')
def step_impl(context):
    driver = context.driver
    driver.find_element(By.CSS_SELECTOR, moneyhelper_dtt_locators.sharing_email_button).click()
    time.sleep(1)

@then('we should be able to click the copy link button from the email panel')
def step_impl(context):
    driver = context.driver
    driver.find_element(By.CSS_SELECTOR, moneyhelper_dtt_locators.sharing_email_panel_copy_button).click()

@when('we expand the more options panel')
def step_impl(context):
    driver = context.driver
    driver.find_element(By.CSS_SELECTOR, moneyhelper_dtt_locators.sharing_more_options_button).click()
    time.sleep(1)

@then('we should be able to click the copy link button from the more options panel')
def step_impl(context):
    driver = context.driver
    driver.find_element(By.CSS_SELECTOR, moneyhelper_dtt_locators.sharing_more_options_panel_copy_button).click()