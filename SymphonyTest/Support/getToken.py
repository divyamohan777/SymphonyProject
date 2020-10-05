from twilio.rest import Client


def getSMSverificationcode():
    account_sid = "ACb4542fb4dba7479c735ce529076e65e5"
    auth_token = "c4d4880c48b020ae931e6aee54a93734"
    client = Client(account_sid, auth_token)
    received = client.messages.list(to='+12014827936', limit=1)
    for message in received:
        token = message.body.split(" ")
    return token[0]
