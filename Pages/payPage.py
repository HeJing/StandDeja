import time
import basePages
from locators.locators import PayObj


class PayPage(basePages.BasePage):
    def payment(self):
        self.elemPay=self.driver.find_element(*PayObj.elemPay)
        self.payment_url=self.driver.current_url
        print("Proceed to payment.")
        self.mouse_click(self.elemPay)
        time.sleep(2)