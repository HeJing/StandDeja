from Pages.creditsPage import CreditsPage
import basePages
from locators.locators import FBLogin, Credits
import time


class FacebookLoginPage(basePages.BasePage):
    def type_username_and_password(self, username, password):
        """

        :param username:
        :param password:
        """
        time.sleep(2)
        print("Login")
        elem_username = self.driver.find_element(*FBLogin.elemFBUsername)
        elem_password = self.driver.find_element(*FBLogin.elemFBPwd)
        elem_username.send_keys(username)
        elem_password.send_keys(password)

    def tap_login_button(self):
        elem_submit = self.driver.find_element(*FBLogin.elemFBSubmit)
        self.mouse_click(elem_submit)
        time.sleep(5)
        print(time.strftime("End: " + '%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

        # if (self.is_text_present("Your Credits")):
        #     print("Login successfully!")
        #     crePage.redeem()
        # else:
        #     print("Failed to login.")

        # return credits page
        return CreditsPage(self.driver)
