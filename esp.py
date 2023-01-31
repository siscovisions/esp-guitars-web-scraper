import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.americanmusical.com/ItemSearch--search-Esp-Guitars--srcin-1'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0',
    'Accept-Language': 'en-GB,en;q=0.5',
    'Referer': 'https://google.com',
    'DNT': '1',
}

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'html.parser')

elems = soup.find_all('div', class_='table2 itemContainer')

guitars = []

for elem in elems:
    title = elem.find('h3').text
    price = elem.find('span', class_='itemprice').text
    link = elem.find('a')['href']
    #print(title, price, link)

    items = {
        'title': title,
        'price': price,
        'link': link
    }

    guitars.append(items)

df = pd.DataFrame(guitars)
df.to_csv('esp_guitars.csv', index=False)
