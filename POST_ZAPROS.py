from requests import session
from time import sleep
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:125.0) Gecko/20100101 Firefox/125.0'
}

work = session()

work.get('https://quotes.toscrape.com/', headers=headers)
sleep(2)
response = work.get('https://quotes.toscrape.com/login', headers=headers)

sup = BeautifulSoup(response.text, 'lxml')

token = sup.find('form').find('input').get('value')

data = {'csrf_token': token, 'username': 'admin', 'password': 'admin'}
sleep(3)
result = work.post('https://quotes.toscrape.com/login', headers=headers, data=data)
