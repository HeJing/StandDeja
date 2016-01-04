import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import time

class BaseTest(unittest.TestCase):
    def setUp(self):
        self.inteval_time=20
        """
        self.driver=webdriver.Chrome("/Users/zhaorui/PycharmProjects/DejaCheckout/chromedriver")
        #self.driver=webdriver.Firefox()
        self.driver.implicitly_wait(self.inteval_time)
        self.driver.maximize_window()
        """
        driver_location = "/Users/suxiaoyin/PycharmProjects/DejaCredits/chromedriver"
        mobile_emulation = { "deviceName": "Google Nexus 5" }
        options = webdriver.ChromeOptions()
        options.add_experimental_option("mobileEmulation", mobile_emulation)
        self.driver = webdriver.Chrome(executable_path=driver_location, chrome_options=options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(self.inteval_time)

        # Assert whether the text exist in this page
    def is_text_present(self, text):
        try:
            body = self.driver.find_element_by_tag_name("body")
            # find body tag element
            #print("Show body's text:"+body.text)
        except NoSuchElementException, e:
            return False
        return text in body.text.encode('utf8') # check if the text is in body's text

    #assert whether the control exists in this page
    """
    def check_exists_by_xpath(self,xpath):
        try:
            self.driver.implicitly_wait(2)
            self.driver.find_element_by_xpath(xpath)
            self.driver.implicitly_wait(self.inteval_time)
        except NoSuchElementException:
            return False
        return True"""

    def check_exists_by_locator(self,by_method,locator_value):
        try:
            self.driver.implicitly_wait(2)
            self.driver.find_element(by_method, locator_value)
            self.driver.implicitly_wait(self.inteval_time)
        except NoSuchElementException:
            return False
        return True

    def mouse_click(self,o_element):
        time.sleep(1)
        actions = ActionChains(self.driver)
        actions.click(o_element)
        actions.perform()

    def tearDown(self):
        self.driver.close()
        #pass