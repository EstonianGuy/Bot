import requests
from bs4 import BeautifulSoup

url = 'https://kinoklub-eldar.ru/kinoafisha'
user_agent = {
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0'
    }

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
name_movie = soup.find_all('p', class_= 'kb_widget_theatre_film_info_name')
print(type(name_movie))
for i in range(0, len(name_movie)):
    # print(name_movie[i].text)
    print(type(name_movie[i]))