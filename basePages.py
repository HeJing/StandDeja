from selenium.common.exceptions import NoSuchElementException
import time
from locators.locators import FBLogin
import baseTest

class BasePage(baseTest.BaseTest):
    def __init__(self, driver):
        self.driver = driver

    def login(self):
        elemUsername=self.driver.find_element(*FBLogin.elemFBUsername)
        elemPassword=self.driver.find_element(*FBLogin.elemFBPwd)
        elemSubmit=self.driver.find_element(*FBLogin.elemFBSubmit)

        elemUsername.send_keys("ringsqa2@gmail.com")
        elemPassword.send_keys("mozatm2u")
        self.mouse_click(elemSubmit)

        time.sleep(5)
        if(self.is_text_present("Your Credits")):
            print("Login successfully!")
            self.redeem()
        else:
            print("Failed to login.")