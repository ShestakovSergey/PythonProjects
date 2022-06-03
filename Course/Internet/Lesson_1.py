from bs4 import BeautifulSoup as bs
import requests

url = 'https://news.google.com/topstories?hl=ru&gl=RU&ceid=RU:ru'
r = requests.get(url)
r.encoding = 'utf-8"'

b = bs(r.text, "html.parser")
aspan = b.find_all('a', class_='DY5T1d RZIKme')

my_news = []

for n in aspan:
    my_news.append(n.getText())

for n in my_news:
    print(n)
