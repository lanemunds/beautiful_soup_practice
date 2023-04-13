from bs4 import BeautifulSoup
import requests

response = requests.get('https://www.espn.com/')

linked = response.text
soup = BeautifulSoup(linked, 'html.parser')

article_name = soup.find(name='h1', class_='contentItem__title').text
article_sum = soup.find(name='p', class_='contentItem__subhead').text


def espn_top_story():
    print(article_name)
    print(article_sum)


espn_top_story()
