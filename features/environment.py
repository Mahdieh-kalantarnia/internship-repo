from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager
from app.application import Application

def browser_init(context, scenario_name):
    ### Chrome
    # options = webdriver.ChromeOptions()
    # options.add_argument("--headless=new")
    # options.add_argument("--window-size=1920,1080")
    # options.add_argument("--no-sandbox")
    # options.add_argument("--disable-gpu")
    # options.add_argument("--disable-dev-shm-usage")
    #
    # context.driver = webdriver.Chrome(
    #     service=ChromeService(ChromeDriverManager().install()),
    #     options=options
    # )

    ### Firefox ###
    options = FirefoxOptions()
    # options.add_argument("--headless")
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")

    context.driver = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install()),
        options=options
    )


    context.app = Application(context.driver)

def before_scenario(context, scenario):
    browser_init(context, scenario.name)

def after_scenario(context, scenario):
    if hasattr(context, "driver"):
        context.driver.quit()