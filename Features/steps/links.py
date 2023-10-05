from behave import *
from selenium.webdriver.common.by import By
from locators.moneyhelper_dtt import moneyhelper_dtt_locators
import requests

@then('all links on the page should be reachable')
def step_impl(context):
    driver = context.driver
    links = driver.find_elements(By.CSS_SELECTOR, moneyhelper_dtt_locators.links)
    broken_links = {}
    for link in links:
        link_href = link.get_attribute('href')
        if not '#' in link_href and not 'tel:' in link_href and not 'mailto:' in link_href:
            link_status = requests.get(link_href).status_code
            if link_status == 404:
                broken_links[link_href] = link_status
    if len(broken_links):
        error_message = 'The following links 404:\n'
        for link, status in broken_links.items():
            error_message = f'{error_message}\n{link} - {status}'
        raise AssertionError(error_message)
