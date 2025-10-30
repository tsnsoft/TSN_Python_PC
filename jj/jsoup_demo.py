import requests
from bs4 import BeautifulSoup

url = "https://sinoptik.ua/ru/pohoda/pavlodar"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Текущая температура
temp = soup.select_one(".R1ENpvZz").get_text(strip=True)

# Описание погоды (оттуда берём "утром", "днём" и т.п.)
desc = soup.select_one(".GVzzzKDV").get_text(strip=True)

print(f"{desc} Погода сейчас {temp}")