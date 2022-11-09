# Se usa para recorrer ciertas estructuras de datos

"""
for element in range(20):
  print(element)
  
for element in range(1, 21):
  print(element)
"""

my_list = [23, 45, 67, 89, 43]

for element in my_list:
    print(element)

my_tuple = ('César', 'Alejandro', 'Almeida')

for element in my_tuple:
    print(element)

product = {
    'name': 'Camisa',
    'price': 100,
    'stock': 89,
}

# for solo devuelve las llaves de un diccionario
for key in product:
    print(key, '=>', product[key])

# para obtener los keys y values con for desestructura el diccionario con el método .items()

for key, value in product.items():
    print(key, '=>', value)

# recorrer lista de diccionarios
people = [
    {
        'name': 'César',
        'age': 32,
    },
    {
        'name': 'Alejandro',
        'age': 23,
    },
    {
        'name': 'Almeida',
        'age': 18,
    },
]

for person in people:
    print(person)

for person in people:
    print('name =>', person['name'])
