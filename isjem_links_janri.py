import requests
from bs4 import BeautifulSoup
from time import sleep

link = 'https://kinokrad.film/'

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
