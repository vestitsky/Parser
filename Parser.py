import pandas as pd
import requests
from bs4 import BeautifulSoup
# Чтобы убрать пробелы со строк используют split() strip() или replace()
# df['price'] = [prices], data.append({'title': title})  - добавить новую колонну
# export_excel = df.to_excel('export_dataframe.xlsx', index=None, header=True) - экпорт пандас
url = 'https://www.avito.ru/moskva'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
title_elem_data = []
title_elem = soup.find_all('div', class_='styles-root-2nfT7')
for item in title_elem:
    title_elem_data.append(item.text)
price_elem_data = []
price_elem = soup.find_all('div', class_='styles-price-2lpKU')
for item in price_elem:
    price_elem_data.append(item.text)
final_array = []
for title, price in zip(title_elem_data, price_elem_data):
    final_array.append({'Заголовок': title, 'Цена': price})
df = pd.DataFrame(final_array)
print(df)