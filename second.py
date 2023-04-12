from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com/news')

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, 'html.parser')


print(soup.title)


page_name = soup.find(name='span', class_='titleline')

page_name_a = page_name.find_all(name='a')
article_links = []
article_texts = []
for article_tag in page_name_a:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get('href')
    article_links.append(link)


article_upvote = soup.find_all(name='span', class_='score').get_text()


print(article_texts)
