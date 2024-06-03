import requests
from bs4 import BeautifulSoup
from time import sleep

for count in range(1):

    link = f"https://kinokrad.film/filmy-2024/page/{count}/"

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:125.0) Gecko/20100101 Firefox/125.0'}

    response = requests.get(link, headers=headers)  # Получение ответа от сервера
    print('статус запроса:', response.status_code)  # всегда проверяю статус запроса

    # with open('parsed_data.html', 'w', encoding='utf-8') as file:     # создаю фаил и записываю в него информацию
    #     file.write(response_text)

    soup = BeautifulSoup(response.text, 'lxml')  # Создание объекта BeautifulSoup для парсинга HTML-кода

    v_soup = soup.find_all('div', class_="shorbox")

    # strip_reiting= v_soup.find('li', class_="current-rating").text
    # print(strip_reiting)

    a = []
    for i in v_soup:
        proverka_raitinga = i.find('li', class_="current-rating").text

        a.append(proverka_raitinga)

    print(a)

# rating_width = rating_element['style'].split(':')[1].strip().rstrip('%')
#        rating = int(rating_width)


# rating_width = rating_element['style'].split(':')[1].strip().rstrip('%')


# <div class="shorbox" id="storyID-472412">

# <li class="current-rating" style="width:83%;">83</li>
