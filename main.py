from bs4 import BeautifulSoup

with open('website.html') as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')
heading = soup.find(name='h1', id='name')
print(heading)

section_heading = soup.find(name='h3', class_='heading')
print(section_heading)

company_url = soup.select_one(selector='p a')
print(company_url)

headings = soup.select('.heading')
print(headings)
