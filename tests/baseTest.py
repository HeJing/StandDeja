import unittest
from selenium import webdriver


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.inteval_time = 20
        """
        self.driver=webdriver.Chrome("/Users/zhaorui/PycharmProjects/DejaCheckout/chromedriver")
        #self.driver=webdriver.Firefox()
        self.driver.implicitly_wait(self.inteval_time)
        self.driver.maximize_window()
        """
        driver_location = "/Users/suxiaoyin/PycharmProjects/DejaCredits/chromedriver"
        #driver_location = "/Users/jerryzhao/node_modules/appium/node_modules/appium-android-driver/node_modules/appium-chromedriver/chromedriver/mac/chromedriver"
        mobile_emulation = {"deviceName": "Google Nexus 5"}
        options = webdriver.ChromeOptions()
        options.add_experimental_option("mobileEmulation", mobile_emulation)
        self.driver = webdriver.Chrome(executable_path=driver_location, chrome_options=options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(self.inteval_time)


    def tearDown(self):
        # self.driver.close()
        pass
