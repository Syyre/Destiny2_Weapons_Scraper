import sys
from bs4 import BeautifulSoup
import requests


url = "https://www.light.gg/"
headers = {
    'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
}
r = requests.get(url, headers=headers).text
soup = BeautifulSoup(r, 'lxml')

weapons = soup.find_all('div', class_="popular-item clearfix")

# for weapon in range(6):
#     name = weapon.find()

print(len(weapons))
