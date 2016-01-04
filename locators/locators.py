from selenium.webdriver.common.by import By

class baseLocators():
        pass

class FBLogin(baseLocators):
        # Objects in login page
        elemFBLogin=(By.XPATH,"//i[@class='icon icon-btn_fb_login']")
        elemFBUsername=(By.XPATH,"//input[@name='email']")
        elemFBPwd=(By.XPATH,"//input[@name='pass']")
        elemFBSubmit=(By.XPATH,"//button[@name='login']")


class BuyObj(baseLocators):
        elemCartBuy=(By.XPATH,"//div[@class='btn bt-primary size-s buy normal']")
        elemSize=(By.XPATH,"//div[@data-value='4']")

class PayObj(baseLocators):
        # Objects in payment
        elemPay=(By.XPATH,"//div[@class='btn bt-primary size-s pay']")
        elemPayHis=(By.XPATH,"//div[@class='bt-default size-s history']")
        elemOrderHis=(By.XPATH,"//div[@class='bt-default size-s history']")

class CheckoutObj(baseLocators):
        # Objects in add to cart
        elemCheckout=(By.XPATH,"//div[@class='btn bt-default size-s checkout']")
        elemCard=(By.XPATH,"//div[@class='detail ellipsis']")
        elemAddCard=(By.XPATH,"//section[@class='add-card']")

        # Objects in add addr
        elemAddAddrOK=(By.XPATH,"//div[@class='yes']")
        elemAddAddr=(By.XPATH,"//section[@class='add-address']")


class AddtoCart(baseLocators):
        elemAddtoCart=(By.XPATH,"//div[@class='btn bt-primary size-s add']")
        elemGotoCart=(By.XPATH,"//div[@class='btn bt-primary size-s cart']")

        # Objects in cart
        elemCartCheckout=(By.XPATH,"//div[@class='btn bt-primary size-s co normal']")

class Credits(baseLocators):
        # Objects about login
        elemCreLogin=(By.XPATH,"//i[@class='icon icon-btn_fb_login default-active']")

        # Objects in redeem
        elemRedeem=(By.XPATH,"//div[@class='btn bt-c size-s uppercase normal']")
        elemReName=(By.XPATH,"//input[@class='name']")
        elemReMail=(By.XPATH,"//input[@class='mail']")
        elemRePhone=(By.XPATH,"//input[@class='phone']")
        elemReAddr=(By.XPATH,"//input[@class='address']")
        elemReSubmit=(By.XPATH,"//div[@class='btn bt-b']")
        elemReConfirm=(By.XPATH,"//div[@class='yes']")

        # Objects in redeem within 30 days
        elemFailOK=(By.XPATH,"//div[@class='yes']")