#!/usr/bin/env python3
# coding=utf-8
import base64
import ssl
import urllib
from urllib.request import urlopen
import bs4
from pykson import JsonObject, StringField
from pykson import Pykson

key_api = base64.b64encode(b'\xf7v\xf4'
                           b'\xce\xbc\xe7n\xbb\xdfg=').decode("utf-8")
url = "{}{}/api/v4/{}/v6?{}={}".format('https://', 'data.egov.kz', 'mugalimder_boiynsha_statistika', 'apiKey', key_api)

try:
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS)
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
except:
    print("Ошибка доступа к информации!")
