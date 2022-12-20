import requests
from bs4 import BeautifulSoup


url_weather_mail_ru = 'https://pogoda.mail.ru/prognoz/moskva/'

req = requests.get(url_weather_mail_ru)
src = req.text
soup = BeautifulSoup(src, 'html.parser')
temp_at_the_moment = soup.find('div', class_='information__content__temperature').text
print(temp_at_the_moment)

