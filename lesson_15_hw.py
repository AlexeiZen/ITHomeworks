import json
with open('products.json', 'w',  encoding='utf-8') as f:
    product_list = {}
    product_list['product_name'] = []
    product_list['price'] = []
    while True:
        product_name = input('Enter product name:')
        if product_name == 'stop':
            break
        price = int(input('Enter product price:'))
        product_list['product_name'].append(product_name)
        product_list['price'].append(price)
    json.dump(product_list, f)

with open('products.json', encoding='utf-8') as f:
    prods = json.load(f)
    final_price = 0
    for item in prods['price']:
        final_price += item
print(f'Цена за все продукты равна {final_price}')
