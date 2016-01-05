import unittest
import time
import baseTest
import string
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from locators.locators import BuyObj, AddtoCart, PayObj, FBLogin


class AddToCart(baseTest.BaseTest):
    def setUp(self):
        super(AddToCart,self).setUp()

        # Define item url
        self.item_url="http://office.mozat.com:8083/dejafm/?debug=1#/product/id=102084"
        self.his_url="http://office.mozat.com:8083/dejafm/?debug=0#/orderhistory/"

        # Objects in fb login
        self.credits_url="http://office.mozat.com:8083/redeemgif/"

        """
        # Objects in item details
        self.xpath_buy="//div[@class='btn bt-primary size-s buy normal']"

        # Objects in buy
        self.xpath_sub_size="//div[@data-value='4']"
        self.xpath_add_to_cart="//div[@class='btn bt-primary size-s add']"
        self.xpath_go_to_cart="//div[@class='btn bt-primary size-s cart']"

        # Objects in cart
        self.xpath_checkout="//div[@class='btn bt-primary size-s co normal']"

        # Objects about login
        self.xpath_fb_login="//i[@class='icon icon-btn_fb_login default-active']"
        self.xpath_username="//input[@name='email']"
        self.xpath_pwd="//input[@name='pass']"
        self.xpath_submit="//button[@name='login']"
        """

        """
        self.xpath_fb_login="//i[@class='icon icon-btn_fb_login']"
        self.xpath_username="//input[@name='email']"
        self.xpath_pwd="//input[@name='pass']"
        self.xpath_submit="//button[@name='login']"
        """

        # Objects in payment
        self.xpath_pay="//div[@class='btn bt-primary size-s pay']"
        self.xpath_pay_his="//div[@class='bt-default size-s history']"
        self.xpath_order_his="//div[@class='bt-default size-s history']"

    def buy(self):
        #self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # Scroll up
        time.sleep(1)
        elemBuy=self.driver.find_element(*BuyObj.elemCartBuy)
        print("Click to buy.")
        self.mouse_click(elemBuy)
        self.changeDebugMode()
        self.addToCart()

    # debug=1-->debug=0
    def changeDebugMode(self):
        self.cur_url=self.driver.current_url
        self.d0_url=string.replace(self.cur_url,"debug=1","debug=0")
        self.driver.get(self.d0_url)

    def addToCart(self):
        elemSize=self.driver.find_element(*BuyObj.elemSize)
        print("Choose size.")
        self.mouse_click(elemSize)
        elemAddToCart=self.driver.find_element(*AddtoCart.elemAddtoCart)
        self.mouse_click(elemAddToCart)
        print("Add to cart.")
        elemToCart=self.driver.find_element(*AddtoCart.elemGotoCart)
        self.mouse_click(elemToCart)
        print("Go to cart.")

    def checkout(self):
        print("Checkout")
        elemCheckout=self.driver.find_element(*AddtoCart.elemCartCheckout)
        self.mouse_click(elemCheckout)
        time.sleep(2)
        # Login or payment
        if(self.check_exists_by_locator(*PayObj.elemPay)):
            self.payment()
            print("Payment")

            if(self.check_exists_by_locator(*PayObj.elemOrderHis)):
                time.sleep(2)
                if(self.is_text_present("Sorry")):
                    print("Failed to payment.")
                else:
                    print("Bala Bala")
                time.sleep(2)
                print("Go to order history.")
                self.enterOrderHis() # Enter Order History

    def login(self):
        elemLogin=self.driver.find_element(*FBLogin.elemFBLogin)
        self.mouse_click(elemLogin)
        time.sleep(1)

        elemUsername=self.driver.find_element(*FBLogin.elemFBUsername)
        elemPassword=self.driver.find_element(*FBLogin.elemFBPwd)
        elemSubmit=self.driver.find_element(*FBLogin.elemFBSubmit)

        elemUsername.send_keys("ringsqa2@gmail.com")
        elemPassword.send_keys("mozatm2u")
        self.mouse_click(elemSubmit)

        time.sleep(4)
        if(self.is_text_present("Your Credits")):
            print("Login successfully!")

        else:
            print("Failed to login.")

    """
    def login(self):
        elemLogin=self.driver.find_element_by_xpath(self.xpath_fb_login)
        self.mouse_click(elemLogin)
        time.sleep(2)
        if(self.check_exists_by_xpath(self.xpath_username)):
            print("Input username & pwd.")
            elemUsername=self.driver.find_element_by_xpath(self.xpath_username)
            elemPwd=self.driver.find_element_by_xpath(self.xpath_pwd)
            elemSubmit=self.driver.find_element_by_xpath(self.xpath_submit)

            elemUsername.send_keys("ringsqa2@gmail.com")
            elemPwd.send_keys("Mozatm2u")
            self.mouse_click(elemSubmit)
            print("Log in.")
            time.sleep(2)
        if(self.check_exists_by_xpath(self.xpath_checkout)):
            print("check out again.")
            self.checkout()
            """

    def payment(self):
        self.elemPay=self.driver.find_element(*PayObj.elemPay)
        self.payment_url=self.driver.current_url
        print("Proceed to payment.")
        self.mouse_click(self.elemPay)
        time.sleep(2)

    def enterOrderHis(self):
        elemOrderHis=self.driver.find_element()
        self.mouse_click(elemOrderHis)

    def test_addToCart(self):
        print(time.strftime("Login time: "+'%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        self.driver.get(self.credits_url)
        if(self.check_exists_by_locator(*FBLogin.elemFBLogin)):
            print("Login")
            self.login()
        elif(self.is_text_present("Your Credits")):
            print("Already login.")
        self.driver.get(self.item_url)
        self.buy()
        time.sleep(1)
        self.checkout()
        print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))