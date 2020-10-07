from SymphonyTest.PageObjects.signUpPageObjects import signUpPageObjects
from SymphonyTest.Support.errorMessages import errorMessages
from time import sleep


class SignUp():
    #capturing sign up module webelements from page objects
    def __init__(self, driver):
        self.driver = driver
        self.signUpClick = signUpPageObjects.signUplinkXpath
        self.firstName = signUpPageObjects.firstNameXpath
        self.lastName = signUpPageObjects.lastNameXpath
        self.emailAddress = signUpPageObjects.emailaddressXpath
        self.signUpPassword = signUpPageObjects.signUpPasswordXpath
        self.activesignUpbutton = signUpPageObjects.activesignUpbuttonXpath
        self.existingSignUperror = signUpPageObjects.signupErrorXpath
        self.signclose = signUpPageObjects.signUpClose
    # Sign up method until email validation 
    def clickonSignUp(self, firstname, lastname, email, password):
        signUpClickElement = self.driver.find_elements_by_xpath(self.signUpClick)
        self.driver.implicitly_wait(2)
        signUpClickElement[0].click()
        self.driver.implicitly_wait(2)
        firstNameelement = self.driver.find_elements_by_xpath(self.firstName)
        firstNameelement[0].send_keys(firstname)
        lastNameElement = self.driver.find_elements_by_xpath(self.lastName)
        lastNameElement[0].send_keys(lastname)
        emailAddresselement = self.driver.find_elements_by_xpath(self.emailAddress)
        emailAddresselement[0].send_keys(email)
        signUpPasswordElement = self.driver.find_elements_by_xpath(self.signUpPassword)
        signUpPasswordElement[0].send_keys(password)
        activesignUpbutton = self.driver.find_elements_by_xpath(self.activesignUpbutton)
        activesignUpbutton[0].click()
    #exiting sign up method
    def exisitingsignUpbuttonclick(self, firstname, lastname, email, password):
        self.clickonSignUp(firstname, lastname, email, password)
        self.driver.implicitly_wait(2)
        signupError = self.driver.find_elements_by_xpath(self.existingSignUperror)
        message = signupError[0].text
        errmessage = errorMessages.invalidSignUpMessage
        self.driver.implicitly_wait(2)
        assert message == errmessage
        signclosebutton = self.driver.find_elements_by_xpath(self.signclose)
        signclosebutton[0].click()

    def validSignUpbuttonclick(self, firstname, lastname, email, password):
        self.clickonSignUp(firstname, lastname, email, password)
        self.driver.implicitly_wait(2)

