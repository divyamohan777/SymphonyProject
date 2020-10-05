from SymphonyTest.Pages.ForgotPassword import ForgotPassword
from SymphonyTest.Pages.Login import Login
from SymphonyTest.Support.errorMessages import errorMessages
from SymphonyTest.Pages.Authentication import Authentication
from SymphonyTest.Pages.SignUp import SignUp
from SymphonyTest.Support.genericSupportModule import visualdelay, gotoSymphonyChrome, gotoSymphonyEdge, gotoSymphonyFF
from SymphonyTest.Support.getTestData import getTestData
import pytest


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


def test_symphonytest_signup_existing_app(init_driver):
    signUp = SignUp(init_driver)
    signUp.exisitingsignUpbuttonclick(getTestData.InvalidSignUpFirstName, getTestData.InvalidSignUpLastName,
                                      getTestData.InvalidSignUpexisitingEmail,
                                      getTestData.InvalidSignUpPassword)
    visualdelay()


def test_symphonytest_signup_app(init_driver):
    signUp = SignUp(init_driver)
    signUp.validSignUpbuttonclick(getTestData.ValidSignUpFirstName, getTestData.ValidSignUpLastName,
                                  getTestData.ValidSignUpEmail,
                                  getTestData.ValidSignUpPassword)
    visualdelay()


def test_symphonytest_forgot_password(init_driver):
    forgotpassword = ForgotPassword(init_driver)
    forgotpassword.enterCaptchaInfo(getTestData.ValidUserName)


def test_symphonytest_invalidforgot_password(init_driver):
    forgotpassword = ForgotPassword(init_driver)
    forgotpassword.noEmailForgotPassword()
