import time
import baseTest
from Pages.buyPage import Buy
from Pages.changeMode import ChangeMode
from Pages.addtocartPage import AddtoCart
from Pages.checkoutPage import Checkout
from Pages.payPage import PayPage

class testAddtoCart(baseTest.BaseTest):
    def setUp(self):
        super(testAddtoCart,self).setUp()
        self.item_url="http://office.mozat.com:8083/dejafm/?debug=1#/product/id=102084"

    def test_add_to_cart(self):
        print(time.strftime("Start: "+'%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        self.driver.get(self.item_url)

        #buy
        buyItem=Buy(self.driver)
        changeMode=ChangeMode(self.driver)

        buyItem.buy()
        changeMode.changeDebugMode()
        buyItem.buy()

        #add to cart
        cart=AddtoCart(self.driver)

        cart.addtocart()
        cart.gotocart()

        #checkout
        check_out=Checkout(self.driver)
        check_out.checkout()

        #Payment
        pay=PayPage(self.driver)
        pay.payment()