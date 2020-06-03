#modules
import requests
import sys

#data
webhook = "716540771469230126/tsrjpCskRAsy7NGz8QE4amrknf3v_jbey3UYkBCuZRMv6XWkBW-Vh4McKRJsNCBrIBF-"

consoleout = str(sys.stdout)



#START
resp = requests.post("https://discordapp.com/api/webhooks/{}".format(webhook),json={"content": consoleout})


print(resp)