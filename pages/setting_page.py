from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC





class Setting(Page):

       SUBSCRIPTION_PAYMENT_BTN=(By.XPATH, '//div[text()=\"Subscription & payments"]')

       def subscription_payments(self):
           element = WebDriverWait(self.driver, 10).until(
               EC.presence_of_element_located(self.SUBSCRIPTION_PAYMENT_BTN)
           )
           self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
           WebDriverWait(self.driver, 10).until(
               EC.element_to_be_clickable(self.SUBSCRIPTION_PAYMENT_BTN)
           )
           element.click()


