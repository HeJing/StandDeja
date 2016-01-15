import time
import basePages


class PayPage(basePages.BasePage):
    def payment(self):
        self.elemPay=self.driver.find_element_by_xpath(*PayObj.elemPay)
        self.payment_url=self.driver.current_url
        print("Proceed to payment.")
        self.mouse_click(self.elemPay)
        time.sleep(2)