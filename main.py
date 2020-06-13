#modules
import requests
import sys
import lxml
from bs4 import BeautifulSoup

#DATA
trx40aorusextreme = "https://www.microcenter.com/product/617303/gigabyte-trx40-aorus-xtreme-amd-strx4-atx-motherboard"
trx40asuszenithAlpha = "https://www.microcenter.com/product/618565/asus-trx40-rog-zenith-ii-extreme-alpha-amd-strx4-eatx-motherboard"

####################        REQ     ####################
getaextreme = requests.get(trx40aorusextreme)
src = getaextreme.content

sp = BeautifulSoup(src, 'lxml')

#OrganizeData
product = sp.find('span', class_='ProductLink_617303').text
print(product)




print("Hey")



#Connect To WEBHOOK
webhook = "716540771469230126/tsrjpCskRAsy7NGz8QE4amrknf3v_jbey3UYkBCuZRMv6XWkBW-Vh4McKRJsNCBrIBF-"

consoleout = str(sys.stdout)

#START
resp = requests.post("https://discordapp.com/api/webhooks/{}".format(webhook),json={"content": consoleout})
print(resp)