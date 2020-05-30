import requests

message = "Hey Discord!"
WEBHOOKS = "716303854206976061/1T7VnMRVGsbZdmoRXt-ZpC6evInxRMaQgylA6XAUC57TpxkB5m2bhpObobA4z7HQwFoa"

#function
resp = requests.post("https://discordapp.com/api/webhooks/{WEBHOOKS}".format(WEBHOOKS=WEBHOOKS), json={"content": message})

print(resp)