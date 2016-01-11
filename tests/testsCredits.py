import time


# use from.... import .... to import the page which you want.


# here  you should use baseTest, because this is a testcase.
from Pages.homePage import HomePage
from Pages.loginPage import FacebookLoginPage
from tests.baseTest import BaseTest


class TestCredits(BaseTest):
    def setUp(self):
        super(TestCredits, self).setUp()
        self.credits_url = "http://office.mozat.com:8083/redeemgif/"

    def test_credits(self):
        print(time.strftime("Start: "+'%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        self.driver.get(self.credits_url)
        home_page = HomePage(self.driver)
        f_login = home_page.tap_on_login_with_facebook()
        f_login.type_username_and_password("ringsqa2@gmail.com", "mozatm2u")
        credits_page = f_login.tap_login_button()
        credits_page.redeem()
