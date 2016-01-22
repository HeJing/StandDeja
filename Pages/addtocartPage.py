import time
import basePages
from locators.locators import AddtoCart, FBLogin, CheckoutObj


class AddToCart(basePages.BasePage):
    def addtocart(self):
        elemAddToCart=self.driver.find_element(*AddtoCart.elemAddtoCart)
        self.mouse_click(elemAddToCart)
        print("Add to cart.")

    def gotocart(self):
        elemToCart=self.driver.find_element(*AddtoCart.elemGotoCart)
        self.mouse_click(elemToCart)
        print("Go to cart.")

    def checkout(self):
        print("Checkout")
        elemCheckoutCart=self.driver.find_element(*CheckoutObj.elemCartCheckout)
        self.mouse_click(elemCheckoutCart)
        time.sleep(2)
        elemCheckout=self.driver.find_element(*AddtoCart.elemCartCheckout)
        self.mouse_click(elemCheckout)
        time.sleep(2)

    def loginEntrance(self):
        print("Begin to login")
        elemLogin=self.driver.find_element(*FBLogin.elemFBLogin)
        self.mouse_click(elemLogin)
        time.sleep(1)