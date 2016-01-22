import time
import basePages
from locators.locators import OrderHistory


class OrderHis(basePages.BasePage):

    def orderHis(self):
        print("Order History")
        elemOrderHis=self.driver.find_element(*OrderHistory.elemOrderHis)
        self.mouse_click(elemOrderHis)
        time.sleep(1)