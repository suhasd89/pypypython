import requests
import reportlab.lib.rparsexml
import BeautifulSoup4


url = 'https://www.brainyquote.com/topics/motivational-quotes'

reponse = requests.get(url)
soup=BeautifulSoup(reponse.text,'lxml')
print(soup)