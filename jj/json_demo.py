#!/usr/bin/env python3
# coding=utf-8

import requests

# Новый URL: CoinGecko API (бесплатный, без ключей)
url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'

try:
    response = requests.get(url, timeout=10)  # Устанавливаем таймаут в 10 секунд
    response.raise_for_status()  # Проверяет HTTP-ошибки (4xx/5xx)
    data = response.json()

    # Извлекаем цену (структура: {"bitcoin": {"usd": 123456.78}})
    price = data["bitcoin"]["usd"]

    print("Bitcoin стоит", price, "$\n")

except requests.exceptions.ConnectionError:
    print("❌ Ошибка: Нет интернета или сервер недоступен. Проверь DNS (ipconfig /flushdns).")
except requests.exceptions.Timeout:
    print("❌ Ошибка: Таймаут — сервер не отвечает вовремя.")
except requests.exceptions.RequestException as e:
    print(f"❌ Ошибка запроса: {e}")
except KeyError:
    print("❌ Ошибка: Неожиданный формат JSON от API.")
except Exception as e:
    print(f"❌ Неизвестная ошибка: {e}")