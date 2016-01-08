import time
import basePages
from locators.locators import FBLogin

class LoginPage(basePages.BasePage):
   def login(self):
        elemUsername=self.driver.find_element(*FBLogin.elemFBUsername)
        elemPassword=self.driver.find_element(*FBLogin.elemFBPwd)
        elemSubmit=self.driver.find_element(*FBLogin.elemFBSubmit)

        elemUsername.send_keys("ringsqa2@gmail.com")
        elemPassword.send_keys("mozatm2u")
        self.mouse_click(elemSubmit)