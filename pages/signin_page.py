from selenium.webdriver.common.by import By

from pages.base_page import Page




class SignIn(Page):

    USERNAME = (By.XPATH, '//input[@id="email-2"]')
    PASSWORD = (By.XPATH, '//input[@id="field"]')
    CONTINUE = (By.XPATH, '//a[text()="Continue"]')


    def username_password(self):

     self.driver.find_element(*self.USERNAME).send_keys("atefeh210@yahoo.com")
     self.driver.find_element(*self.PASSWORD).send_keys("Atefeh.210!")


    def continue_btn(self):
        self.driver.find_element(*self.CONTINUE).click()





