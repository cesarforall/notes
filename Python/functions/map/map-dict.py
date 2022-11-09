items = [
    {
        'product': 'camisa',
        'price': 100
    },
    {
        'product': 'pantalones',
        'price': 300
    },
    {
        'product': 'pantalones cortos',
        'price': 50
    }
]

# map() recorre un iterable y lo modifica
# Las funciones lambda solo admiten una línea de código. Por tanto, si necesitamos una función más compleja se haría de la forma clásica
prices = list(map(lambda item: item['price'], items))
print(prices)


def add_taxes(item):
    item['taxes'] = item['price'] * .19
    return item


new_items = list(map(add_taxes,  items))
print(new_items)
print(items)
