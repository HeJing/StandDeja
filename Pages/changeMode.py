import string
import basePages

class ChangeMode(basePages.BasePage):
    def changeDebugMode(self):
        self.cur_url=self.driver.current_url
        self.d0_url=string.replace(self.cur_url,"debug=1","debug=0")
        self.driver.get(self.d0_url)