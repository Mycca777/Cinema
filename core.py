import requests
from bs4 import BeautifulSoup
class CinemaParser:
    def __init__(self, city):
        self.city = city




spb_parser = CinemaParser('spb')
msk_parser = CinemaParser()
another_msk_parser = CinemaParser('msk')