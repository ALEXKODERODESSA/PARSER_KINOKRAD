from POST_ZAPROS import result

import requests
from bs4 import BeautifulSoup
from time import sleep

result

soup = BeautifulSoup(result.text, 'lxml')  # Создание объекта BeautifulSoup для парсинга HTML-кода

print(soup)
