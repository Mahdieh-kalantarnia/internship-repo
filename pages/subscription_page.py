from selenium.webdriver.common.by import By
from pages.base_page import Page

class VerifyPage(Page):
    BACK_BTN = (By.XPATH, '//div[text()="Back"]')
    UPGRADE_BTN = (By.XPATH, '//div[text()="Upgrade plan"]')

    def __init__(self, driver):
        super().__init__(driver)

    def verify_title(self):
        title = self.driver.title
        if title == "Extend subscription":
            print("Title is correct: Extend subscription")
        else:
            print(f"Title is different: {title}")

    def verify_btn(self):
        back_button = self.driver.find_element(*self.BACK_BTN)
        upgrade_button = self.driver.find_element(*self.UPGRADE_BTN)
        assert back_button.is_displayed() and upgrade_button.is_displayed(), "TEST FAIL: Buttons not visible"
        print("TEST PASS: Both buttons are visible")