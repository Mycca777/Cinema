from cinemaparse import CinemaParser
spb_parser = CinemaParser('spb')
print(spb_parser.get_films_list())
msk_parser = CinemaParser('msk')
print(spb_parser.get_film_nearest_session('Джокер'))
