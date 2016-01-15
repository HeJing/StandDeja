import time
import basePages
from locators.locators import BuyObj


class Buy(basePages.BasePage):
    def buy(self):
        #self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # Scroll up
        time.sleep(2)
        elemBuy=self.driver.find_element(*BuyObj.elemCartBuy)
        print("Click buy.")
        self.mouse_click(elemBuy)

    def chooseSize(self):
        elemSize=self.driver.find_element_by_xpath(*BuyObj.elemSize)
        print("Choose size.")
        self.mouse_click(elemSize)

