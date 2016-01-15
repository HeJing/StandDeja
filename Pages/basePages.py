import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import string


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.inteval_time = 20

    # Assert whether the text exist in this page
    def is_text_present(self, text):
        try:
            body = self.driver.find_element_by_tag_name("body")
            # find body tag element
            # print("Show body's text:"+body.text)
        except NoSuchElementException, e:
            return False
        return text in body.text.encode('utf8')  # check if the text is in body's text

    # assert whether the control exists in this page
    """
    def check_exists_by_xpath(self,xpath):
        try:
            self.driver.implicitly_wait(2)
            self.driver.find_element_by_xpath(xpath)
            self.driver.implicitly_wait(self.inteval_time)
        except NoSuchElementException:
            return False
        return True"""

    def check_exists_by_locator(self, by_method, locator_value):
        try:
            self.driver.implicitly_wait(2)
            self.driver.find_element(by_method, locator_value)
            self.driver.implicitly_wait(self.inteval_time)
        except NoSuchElementException:
            return False
        return True

    def mouse_click(self, o_element):
        time.sleep(1)
        actions = ActionChains(self.driver)
        actions.click(o_element)
        actions.perform()

    # Change debug mode
    def changeDebugMode(self):
        self.cur_url=self.driver.current_url
        self.new_url=string.replace(self.cur_url,'debug=1','debug=0')
        self.driver.get(self.new_url)
