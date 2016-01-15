import basePages
from locators.locators import BuyObj


class ChooseSize(basePages.BasePage):

    def chooseSize(self):
        elemSize=self.driver.find_element(*BuyObj.elemSize)
        print("Choose size.")
        self.mouse_click(elemSize)