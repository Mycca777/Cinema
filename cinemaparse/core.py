import requests as req
from bs4 import BeautifulSoup
class CinemaParser:
    def __init__(self, city='msk'):
        self.city = city
    def extract_raw_content(self):
        resp = req.get("https://spb.subscity.ru")
        self.content = BeautifulSoup(resp.text, 'html.parser')

    def print_raw_content(self):
        self.extract_raw_content()
        print(self.content.prettify())
    def  get_films_list(self):
        self.extract_raw_content()
        films = self.content.find_all("div", {"class" : "movie-plate"})
        titles = []
        for film in films:
            titles.append(film["attr-title"])
        return titles
    def get_film_nearest_session(self, film_name):
        if not self.content:
            self.extract_raw_content()
        url = "https://spb.subscity.ru"
        self.extract_raw_content()
        films = self.content.find_all("div", {"class" : "movie-plate"})
        for film in films:
            
            if film["attr-title"] == film_name:
                title = film.find("div", {"class" : "movie-title"})
                print(title)
                a = title.find("a", {"class" : "underdashed"})
                print(a.prettify())
                href = a["href"]
                print(url+href)
        return url


spb_parser = CinemaParser('spb')
#spb_parser.print_raw_content()
print(spb_parser.get_films_list())
msk_parser = CinemaParser('msk')
print(spb_parser.get_film_nearest_session('Джокер'))
#print(another_msk_parser = CinemaParser('msk'))
