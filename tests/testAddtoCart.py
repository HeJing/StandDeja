import time
import baseTest

class testAddtoCart(baseTest.BaseTest):
    def setUp(self):
        super(testAddtoCart,self).setUp()
        self.item_url="http://office.mozat.com:8083/dejafm/?debug=1#/product/id=102084"

    def test_add_to_cart(self):
        print(time.strftime("Start: "+'%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        self.driver.get(self.item_url)