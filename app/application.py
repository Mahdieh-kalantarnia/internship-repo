from pages.base_page import Page
from pages.ambassadors_page import Ambassadors
from pages.setting_page import Setting
from pages.main_page import MainPage
from pages.subscription_page import VerifyPage

from pages.signin_page import SignIn


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.page = Page(driver)
        self.ambassadors_page = Ambassadors(driver)
        self.setting_page = Setting(driver)
        self.signin_page = SignIn(driver)
        self.subscription_page = VerifyPage(driver)
        self.main_page = MainPage(driver)




