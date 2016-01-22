import time
from Pages.orderHisPages import OrderHis
import baseTest
from Pages.buyPage import Buy
from Pages.changeMode import ChangeMode
from Pages.addtocartPage import AddToCart
from Pages.checkoutPage import Checkout
from Pages.payPage import PayPage
from Pages.chooseSizePage import ChooseSize
from Pages.loginPage import FacebookLoginPage

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
        #buyItem.buy()

        #add to cart
        choose_size=ChooseSize(self.driver)
        cart=AddToCart(self.driver)

        choose_size.chooseSize()
        cart.addtocart()
        cart.gotocart()
        time.sleep(2)

        #checkout
        cart.checkout()

        # Login in FB
        cart.loginEntrance()
        login=FacebookLoginPage(self.driver)
        login.type_username_and_password("ringsqa2@gmail.com","mozatm2u")
        login.tap_login_button()

        # Checkout
        cart.checkout()

        #Payment
        pay=PayPage(self.driver)
        pay.payment()

        # Order History
        order_his=OrderHis.orderHis()

        print(time.strftime("End: " + '%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
