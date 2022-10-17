#!/usr/bin/env python3
# coding=utf-8

import requests

print(requests.get('http://api.coindesk.com/v1/bpi/currentprice.json').json()["chartName"], end=" стоит ")
print(requests.get('http://api.coindesk.com/v1/bpi/currentprice.json').json()["bpi"]["USD"]["rate"], end="$\n")
