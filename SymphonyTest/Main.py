from SymphonyTest.Pages.ForgotPassword import ForgotPassword
from SymphonyTest.Pages.Login import Login
from SymphonyTest.Support.errorMessages import errorMessages
from SymphonyTest.Pages.Authentication import Authentication
from SymphonyTest.Pages.SignUp import SignUp
from SymphonyTest.Support.genericSupportModule import visualdelay, gotoSymphonyChrome, gotoSymphonyEdge, gotoSymphonyFF
from SymphonyTest.Support.getTestData import getTestData
import pytest

#fixature for driver and closing the session
@pytest.fixture(params=["chrome", "edge", "firefox", "safari"], scope="class")
def init_driver(request):
    if request.param == "chrome":
        web_driver = gotoSymphonyChrome()
    if request.param == "edge":
        web_driver = gotoSymphonyEdge()
    if request.param == "firefox" or request.param == "safari":
        pytest.skip("Browser Not supported")
    yield web_driver
    web_driver.close()

#1. test case to for valid login with 2FA authentication
def test_symphonytest_validlogin_app(init_driver):
    login = Login(init_driver)
    login.enterUsername(getTestData.ValidUserName)
    login.enterPassword(getTestData.ValidPassword)
    login.loginbuttonclick()
    visualdelay()
    auth = Authentication(init_driver)
    auth.authenticate()
    assert init_driver.title == "Symphony | Secure Seamless Communication"
    visualdelay()

#Test case to alidate an empty login 
def test_symphonytest_emptylogin_test(init_driver):
    login = Login(init_driver)
    login.enterUsername("")
    login.enterPassword("")
    login.loginbuttonclick()
    visualdelay()
    message = login.loginError()
    emptyLoginerrorMessage = errorMessages.emptyloginerrorMessage
    assert message == emptyLoginerrorMessage
    visualdelay()

#Test Case to validate invalid login
def test_symphonytest_invalidlogin_test(init_driver):
    login = Login(init_driver)
    login.enterUsername(getTestData.InvalidUserName)
    login.enterPassword(getTestData.ValidPassword)
    login.loginbuttonclick()
    visualdelay()
    message = login.loginError()
    invalidLoginerrorMessage = errorMessages.invalidloginerrorMessage
    assert message == invalidLoginerrorMessage
    visualdelay()

#Test case to validate an exisitng email ids sign up attempt
def test_symphonytest_signup_existing_app(init_driver):
    signUp = SignUp(init_driver)
    signUp.exisitingsignUpbuttonclick(getTestData.InvalidSignUpFirstName, getTestData.InvalidSignUpLastName,
                                      getTestData.InvalidSignUpexisitingEmail,
                                      getTestData.InvalidSignUpPassword)
    visualdelay()

#Test case to Sign up a new user
def test_symphonytest_signup_app(init_driver):
    signUp = SignUp(init_driver)
    signUp.validSignUpbuttonclick(getTestData.ValidSignUpFirstName, getTestData.ValidSignUpLastName,
                                  getTestData.ValidSignUpEmail,
                                  getTestData.ValidSignUpPassword)
    visualdelay()

#Test case to validate forgot password module for an existing user
def test_symphonytest_forgot_password(init_driver):
    forgotpassword = ForgotPassword(init_driver)
    forgotpassword.enterCaptchaInfo(getTestData.ValidUserName)

#test case to validate forgot word for an non exisitng user 
def test_symphonytest_invalidforgot_password(init_driver):
    forgotpassword = ForgotPassword(init_driver)
    forgotpassword.noEmailForgotPassword()
