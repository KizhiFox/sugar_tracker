# 2022, KizhiFox (https://github.com/KizhiFox/)
# This program is distributed under the GNU General Public License.
import requests
import json
from sys import argv
from bs4 import BeautifulSoup


SUGAR_PAGE = 'https://sbermegamarket.ru/catalog/sahar/'
KEYWORDS = ['сахар', 'песок']
EXCLUDE = ['тростниковый']

JSON_OUTPUT = any(arg in ['-j', '--json'] for arg in argv)


res = requests.get(SUGAR_PAGE)
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text, 'html.parser')

sugar = []
for item in soup.findAll('div', {'class': 'item-block'}):
    item_name = item.find('a', {'class': 'ddl_product_link'})
    if item_name:
        item_name = item_name.text.lower().split()
        if set(KEYWORDS).issubset(item_name) and all(exc not in item_name for exc in EXCLUDE):
            sugar.append(item)

if len(sugar) > 0:
    sugar_prices = []
    sugar_names = []
    for s in sugar:
        price = float(s.find('div', {'class': 'item-price'}).text.replace(',', '.').split()[0])
        weight = float(s.find('p', {'class': 'item-details-item__value'}).text.replace(',', '.').split()[-1]) / 1000
        sugar_prices.append(round(price / weight, 2))
        sugar_names.append(s.find('a', {'class': 'ddl_product_link'}).text)

    min_price = min(sugar_prices)
    min_name = sugar_names[sugar_prices.index(min_price)]

    max_price = max(sugar_prices)
    max_name = sugar_names[sugar_prices.index(max_price)]

    mean_price = round(sum(sugar_prices) / len(sugar_prices), 2)

    if JSON_OUTPUT:
        print(json.dumps({'mean_price': mean_price,
                          'min_price': min_price,
                          'min_name': min_name,
                          'max_price': max_price,
                          'max_name': max_name,
                          'source': SUGAR_PAGE},
                         ensure_ascii=False, indent=2))

    else:
        print(f'Prices per 1 kg according to {SUGAR_PAGE} data:\n'
              f'mean: {mean_price} ₽\n'
              f'min: {min_price} ₽ ({min_name})\n'
              f'max: {max_price} ₽ ({max_name})')

else:
    if JSON_OUTPUT:
        print('{"exception": "No sugar available :("}')
    else:
        print('No sugar available :(')
