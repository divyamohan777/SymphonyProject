import yaml
import os


class getTestData():
    HOME = os.environ['HOME']
    with open(HOME+"/PycharmProjects/pythonProject2/SymphonyTest/Support/TestData.yaml", "r") as ymlfile:
        testdata = yaml.safe_load(ymlfile)
        ValidUserName = testdata["ValidLogin"]["ValidUserName"]
        ValidPassword = testdata["ValidLogin"]["ValidPassword"]
        InvalidUserName = testdata["InvalidLogin"]["InvalidUserName"]
        InvalidPassword = testdata["InvalidLogin"]["InvalidPassword"]
        InvalidSignUpFirstName= testdata["InvalidSignUp"]["FirstName"]
        InvalidSignUpLastName = testdata["InvalidSignUp"]["LastName"]
        InvalidSignUpexisitingEmail = testdata["InvalidSignUp"]["SignUpexisitingEmail"]
        InvalidSignUpPassword = testdata["validSignUp"]["Password"]
        ValidSignUpFirstName = testdata["validSignUp"]["FirstName"]
        ValidSignUpLastName = testdata["validSignUp"]["LastName"]
        ValidSignUpEmail = testdata["validSignUp"]["SignUpEmail"]
        ValidSignUpPassword = testdata["validSignUp"]["Password"]
