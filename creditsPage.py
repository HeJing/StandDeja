import unittest
from selenium import webdriver
import time
import basePages
from locators import locators
from locators.locators import Credits, FBLogin
from loginPage import LoginPage


class CreditsPage(basePages.BasePage):
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

    def LoginRedeem(self):
        crePage= CreditsPage(self.driver)
        creLogin=LoginPage(self.driver)
        if(self.check_exists_by_locator(*locators.FBLogin.elemFBLogin)):
            elemLogin=self.driver.find_element(*Credits.elemCreLogin)
            self.mouse_click(elemLogin)
            time.sleep(2)
            print("Login")
            creLogin.login()
            time.sleep(5)

            if(self.is_text_present("Your Credits")):
                print("Login successfully!")
                crePage.redeem()
            else:
                print("Failed to login.")

        elif(self.is_text_present("Your Credits")):
            print("Redeem")
            crePage.redeem()

        else:
            print("Error")
        print(time.strftime("End: "+'%Y-%m-%d %H:%M:%S',time.localtime(time.time())))