import requests
from bs4 import BeautifulSoup


SUGAR_PAGE = 'https://sbermegamarket.ru/catalog/sahar/'
KEYWORDS = ['сахар', 'песок']


res = requests.get(SUGAR_PAGE)
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text, 'html.parser')

sugar = None
for item in soup.findAll('div', {'class': 'item-block'}):
    item_name = item.find('a', {'class': 'ddl_product_link'})
    if item_name:
        if set(KEYWORDS).issubset(item_name.text.lower().split()):
            sugar = item
            break

if sugar is None:
    print('No sugar available :(')
else:
    price = float(sugar.find('div', {'class': 'item-price'}).text.replace(',', '.').split()[0])
    weight = float(sugar.find('p', {'class': 'item-details-item__value'}).text.replace(',', '.').split()[-1]) / 1000
    print(round(price / weight, 2))
