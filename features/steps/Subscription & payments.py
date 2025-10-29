#from selenium.webdriver.common.by import By
from time import sleep
from behave import given, when, then


@given('Open the main page')
def open_page(context):
    #   context.driver.get('https://soft.reelly.io')
    context.app.main_page.open_page()
    sleep(5)


@when('Enter username & password')
def enter_user_pass(context):
    #  context.driver.find_element(By.XPATH, "//input[@id='email-2']").send_keys("atefeh210@yahoo.com")
    #  context.driver.find_element(By.XPATH, "//input[@id='field']").send_keys("Atefeh.210!")
    context.app.signin_page.username_password()


@then('Click on Continue')
def click_continue(context):
    #    context.driver.find_element(By.XPATH, "//a[text()='Continue']").click()
    context.app.signin_page.continue_btn()
    sleep(5)


@then('Click on Settings')
def click_settings(context):
    #    context.driver.find_element(By.XPATH, '//div[text()="Settings"]').click()
    context.app.ambassadors_page.setting_btn()
    sleep(5)


@then('Click on Subscription & payments')
def click_subscription(context):
    #    context.driver.find_element(By.XPATH, '//div[text()=\"Subscription & payments"]').click()
    context.app.setting_page.subscription_payments()
    sleep(5)


@then('Verify title is visible')
def verify_title_visible(context):
 # title = context.driver.title
# if title == "Subscription and Payment":
#     print("Title is correct: Subscription and Payment")
# else:
#     print(f" Title is different: {title}")
   context.app.subscription_page.verify_title()
   sleep(5)

@then('Verify buttons are available')
def verify_back_upgrade(context):
# back_button = context.driver.find_element(By.XPATH, '//div[text()="Back"]')
     # upgrade_button = context.driver.find_element(By.XPATH, '//div[text()="Upgrade plan"]')
     # assert back_button.is_displayed() and upgrade_button.is_displayed(), "TEST FAIL: Buttons not visible"
     # print(" TEST PASS: Both buttons are visible")

   context.app.subscription_page.verify_btn()
sleep(5)