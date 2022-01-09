import requests
from bs4 import BeautifulSoup

url = 'https://kinoteatr.ru/raspisanie-kinoteatrov/kaluzhskij/'
user_agent = {
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0'
    }

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
data = ''
info = []
def callback():
    name_movie = soup.find_all(
    'div', class_='shedule_movie bordered gtm_movie')
    for n in name_movie:
        cl = n.find(
        'div', class_='shedule_movie_description')
        dl = n.find('div', class_='shedule_movie_sessions col col-md-8')
        foo = cl.text
        foo2 = dl.text
        return foo, foo2
    # for g in name_movie:
    #     bl = g.find('div', class_='shedule_movie_sessions col col-md-8')
    #     print(bl.text)
print(callback)