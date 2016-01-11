import time
import string

from tests import baseTest
from locators.locators import BuyObj, CheckoutObj, PayObj, FBLogin


class history(baseTest.BaseTest):
    def setUp(self):
        super(test_history,self).setUp()

        # Define url
        self.item_url="http://office.mozat.com:8083/dejafm/?debug=1#/product/id=102084"
        #http://office.mozat.com:8083/dejafm/?debug=1&userid=xxx#/product/id=102084

        # Objects in login page
        self.xpath_fb_login="//i[@class='icon icon-btn_fb_login']"
        self.xpath_username="//input[@name='email']"
        self.xpath_pwd="//input[@name='pass']"
        self.xpath_submit="//button[@name='login']"

        # Define objects
        self.xpath_buy="//div[@class='btn bt-primary size-s buy normal']"
        #self.xpath_buy="//div[@data-id='102084']"
        #self.xpath_add_to_cart="btn bt-primary size-s add"
        self.xpath_checkout="//div[@class='btn bt-default size-s checkout']"
        self.xpath_card="//div[@class='detail ellipsis']"
        self.xpath_add_card="//section[@class='add-card']"

        self.xpath_sub_size="//div[@data-value='4']"

        # Objects in add addr
        self.xpath_add_addr_OK="//div[@class='yes']"
        self.xpath_add_addr="//section[@class='add-address']"

        # Objects in payment
        self.xpath_pay="//div[@class='btn bt-primary size-s pay']"

        # Objects after payment
        self.xpath_pay_his="//div[@class='bt-default size-s history']"
        self.xpath_order_his="//div[@class='bt-default size-s history']"

        #self.driver.get("http://m.deja.me/redeemgif/")

    def buy(self):
        #self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # Scroll up
        time.sleep(2)
        elemBuy=self.driver.find_element(*BuyObj.elemCartBuy)
        print("Click buy.")
        self.mouse_click(elemBuy)
        self.changeDebugMode()

    # Change debug mode
    def changeDebugMode(self):
        self.cur_url=self.driver.current_url
        self.new_url=string.replace(self.cur_url,'debug=1','debug=0')
        self.driver.get(self.new_url)

    def checkOut(self):
        elemSize=self.driver.find_element(*BuyObj.elemSize)
        print("Choose size.")
        self.mouse_click(elemSize)
        elemCheckout=self.driver.find_element(*CheckoutObj.elemCheckout)
        print("Check out now.")
        self.mouse_click(elemCheckout)
        if(self.check_exists_by_locator(*PayObj.elemPay)):
            self.payment()
        elif(self.check_exists_by_locator(*FBLogin.elemFBLogin)):
            print("Begin to login.")
            self.login()

            #check payment status: payment or not
            if(self.check_exists_by_locator(*PayObj.elemOrderHis)):
                time.sleep(3)
                ##########logical error need to modify############
                if(self.check_exists_by_locator(*PayObj.elemMsg)):
                    print("Failed to payment.")
                else:
                    print("Bala Bala")
            time.sleep(1)
            self.enterOrderHis() # Enter Order History

    # Enter Order History
    def enterOrderHis(self):
        print("Enter order history.")
        elemOrderHis=self.driver.find_element(*PayObj.elemOrderHis)
        self.mouse_click(elemOrderHis)

    def payment(self):
        self.elemPay=self.driver.find_element(*PayObj.elemPay)
        self.payment_url=self.driver.current_url
        self.mouse_click(self.elemPay)
        time.sleep(1)

    def addAddr(self):
        time.sleep(2)
        elemAddrOK=self.driver.find_element(*CheckoutObj.elemAddAddrOK)
        self.mouse_click(elemAddrOK)

        time.sleep(2)
        elemAddr=self.driver.find_element(*CheckoutObj.elemAddAddr)
        self.mouse_click(elemAddr)

    def contiPayment(self):
        self.driver.get(self.payment_url)
        self.mouse_click(self.elemPay)

    def login(self):
        elemLogin=self.driver.find_element(*FBLogin.elemFBLogin)
        self.mouse_click(elemLogin)
        time.sleep(2)
        if(self.check_exists_by_locator(*FBLogin.elemFBUsername)):
            print("Start to log in.")
            elemUsername=self.driver.find_element(*FBLogin.elemFBUsername)
            elemPwd=self.driver.find_element(*FBLogin.elemFBPwd)
            elemSubmit=self.driver.find_element(*FBLogin.elemFBSubmit)

            elemUsername.send_keys("ringsqa2@gmail.com")
            elemPwd.send_keys("Mozatm2u")
            self.mouse_click(elemSubmit)
            time.sleep(3)
        if(self.check_exists_by_locator(*CheckoutObj.elemCheckout)):
            print("payment again.")
            self.checkOut()

    def enterItem(self):
        self.driver.get(self.item_url)
        self.buy()
        self.checkOut()

    def test_checkout(self):
        print(time.strftime("Start: "+'%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        self.driver.get(self.item_url)
        self.buy()
        time.sleep(3)
        self.checkOut()

        if(self.check_exists_by_locator(*CheckoutObj.elemCheckout)):
            print("Find way to cart.")
            #time.sleep(2)
            self.checkOut()
        print(time.strftime("End: "+'%Y-%m-%d %H:%M:%S',time.localtime(time.time())))