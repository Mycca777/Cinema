import requests as req
from bs4 import BeautifulSoup
from datetime import datetime
class CinemaParser:
    def __init__(self, city='msk'):
        self.city = city
        if self.city == 'msk':
            self.url = 'https://msk.subscity.ru/'
        else:
            self.url = 'https://spb.subscity.ru/'
        self.content = self.extract_raw_content(self.url)
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
        film_name = film_name.strip(' ')
        film_name = film_name.lower()
        if not self.content:
            self.extract_raw_content(self.url)
        FILMS = self.get_films_list()
        for i in range(len(FILMS)):
            if film_name == FILMS[i].lower():
                continue
        self.extract_raw_content(self.url)
        films = self.content.find_all("div", {"class" : "movie-plate"})
        for film in films:
          if str(film["attr-title"]).lower() == film_name.lower():
            a = film.find("a", {"class" : "underdashed"})
            href = a["href"]
            href_for_films = self.url + "/" + href
            self.extract_raw_content(href_for_films)
            span = film.find("span", {"class": "label label-bg label-default normal-font"})
            times = self.content.find_all("table", {"class" : "table table-bordered table-condensed table-curved table-striped table-no-inside-borders"})
            for time in times:
                trs = self.content.find_all("tr", {"class": "row-entity"})
                thing_for_day1 = film.find_all('div', {'class': 'movie-plate-table'})
                thing_for_day2 = thing_for_day1[0].find_all('div', {'class': 'movie-plate-row'})
                day = thing_for_day2[1].find_all('span', {'class': 'label label-bg label-default normal-font'})
                day = day[0].text
                if day != ' сегодня':
                    korteh = 'None', 'None'
                elif day == ' сегодня':
                        typok = times[0]
                        times_for_result = typok.find_all('tr', {'class': 'row-entity'})
                        result = []
                        for i in range(len(times_for_result)):
                            n = times_for_result[i].find_all('td', {'class': 'col-sm-8 col-xs-1'})
                            resultat = n[0].find_all('td')
                            res = resultat[0]['attr-time']
                            result.append(int(res))
                        closest_time_index = result.index(min(result))
                        route = times_for_result[closest_time_index].find_all('td', {'class': 'col-sm-8 col-xs-1'})
                        normal_time = route[0].find_all('a')[0]
                        thing_for_cinema = times_for_result[closest_time_index].find_all('td', {'class': 'col-sm-4 col-xs-11'})
                        cinema = thing_for_cinema[0].find_all('a')[0]
                        korteh = cinema.text, normal_time.text

                        return korteh
    def get_soonest_session(self, film_name):
        respect
 
spb_parser = CinemaParser('spb')
spb_parser.print_raw_content()
print(spb_parser.get_films_list())
msk_parser = CinemaParser('msk')
print(spb_parser.get_film_nearest_session('Прекрасная эпоха    '))
