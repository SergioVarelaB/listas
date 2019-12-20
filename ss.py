import gspread 
from   oauth2client.service_account import ServiceAccountCredentials
import pprint
import array
import requests
from bs4 import BeautifulSoup
import smtplib
URL = "https://www.amazon.com.mx/gp/bestsellers/baby/ref=zg_bs_nav_0" ##Bebes
URL2 = "https://www.amazon.com.mx/gp/bestsellers/sports/ref=zg_bs_nav_0" ##Deportes
URL3 = "" ##Mascotas
URL4 = "" ##Mochilas

scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('/home/sergio/Documentos/python/prueba.json',scope)
client = gspread.authorize(creds)

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}
# headers=headers
page = requests.get(URL)
page2 = requests.get(URL2)

soup = BeautifulSoup(page.content,'html.parser')
soup2 = BeautifulSoup(page2.content,'html.parser')

l = soup.find_all(class_ = "p13n-sc-truncate p13n-sc-line-clamp-2")
lDeportes = soup.find_all(class_ = "p13n-sc-truncate p13n-sc-line-clamp-2")

sheet = client.open('prueba').sheet1
#ssheet2 = client.open('pruba')

j = 1
for i in l:
    sheet.update_cell(j,2,i.getText())
    j = j + 1
#    print(i.getText())

j = 1
for i in lDeportes:
    sheet.update_cell(j,4,i.getText())
    j = j + 1
#    print(i.getText())


