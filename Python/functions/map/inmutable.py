# Los objetos tienen una referencia en memoria. Si accedemos al diccionario con map y hacemos una modificación se hará la modificación en la referencia
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

# Para evitar la modificación de la referencia en memoria crearemos un nuevo diccionario con la función copy() en la higher order function map()
prices = list(map(lambda item: item['price'], items))
print(prices)


def add_taxes(item):
    new_item = item.copy()
    new_item['taxes'] = new_item['price'] * .19
    return new_item


new_items = list(map(add_taxes, items))
print('new items', new_items)
print('items', items)
