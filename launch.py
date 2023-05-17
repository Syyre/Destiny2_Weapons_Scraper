import sys
from bs4 import BeautifulSoup
import requests


url = "https://www.light.gg/"

r = requests.get(url).text
soup = BeautifulSoup(r, 'lxml')
#List of all hot/popular/rising weapons
weapons = soup.find_all('div', class_="popular-item clearfix")

# Below prints the weapons under their respecitve catagory
print("Hot Items:")
for i in range(6):
    print(i+1, end ='')
    print(". ", end='')
    name = weapons[i].find('div', class_="pop-item-name").a.get_text(strip=True)
    print(name)

print("\nPopular Items:")
for i in range(6, 12):
    print(i+1, end ='')
    print(". ", end='')
    name = weapons[i].find('div', class_="pop-item-name").a.get_text(strip=True)
    print(name)

print("\nRising Items:")
for i in range(12, 18):
    print(i+1, end ='')
    print(". ", end='')
    name = weapons[i].find('div', class_="pop-item-name").a.get_text(strip=True)
    print(name)
