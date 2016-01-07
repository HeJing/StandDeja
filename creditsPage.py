import unittest
from selenium import webdriver
import time
import basePages
from locators.locators import Credits, FBLogin


class CreditsPage(basePages.BasePage):
    def login(self):
        elemLogin=self.driver.find_element(*Credits.elemCreLogin)
        self.mouse_click(elemLogin)
        time.sleep(2)
        basePages.BasePage.login()

    def redeem(self):
        #time.sleep(2)
        if(self.check_exists_by_locator(*Credits.elemRedeem)):
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
