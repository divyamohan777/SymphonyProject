from SymphonyTest.PageObjects.loginPageObjects import loginPageObjects
from SymphonyTest.Support.getToken import getSMSverificationcode


class Authentication():
    def __init__(self, driver):
        self.driver = driver
        self.authenticationpath = loginPageObjects.passauthenticationcodeXpath
        self.authenticationbutton = loginPageObjects.authenticateButtonXpath
#Use 2FA Authentication using SMS verification code
    def authenticate(self):
        #Calling 2FA SMS verifcation retrival method
        auth_smscode = getSMSverificationcode()
        authenticatoncode = self.driver.find_elements_by_xpath(self.authenticationpath)
        authenticatoncode[0].send_keys(auth_smscode)
        verifybutton = self.driver.find_elements_by_xpath(self.authenticationbutton)
        verifybutton[0].click()
