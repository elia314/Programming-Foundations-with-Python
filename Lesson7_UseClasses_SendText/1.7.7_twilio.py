from twilio.rest import TwilioRestClient

# Your Account SID from twilio.com/console
account_sid = "ACc87b93efb3f4a51b5b232420efffe1a7"
# Your Auth Token from twilio.com/console
auth_token  = "7d547de5733595e4b6dc7a8a15066b69"

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(
    to="+17174222066", 
    from_="+17179857050",
    body="My name is Mike Jones")

print(message.sid)
