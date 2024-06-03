import requests
from bs4 import BeautifulSoup
from time import sleep


def skajat(url):
    resp = requests.get(url, stream=True)
    r = open('/Users/alexandr/Desktop/image/' + url.split('/')[-1], 'wb')
    for content in resp.iter_content(1048576):
        r.write(content)
    r.close()


links_card = []
rezult_all_card = []


def parser():
    for count in range(1):

        link = f"https://scrapingclub.com/exercise/list_basic/?page={count}"

        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:125.0) Gecko/20100101 Firefox/125.0'}

        response = requests.get(link, headers=headers, timeout=5, verify=False, data=None,
                                params=None, )  # Получение ответа от сервера
        print('статус запроса:', response.status_code)  # всегда проверяю статус запроса
        # response_text = response.text  # просто перевел респонс в стр

        # with open('parsed_data.html', 'w', encoding='utf-8') as file:     # создаю фаил и записываю в него информацию
        #     file.write(response_text)

        soup = BeautifulSoup(response.text, 'lxml')  # Создание объекта BeautifulSoup для парсинга HTML-кода

        v_soup = soup.find_all('div', class_="w-full rounded border")

        for i in v_soup:
            link_card = ('https://scrapingclub.com' + i.find('a').get('href'))
            #             print (link_card)

            yield link_card


#       берем по одно ссылке с   links_card и вынимаем ссылку  ,делаем суп, уточненный суп по общему блоку карточки.
def funk_iz_main():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:125.0) Gecko/20100101 Firefox/125.0'
    }

    for i in parser():
        sleep(1)

        response_2 = requests.get(i, headers=headers)
        soup_2 = BeautifulSoup(response_2.text, 'lxml')
        v_soup_2 = soup_2.find('div', class_="px-4 mb-6 w-full sm:w-2/3 md:w-3/4 lg:w-8/12")

        img = 'https://scrapingclub.com' + v_soup_2.find('img', class_="card-img-top").get('src')
        skajat(img)
        tovar_name = v_soup_2.find('h3', class_="card-title").text
        price = v_soup_2.find('h4', class_="my-4 card-price").text
        opisanie = v_soup_2.find('p', class_="card-description").text

        yield img, tovar_name, price, opisanie

# funk_iz_main()
# print(*rezult_all_card)
