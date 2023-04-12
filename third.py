from bs4 import BeautifulSoup
import requests

response = requests.get('https://cougarboard.com')

cougar_site = response.text
soup = BeautifulSoup(cougar_site, 'html.parser')

top_ten = soup.find(name='div', id='home-board')
topTen = top_ten.find(name='cb-tab')
list_box = topTen.find(name='div', class_='list_box')

top = top_ten.find(name='h4')
list_text = list_box.text
list_link = list_box.get('href')
head = soup.select_one(selector='div h4')
print(list_text)
print(list_link)
