from pages.base_page import Page
from selenium.webdriver.common.by import By





class Setting(Page):

       SUBSCRIPTION_PAYMENT_BTN=(By.XPATH, '//div[text()=\"Subscription & payments"]')

       def subscription_payments(self):

         self.driver.find_element(*self.SUBSCRIPTION_PAYMENT_BTN).click()