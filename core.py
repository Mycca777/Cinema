import requests as req
from bs4 import BeautifulSoup
class CinemaParser:
    def __init__(self, city):
        self.city = city
    def extract_raw_content(self, content):
        content = self.content
        resp = req.get("https://spb.subscity.ru")
        content = BeautifulSoup(resp.text, 'lxml')
    def print_raw_content(self, content):
        return (extract_raw_content(self, content).prettify())
    def  get_films_list():
        soup = self.extract_raw_content()
        soup.find("span", id="mylist", )


spb_parser = CinemaParser('spb')
msk_parser = CinemaParser()
another_msk_parser = CinemaParser('msk')
