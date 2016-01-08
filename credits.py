import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import baseTest
import string
# use from.... import .... to import the page which you want.
from creditsPage import CreditsPage
from locators import locators
from locators.locators import *
from loginPage import LoginPage


# here  you should use baseTest, because this is a testcase.


class TestCredits(baseTest.BaseTest):
    def setUp(self):
        super(TestCredits,self).setUp()
        self.credits_url="http://office.mozat.com:8083/redeemgif/"

    def test_credits(self):
        print(time.strftime("Start: "+'%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        crePage= CreditsPage(self.driver)
        self.driver.get(self.credits_url)
        crePage.LoginRedeem()
