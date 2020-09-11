import bs4 as bs
import urllib.request
import lxml
import xlwt
from xlwt import Workbook
import time
import requests

baseUrl = 'https://www.transfermarkt.com/'
headers = {'User-Agent': 'Mozilla/5.0'}
playersMostValuable = 'spieler-statistik/wertvollstespieler/marktwertetop'


result = requests.get(baseUrl+playersMostValuable,headers=headers)
c = result.content
soup = bs.BeautifulSoup(c,'lxml')
playerNames = soup.findAll("a",{"class":"spielprofil_tooltip"})

allPlayerNames = []

for name in playerNames:
    currentName = str(name)
    currentName1 = currentName.split('title="')
    currentName2 = currentName1[1].split('"')
    allPlayerNames.append(currentName2[0])
# hotLink = soup.findAll("td",{"class":"hauptlink"})
#
# allLinks = []
#
# for link in hotLink:
#     currentLink = str(link)
#     allLinks.append(currentLink+"AAAAAAAAAAAAAAAAAAAAAAAAAAAAA")


print(allPlayerNames)
