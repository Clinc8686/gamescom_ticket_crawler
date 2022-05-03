import requests
from bs4 import BeautifulSoup
import pathlib
import os

path_to_directory = str(pathlib.Path().resolve())
path_to_file = str(path_to_directory)+"\\last_gamescom_request.txt"
dicord_url = ""  # Add here your Discord Webhook
gamescom_url = "https://www.gamescom.de/die-gamescom/tickets/tickets-kaufen/"

html = requests.get(gamescom_url).text
soup = BeautifulSoup(html, 'html.parser')


for new_request in soup.find_all('div', class_="ctadivider align-center colored corporateback white-color"):
     new_request = str(new_request).rstrip()
     os.open(path_to_file, os.O_RDWR |os.O_CREAT) #Create File if not exists
     file = open(path_to_file, "r+")    #Read file
     last_request = str(file.read()).rstrip()
     if last_request == None or len(last_request) <= 5:
          file.write(new_request)

     elif last_request != new_request:
          dis_param = {'content': '@everyone **Es gibt Gamescom Tickets!**'}
          requests.post(dicord_url, dis_param)  # Sende Discord Webhook