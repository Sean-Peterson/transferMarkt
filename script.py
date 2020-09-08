import urllib
from bs4 import BeautifulSoup
import xlwt
from xlwt import Workbook
import time

allBrandsURL = "https://www.gsmarena.com/makers.php3"
page=urllib.urlopen(allBrandsURL)
soup=BeautifulSoup(page, 'lxml')
allPhoneBrands=soup.find_all('td')
# this is an array that has all of the brands included in the GSMarena DB. This array will be used to append to gsmarena.com/
allBrandsURLArray = []
 
