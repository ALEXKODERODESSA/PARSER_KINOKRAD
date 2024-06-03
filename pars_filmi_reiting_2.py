
import requests
from bs4 import BeautifulSoup
from time import sleep
import itertools


# left_menu_janr = ['https://kinokrad.film/anime2/', 'https://kinokrad.film/biografiya3/',
#                   'https://kinokrad.film/boevik-10/', 'https://kinokrad.film/vestern-5/',
#                   'https://kinokrad.film/4-voennyy/', 'https://kinokrad.film/3-detektiv/',
#                   'https://kinokrad.film/dokumentalny-3/', 'https://kinokrad.film/drama-4/',
#                   'https://kinokrad.film/istoriya-4/', 'https://kinokrad.film/4-komediya/',
#                   'https://kinokrad.film/kriminal-6/', 'https://kinokrad.film/melodrama6/',
#                   'https://kinokrad.film/1-mistika/', 'https://kinokrad.film/2-mult/',
#                   'https://kinokrad.film/myuzikl-online2/', 'https://kinokrad.film/4-priklyucheniya/',
#                   'https://kinokrad.film/3-semeynyy/', 'https://kinokrad.film/2-sport/',
#                   'https://kinokrad.film/tvperedachi-online2/', 'https://kinokrad.film/2-trillers/',
#                   'https://kinokrad.film/3-uzhasy/', 'https://kinokrad.film/3-fantastika/',
#                   'https://kinokrad.film/4-fentezi/']


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

    # for block_vovie in left_menu_janr:
    aaa = ['https://kinokrad.film/anime2/']
    for block_vovie in aaa:

        # for count in itertools.count(1):
        for count in range(1, 5):

            link = f"{block_vovie}page/{count}/"
            # link = 'https://kinokrad.film/anime2/page/2/'

            # print(left_menu_janr,'\n\n\n')
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

        break

        # Ниже код чисто чтобы проверить что код на этой страницы работает. Ответ кода здесь это - список цифр рейтинга
        # всех двенадцати фильмов с одной спаршеной страницы
        # a = []
        # for i in v_soup:
        #     proverka_raitinga = i.find('li', class_="current-rating").text
        #
        #     a.append(proverka_raitinga)

        # print(a)

