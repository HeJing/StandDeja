from Pages.creditsPage import CreditsPage
from Pages.loginPage import FacebookLoginPage
import basePages
from locators.locators import FBLogin, Credits
import time


class HomePage(basePages.BasePage):

    def tap_on_login_with_facebook(self):
        elem_login = self.driver.find_element(*Credits.elemCreLogin)
        self.mouse_click(elem_login)
        time.sleep(2)
        return FacebookLoginPage(self.driver)
