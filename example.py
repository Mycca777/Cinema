from cinemaparse import CinemaParser

msk_parser = CinemaParser('msk')
print(msk_parser.get_film_nearest_session('холодное сердце ii'))
