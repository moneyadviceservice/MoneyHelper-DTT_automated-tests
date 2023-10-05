from behave import *
from selenium.webdriver.common.by import By
from locators.moneyhelper_dtt import moneyhelper_dtt_locators
import time

@given('we visit the url {url}')
def step_impl(context, url):
    driver = context.driver
    base_url = context.base_url
    driver.get(f'{base_url}{url}')

@when('we accept the cookies')
def step_impl(context):
    driver = context.driver
    time.sleep(1)
    cookie_banner_count = driver.find_elements(By.CSS_SELECTOR, 'div#ccc-notify')
    if len(cookie_banner_count):
        driver.find_element(By.CSS_SELECTOR, moneyhelper_dtt_locators.accept_button).click()
    else:
        print('> Cookie banner already dismissed or not found')

@then('the cookie banner should not be visible')
def step_impl(context):
    driver = context.driver
    try:
        cookie_banner = driver.find_element(By.CSS_SELECTOR, moneyhelper_dtt_locators.cookie_banner)
        assert cookie_banner
    except AssertionError:
        raise AssertionError('> Cookie banner should not be visible')
    except:
        pass

@when('we refresh the page')
def step_impl(context):
    driver = context.driver
    current_url = driver.current_url
    driver.get(current_url)

@then('the page title should be {expected_page_title}')
def step_impl(context, expected_page_title):
    driver = context.driver
    actual_page_title = driver.find_element(By.CSS_SELECTOR, moneyhelper_dtt_locators.h1).text
    print(expected_page_title, actual_page_title)
    assert expected_page_title == actual_page_title

@then('we should see a link with the href {href}')
def step_impl(context, href):
    driver = context.driver
    link_href = f'a[href="{href}"]'
    try:
        target_link = driver.find_element(By.CSS_SELECTOR, link_href)
        assert href in target_link
    except AssertionError:
        raise AssertionError(f'> Link expected on page: {href}')
    except:
        pass
