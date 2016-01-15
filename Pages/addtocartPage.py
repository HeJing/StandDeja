import basePages
from locators.locators import AddtoCart

class AddtoCart(basePages.BasePage):
    def addtocart(self):
        elemAddToCart=self.driver.find_element_by_xpath(*AddtoCart.elemAddtoCart)
        self.mouse_click(elemAddToCart)
        print("Add to cart.")

    def gotocart(self):
        elemToCart=self.driver.find_element_by_xpath(*AddtoCart.elemGotoCart)
        self.mouse_click(elemToCart)
        print("Go to cart.")