from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from app.application import Application


def browser_init(context, scenario_name):
    bs_user = 'atefehkalantarni_zuGbcU'
    bs_key = 'z82ByEsvXuHbVTFbSGkB'
    url = f'https://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'

    bstack_options = {
        "deviceName": "Samsung Galaxy S23",
        "osVersion": "13.0",
        "projectName": "Stakeholder Tests",
        "buildName": "Stakeholder BrowserStack Build",
        "sessionName": scenario_name,
        "appiumVersion": "2.0.0"
    }

    options = Options()
    options.set_capability('bstack:options', bstack_options)
    options.set_capability('browserName', 'chrome')

    context.driver = webdriver.Remote(command_executor=url, options=options)
    context.driver.implicitly_wait(4)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario:', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step:', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed:', step)


def after_scenario(context, feature):
    context.driver.quit()