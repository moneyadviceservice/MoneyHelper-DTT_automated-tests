from selenium import webdriver
import os
from sys import platform

if platform == "win32" or platform == "darwin":
    username = 'fake-username'
    access_key = 'fake-key'
    base_url = 'https://adviser.moneyhelper.org.uk'
    environment = 'production'
else:
    username = os.getenv("LT_USERNAME")
    access_key = os.getenv("LT_ACCESS_KEY")
    base_url = os.getenv("BASEURL")
    environment = os.getenv("ENVIRONMENT")

def build_feature_string(feature):
    feature_str = str(feature)
    feature_str = feature_str.replace('<Feature ', '').replace('>', '').replace('":', ' - ').replace('"', '')
    feature_str = f'MoneyHelper DTT BDD: {feature_str}'
    return feature_str

def before_feature(context, feature):

    context.base_url = base_url

    feature_description = build_feature_string(feature)

    if platform == "linux" or platform == "linux2":
        desired_cap = {
            "platform": "Windows 10",
            "browserName": "chrome",
            "version": "latest",
            "build": "MoneyHelper DTT Project",
            "name": feature_description
        }

        context.driver = webdriver.Remote(
            command_executor="http://{}:{}@hub.lambdatest.com/wd/hub".format(
                username, access_key),
            desired_capabilities=desired_cap)

    # MAC
    elif platform == "darwin":
        context.browser = "Chrome"
        context.driver = webdriver.Chrome("Webdrivers/chromedriver")
    # Windows
    elif platform == "win32":
        context.browser = "Edge"
        context.driver = webdriver.Edge("Webdrivers\msedgedriver.exe")

def after_feature(context, feature):
    if platform == "linux" or platform == "linux2":
        if context.failed:
            context.driver.execute_script("lambda-status=failed")
        else:
            context.driver.execute_script("lambda-status=passed")
    context.driver.quit()

def setup_desired_cap(desired_cap):
    """
    sets the capability according to LT
    :param desired_cap:
    :return:
    """
    return desired_cap