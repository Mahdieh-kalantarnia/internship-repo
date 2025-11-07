from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




class Ambassadors(Page):
    SETTINGS = (By.XPATH, '//div[text()="Menu"]')

    def setting_btn(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SETTINGS)
        )
        element.click()
