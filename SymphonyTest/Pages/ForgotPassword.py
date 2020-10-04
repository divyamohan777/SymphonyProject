from SymphonyTest.PageObjects.forgotPasswordPageObjects import forgotPasswordPageObjects
from SymphonyTest.Support.errorMessages import errorMessages
from SymphonyTest.Support.genericSupportModule import visualdelay
from selenium.common.exceptions import NoSuchElementException


class ForgotPassword():

    def __init__(self, driver):
        self.driver = driver
        self.forgotPassword = forgotPasswordPageObjects.ForgotLinkXpath
        self.recoverEmail = forgotPasswordPageObjects.forgotpasswordEmail
        self.checkCaptcha = forgotPasswordPageObjects.checkCaptchaXpath
        self.checkCaptchaClass = forgotPasswordPageObjects.checkCaptchaClass
        self.captchaFrame = forgotPasswordPageObjects.checkCaptchaiFrametag
        self.captchaFrameclick = forgotPasswordPageObjects.captchaframeXpath
        self.captchaAudio = forgotPasswordPageObjects.captchaaudioButton
        self.captchaError = forgotPasswordPageObjects.captchaAudioError

    def clickonForgotPassword(self):
        ForgotLinkXpathElement = self.driver.find_elements_by_xpath(self.forgotPassword)
        ForgotLinkXpathElement[0].click()

    def enterCaptchaInfo(self, email):
        recoverEmail = self.driver.find_elements_by_xpath(self.recoverEmail)
        self.driver.implicitly_wait(4)
        recoverEmail[0].send_keys(email)
        visualdelay()
        captchaclass = self.driver.find_element_by_class_name(self.checkCaptchaClass)
        checkCaptcha = captchaclass.find_element_by_tag_name(self.captchaFrame)
        checkCaptcha.click()
        visualdelay()
        self.driver.switch_to.frame(self.driver.find_element_by_xpath(self.captchaFrameclick))
        visualdelay()
        self.driver.find_element_by_id(self.captchaAudio).click()
        visualdelay()
        if self.check_exists_by_xpath():
            captchaError = self.driver.find_elements_by_xpath(self.captchaError)[0].text
            assert captchaError == errorMessages.captchaError

    def check_exists_by_xpath(self):
        try:
            self.driver.find_elements_by_xpath(self.captchaError)[0]
        except NoSuchElementException:
            return False
        return True
