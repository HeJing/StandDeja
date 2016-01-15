import time
import basePages
from locators.locators import AddtoCart

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
        elemCheckout=self.driver.find_element(*AddtoCart.elemCartCheckout)
        self.mouse_click(elemCheckout)
        time.sleep(2)