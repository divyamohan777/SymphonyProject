from SymphonyTest.PageObjects.loginPageObjects import loginPageObjects
class Login():

    def __init__(self, driver):
        self.driver = driver
        self.usernameXpath = loginPageObjects.usernameXpath
        self.passwordXpath = loginPageObjects.passwordXpath
        self.loginbuttonXpath = loginPageObjects.loginbuttonXpath
        self.loginerrorXpath = loginPageObjects.loginerrorXpath

    def enterUsername(self, username):
        login = self.driver.find_elements_by_xpath(self.usernameXpath)
        login[0].send_keys(username)

    def enterPassword(self, password):
        passwordelement = self.driver.find_elements_by_xpath(self.passwordXpath)
        passwordelement[0].send_keys(password)

    def loginbuttonclick(self):
        loginbutton = self.driver.find_elements_by_xpath(self.loginbuttonXpath)
        loginbutton[0].click()

    def loginError(self):
        loginerrorelement = self.driver.find_elements_by_xpath(self.loginerrorXpath)
        message = loginerrorelement[0].text
        return message

