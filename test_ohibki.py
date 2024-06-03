import requests
from bs4 import BeautifulSoup


def blocks_movie_page():
    link = 'https://kinokrad.film'

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:125.0) Gecko/20100101 Firefox/125.0'}

    response = requests.get(link, headers=headers, )  # Получение ответа от сервера
    print('статус запроса:', response.status_code)  # всегда проверяю статус запроса

    soup = BeautifulSoup(response.text, 'lxml')  # Создание объекта BeautifulSoup для парсинга HTML-кода

    block_janr = soup.find('div', class_="leftmenubox")

    left_menu = block_janr.find_all('ul')
    # left_menu_janr = left_menu[1].find_all('li').find('a').get('href')

    left_menu_janr = []
    for li in left_menu[1].find_all('li'):
        a = li.find('a').get('href')
        left_menu_janr.append(a)

    sleep(2)
    # print(left_menu_janr)

    for block_vovie in left_menu_janr:

        # for count in itertools.count(1):
        for count in range(1, 1000):

            # link = f"{i}page/{count}/"
            link = f"{block_vovie}page/{count}/"

            print(left_menu_janr, '\n\n\n')
            print(link)
            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:125.0) Gecko/20100101 Firefox/125.0'}

            response = requests.get(link, headers=headers, )  # Получение ответа от сервера
            print('статус запроса:', response.status_code)  # всегда проверяю статус запроса

            # with open('parsed_data.html', 'w', encoding='utf-8') as file:     # создаю фаил и записываю в него информацию
            #     file.write(response_text)

            soup = BeautifulSoup(response.text, 'lxml')  # Создание объекта BeautifulSoup для парсинга HTML-кода

            v_soup = soup.find_all('div', class_="shorbox")
            if v_soup == []:
                sleep(2)
                break

            for movie in v_soup:
                # print(movie)

                yield movie

            sleep(2)


# Импортируем переменную из модля  pars_filmi_reiting_2.py в которой 12  блоков карточек фильмов с одной страницы.

from time import sleep

movies_blocks_yes = []


def funk_iz_main():
    # Проверяем в цикле переменню  v_soup каждый блок. Если рейтинг больше 67 то добавляем в movies_blocks_yes  именно блоки карточек.
    for i in blocks_movie_page():

        proverka_raitinga = i.find('li', class_="current-rating").text

        if int(proverka_raitinga) > 70:
            movies_blocks_yes.append(i)

            # Вынимем в цикле всю нужную информацию с блоков карточек в переменной movies_blocks_yes
            for i in movies_blocks_yes:
                # название фильма
                name_film = i.find('a').text
                # print(name_film)

                # Рейтинг фильма
                reiting = 'Рейтинг фильма : ' + str(proverka_raitinga)

                # Следующие 5 строчек кода извлекаю жанр . он лежит в результате в span_yes
                for_janr = i.find('div', class_="item janr")
                spans = for_janr.find_all('span')
                span_twoo = spans[1]
                span_yes = span_twoo.text
                if '/ 2024 года' in span_yes:
                    span_yes = span_yes.replace('/ 2024 года', '')
                # sleep(2)
                # print(span_yes)

                # ссылка на фильм
                link_film = i.find('h2').find('a').get('href')
                print(name_film, reiting, span_yes, link_film)
                # yield {'name_film': name_film, 'reiting': reiting, 'span_yes': span_yes, 'link_film': link_film}


funk_iz_main()
