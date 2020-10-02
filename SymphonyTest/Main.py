from SymphonyTest.Pages.ForgotPassword import ForgotPassword
from SymphonyTest.Pages.Login import Login
from SymphonyTest.Support.errorMessages import errorMessages
from SymphonyTest.Pages.Authentication import Authentication
from SymphonyTest.Pages.SignUp import SignUp
from SymphonyTest.Support.genericSupportModule import visualdelay
from SymphonyTest.Support.genericSupportModule import gotoSymphony
from SymphonyTest.Support.getTestData import getTestData

def test_symphonytest_validlogin_app():
    chrome_driver = gotoSymphony()
    login = Login(chrome_driver)
    login.enterUsername(getTestData.ValidUserName)
    login.enterPassword(getTestData.ValidPassword)
    login.loginbuttonclick()
    visualdelay()
    auth = Authentication(chrome_driver)
    auth.authenticate()
    assert chrome_driver.title == "Symphony | Secure Seamless Communication"
    visualdelay()
    chrome_driver.close()


def test_symphonytest_emptylogin_test():
    chrome_driver = gotoSymphony()
    login = Login(chrome_driver)
    login.enterUsername("")
    login.enterPassword("")
    login.loginbuttonclick()
    visualdelay()
    message = login.loginError()
    emptyLoginerrorMessage = errorMessages.emptyloginerrorMessage
    assert message == emptyLoginerrorMessage
    visualdelay()
    chrome_driver.close()


def test_symphonytest_invalidlogin_test():
    chrome_driver = gotoSymphony()
    login = Login(chrome_driver)
    login.enterUsername(getTestData.InvalidUserName)
    login.enterPassword(getTestData.ValidPassword)
    login.loginbuttonclick()
    visualdelay()
    message = login.loginError()
    invalidLoginerrorMessage = errorMessages.invalidloginerrorMessage
    assert message == invalidLoginerrorMessage
    visualdelay()
    chrome_driver.close()


def test_symphonytest_sign_app():
    chrome_driver = gotoSymphony()
    signUp = SignUp(chrome_driver)
    signUp.clickonSignUp(getTestData.FirstName, getTestData.LastName, getTestData.SignUpexisitingEmail, getTestData.Password)
    visualdelay()


def test_symphonytest_forgot_password():
    chrome_driver = gotoSymphony()
    forgottpassword = ForgotPassword(chrome_driver)
    forgottpassword.clickonForgotPassword()
    forgottpassword.enterCaptchaInfo(getTestData.ValidUserName)
