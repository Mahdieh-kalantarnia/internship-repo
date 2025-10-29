from pages.base_page import Page
from selenium.webdriver.common.by import By





class Ambassadors(Page):
    SETTINGS = (By.XPATH, '//div[text()="Settings"]')

    def setting_btn(self):
        self.driver.find_element(*self.SETTINGS).click()
