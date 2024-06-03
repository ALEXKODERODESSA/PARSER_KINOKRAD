from requests import session
from time import sleep
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:125.0) Gecko/20100101 Firefox/125.0'
}

work = session()

# work.get('https://forumodua.com/', headers=headers)
# sleep(2)
response = work.get('https://forumodua.com/', headers=headers)

sup = BeautifulSoup(response.text, 'lxml')

token = sup.find('form').find('input').get()

data = {'vb_login_username': 'saskin', 'vb_login_password': '987654321'}
sleep(3)
result = work.post('https://quotes.toscrape.com/login', headers=headers, data=data, allow_redirects=True)

result_sup = BeautifulSoup(result.text, 'lxml')

# Определи путь к файлу на рабочем столе
desktop_path = '/Users/alexandr/Desktop/'
file_path = desktop_path + 'result_sup.html'

# Запись содержимого BeautifulSoup объекта в файл
with open(file_path, 'w', encoding='utf-8') as file:
    file.write(result_sup.prettify())

# 'vb_login_password_hint': '(unable to decode value)','cookieuser': '1', 's': '', 'securitytoken': token, 'do': 'login', 'vb_login_md5password': '202cb962ac59075b964b07152d234b70', 'vb_login_md5password_utf': '202cb962ac59075b964b07152d234b70'

input
type = "hidden"
name = "securitytoken"
value = "guest"
