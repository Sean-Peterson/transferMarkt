import bs4 as bs
import urllib.request
import lxml
import xlwt
from xlwt import Workbook
import time
import requests
# baseUrl = "https://www.transfermarkt.com/"
# page=ur.urlopen(baseUrl)
# soup=BeautifulSoup(page, 'lxml')
# transferMarktTest=soup.find_all('td')
# # this is an array that has all of the brands included in the GSMarena DB. This array will be used to append to gsmarena.com/
# baseUrlArray_a_tags = []
# url = 'https://www.transfermarkt.com/aktuell/newsarchiv'
# headers = {'User-Agent': 'Mozilla/5.0'}
# content = urllib.request.urlopen(url).read()
# soup = bs.BeautifulSoup(content,'lxml')
# test = soup.title
# print(test)
url = 'https://www.transfermarkt.com/aktuell/newsarchiv'
headers = {'User-Agent': 'Mozilla/5.0'}
result = requests.get(url,headers=headers)
c = result.content
soup = bs.BeautifulSoup(c,'lxml')
print(soup.title)









# practice stuff to test if it was actually working. Found out I needed to download lxml
# import bs4 as bs
# import urllib.request
#
# source = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
# soup = bs.BeautifulSoup(source,'lxml')
# print(soup.title)
