from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com/news')

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, 'html.parser')


print(soup.title)


page_name = soup.find(name='span', class_='titleline')

page_name_a = page_name.find_all(name='a')
for article_tag in page_name_a:


article_link = page_name_a.get('href')

article_upvote = soup.find_all(name='span', class_='score').get_text()
