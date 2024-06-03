# Импортируем переменную из модля  pars_filmi_reiting_2.py в которой 12  блоков карточек фильмов с одной страницы.
from pars_filmi_reiting_2 import blocks_movie_page


# from pars_filmi_reiting_2 import block_vovie


def funk_iz_main():
    # Проверяем в цикле переменню  v_soup каждый блок. Если рейтинг больше 67 то добавляем в movies_blocks_yes  именно блоки карточек.
    for film in blocks_movie_page():

        proverka_raitinga = film.find('li', class_="current-rating").text

        if int(proverka_raitinga) > 79:

            # Вынимем в цикле всю нужную информацию с блоков карточек в переменной movies_blocks_yes
            # название фильма
            name_film = film.find('a').text
            otsekaem_dubliaji_movie = set()
            if name_film in otsekaem_dubliaji_movie:
                continue

            otsekaem_dubliaji_movie.add(name_film)

            # Рейтинг фильма
            reiting = 'Рейтинг фильма : ' + str(proverka_raitinga)

            # Следующие 5 строчек кода извлекаю жанр . он лежит в результате в span_yes
            for_janr = film.find('div', class_="item janr")
            spans = for_janr.find_all('span')
            span_twoo = spans[1]
            span_yes = span_twoo.text
            if '/ 2024 года' in span_yes:
                span_yes = span_yes.replace('/ 2024 года', '')
            # sleep(2)
            # print(span_yes)

            # ссылка на фильм
            link_film = film.find('h2').find('a').get('href')
            # print(name_film,reiting, span_yes,link_film)

            # block_vovie.split('/')[-2].replace('/', '')

            yield {'name_film': name_film, 'reiting': reiting, 'span_yes': span_yes, 'link_film': link_film}


funk_iz_main()

# print(for_janr)
# janr = for_janr.find('span').text
# print(janr)

# janr = for_janr.text


# j.movies_blocks_yes[0].find('h2').find('a').get('href')   # ссылка на фильм
# j.movies_blocks_yes[0].find('a').text    название фильма

# for_janr = movies_blocks_yes[0].find('div', class_="item janr")     # жанр
# spans = for_janr.find_all('span')
# span_twoo = spans[1]
# span_yes = span_twoo.text


# print(movies_blocks_yes)

# print(type(a))
