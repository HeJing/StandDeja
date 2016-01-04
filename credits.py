import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import baseTest
import string
from locators import locators
from locators.locators import *


class TestCredits(baseTest.BaseTest):
    def setUp(self):
        super(TestCredits,self).setUp()

        self.credits_url="http://office.mozat.com:8083/redeemgif/"

    def login(self):
        elemLogin=self.driver.find_element(*Credits.elemCreLogin)
        self.mouse_click(elemLogin)
        time.sleep(2)


        elemUsername=self.driver.find_element(*FBLogin.elemFBUsername)
        elemPassword=self.driver.find_element(*FBLogin.elemFBPwd)
        elemSubmit=self.driver.find_element(*FBLogin.elemFBSubmit)

        elemUsername.send_keys("ringsqa2@gmail.com")
        elemPassword.send_keys("mozatm2u")
        self.mouse_click(elemSubmit)

        time.sleep(5)
        if(self.is_text_present("Your Credits")):
            print("Login successfully!")
            self.redeem()
        else:
            print("Failed to login.")

    def redeem(self):
        #time.sleep(2)
        if(self.check_exists_by_locator(*locators.Credits.elemRedeem)):
            elemRedeem=self.driver.find_element(*Credits.elemRedeem)
            self.mouse_click(elemRedeem)
            time.sleep(2)
            if(self.is_text_present("Sorry")):
                print("Failed to redeem.You need to redeem gifts in every 30 days.")
                return
                #self.mouse_click(self.xpath_fail_ok)
            if(self.check_exists_by_locator(*Credits.elemReSubmit)):
                elemReName=self.driver.find_element(*Credits.elemReName)
                elemReEmail=self.driver.find_element(*Credits.elemReMail)
                elemRePhone=self.driver.find_element(*Credits.elemRePhone)
                elemReAddr=self.driver.find_element(*Credits.elemReAddr)
                elemReSubmit=self.driver.find_element(*Credits.elemReSubmit)

                #input contact info
                elemReName.send_keys("Test")
                elemReEmail.send_keys("Test@mozat.com")
                elemRePhone.send_keys("11111111")
                elemReAddr.send_keys("sdjfls;dfjasl;dfj;asljfas")
                self.mouse_click(elemReSubmit)

                time.sleep(5)
                if(self.check_exists_by_locator(*Credits.elemReConfirm)):
                    elemReConfirm=self.driver.find_element(*Credits.elemReConfirm)
                    print("Confirm")
                    self.mouse_click(elemReConfirm)

    def test_credits(self):
        print(time.strftime("Start: "+'%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        self.driver.get(self.credits_url)
        if(self.check_exists_by_locator(*locators.FBLogin.elemFBLogin)):
            print("Login")
            self.login()
        elif(self.is_text_present("Your Credits")):
            print("Redeem")
            self.redeem()
        else:
            print("Error")
        print(time.strftime("End: "+'%Y-%m-%d %H:%M:%S',time.localtime(time.time())))