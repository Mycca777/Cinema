import requests as req
from bs4 import BeautifulSoup
from datetime import datetime
class CinemaParser:
    def __init__(self, city='msk'):
        self.city = city
        self.url = 'http://' + self.city + '.subscity.ru'
        self.content = None
    def extract_raw_content(self, url):
        resp = req.get(url)
        self.content = BeautifulSoup(resp.text, 'html.parser')

    def print_raw_content(self):
        self.extract_raw_content(self.url)
        print(self.content.prettify())
    def get_films_list(self):
        self.extract_raw_content(self.url)
        films = self.content.find_all("div", {"class" : "movie-plate"})
        titles = []
        for film in films:
            titles.append(film["attr-title"])
        return titles
    def get_film_nearest_session(self, film_name):
        if not self.content:
            self.extract_raw_content(self.url)
        self.extract_raw_content(self.url)
        films = self.content.find_all("div", {"class" : "movie-plate"})
        spans = self.content.find_all("span", {"class" : "label label-bg label-default normal-font"})
        print(spans)
        print(len(films))
        for film in films:
            if film["attr-title"] != film_name:
                continue
            a = film.find("a", {"class" : "underdashed"})
            print(a)                 
            href = a["href"]
            href_for_films = self.url + "/" + href
            print(href_for_films)
        result = []
        self.extract_raw_content(href_for_films)
        times = self.content.find("table", {"class" : "table table-bordered table-condensed table-curved table-striped table-no-inside-borders"})
        print(times)
        for time in times:
            print(time)
            td = time.find("td", {"class" : "text-center cell-screenings"})
            print(td)
            res = int(td["attr-time"])
            result.append(res)
        resultat = min(result)
        #if resultat // 3600 // 24 // 365
        return resultat//3600//24//365
spb_parser = CinemaParser('spb')
#spb_parser.print_raw_content()
print(spb_parser.get_films_list())
# msk_parser = CinemaParser('msk')
print(spb_parser.get_film_nearest_session('Ford против Ferrari'))
#print(another_msk_parser = CinemaParser('msk'))
