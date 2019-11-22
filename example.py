from cinemaparse import CinemaParse
spb_parser = CinemaParser('spb')
#spb_parser.print_raw_content()
print(spb_parser.get_films_list())
msk_parser = CinemaParser('msk')
print(spb_parser.get_film_nearest_session('Джокер'))
#print(another_msk_parser = CinemaParser('msk'))
