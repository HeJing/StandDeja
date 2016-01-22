import time
import basePages
from locators.locators import CheckoutObj


class Checkout(basePages.BasePage):
    def checkout(self):
        print("Checkout")
        elemCheckout=self.driver.find_element(*CheckoutObj.elemCheckout)
        self.mouse_click(elemCheckout)
        time.sleep(2)
