import requests
from bs4 import BeautifulSoup

url = 'https://afisha.yandex.ru/moscow/cinema/places/kinoklub-eldar?source=search-page&place-schedule-preset=today'
user_agent = {
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0'
    }

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
data = ''
info = []
name_movie = soup.find_all('div', class_= 'schedule-event i-page__item i-page__item_loader_yes i-bem')
for n in enumerate(name_movie, start=1):
    bl = n.find('h3', class_= 'schedule-event__title')
    print(bl.text)

