import yaml


class getTestData():
    with open("/Users/divyamohan/PycharmProjects/pythonProject2/SymphonyTest/Support/TestData.yaml", "r") as ymlfile:
        testdata = yaml.safe_load(ymlfile)
        ValidUserName = testdata["ValidLogin"]["ValidUserName"]
        ValidPassword = testdata["ValidLogin"]["ValidPassword"]
        InvalidUserName = testdata["InvalidLogin"]["InvalidUserName"]
        InvalidPassword = testdata["InvalidLogin"]["InvalidPassword"]
        FirstName= testdata["FirstName"]
        LastName = testdata["LastName"]
        SignUpexisitingEmail = testdata["SignUpexisitingEmail"]
        Password = testdata["Password"]
