# Пример доступа к сайту с авторизацией по логину и паролю

import os
import requests
from bs4 import BeautifulSoup

# pip install requests bs4

# Указываем адрес страницы для парсинга
url = 'https://tou.edu.kz/armp/?lang=rus&menu=calendar&mod=shedule_prep_kaf'

# Указываем данные для авторизации
payload = {'user': 'ТСН',
           'password': 'Tsn',
           'rememberMe': 'True'
           }

# Создаем сессию
with requests.Session() as s:
    p = s.post(url, data=payload)  # Авторизуемся
    r = s.get(url)  # Получаем страницу
    b = BeautifulSoup(r.text, "html.parser")  # Создаем объект BeautifulSoup
    p = b.select('.schedule-table')  # Ищем таблицу с расписанием
    if p != []:  # Если расписание найдено
        f = open('data.html', 'w', encoding='utf-8')  # Создаем файл для записи
        f.write(p[0].prettify())  # Записываем в файл расписание
        f.close()  # Закрываем файл
        os.startfile(os.path.abspath(f.name))  # Открываем файл в браузере

