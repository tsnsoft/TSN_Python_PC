#!/usr/bin/env python3
# coding=utf-8

import ssl
import urllib
from urllib.request import urlopen
import bs4
from pykson import JsonObject, StringField
from pykson import Pykson
import os

api_key = os.getenv("CMC_API_KEY")

if not api_key:
    print("Ошибка: Переменная окружения CMC_API_KEY не найдена!")
    exit(1)

url = "{}{}/api/v4/{}/v6?{}={}".format('https://', 'data.egov.kz', 'mugalimder_boiynsha_statistika', 'apiKey', api_key)

try:
    ssl_context = ssl.create_default_context()
    html = urllib.request.urlopen(url, context=ssl_context).read()
    html_parse = bs4.BeautifulSoup(html, "html.parser").text

    class TeachersSchool(JsonObject):
        region = StringField()
        id = StringField()
        all_teachers = StringField()
        region_kz = StringField()
        teachers_need = StringField()

    teachers_list = Pykson().from_json(html_parse, TeachersSchool)
    for m in teachers_list:
        print(m.region, ": учителей " + m.all_teachers, ", требуется " + m.teachers_need)
except Exception as e:
    print("Ошибка доступа к информации:", e)
