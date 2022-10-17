#!/usr/bin/env python3
# coding=utf-8

import requests, bs4

b = bs4.BeautifulSoup(requests.get('https://sinoptik.ua/погода-павлодар').text, "html.parser")
print(b.select('.today-time')[0].getText(), end=" около ")
print(b.select('.today-temp')[0].getText())
