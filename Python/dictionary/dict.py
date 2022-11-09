# Son estructuras de datos que funcionan con key y values

my_dict = {}
print(type(my_dict))

my_dict = {
  'name': 'César',
  'last_name': 'Almeida',
  'age': '32',
}
print(my_dict)

# La función len() devuelve el número de elementos que contiene el diccionario

print(len(my_dict))

# Para acceder a los valores se escribe el numbre de la key dentro de []
# Si no existe el valor se produce un error
print(my_dict['age'])
print(my_dict['last_name'])

# Para evitar un error por valor inexistente se puede acceder mediante el método .get() 
print(my_dict.get('no_key'))

# También se puede evaluar si existe la llave con in
if 'name' in my_dict:
  print(my_dict['name'])
  
if not 'status' in my_dict:
  print(my_dict.get('status'))

person = {
  'name': 'César',
  'last_name': 'Almeida',
  'langs': ['JavaScript', 'Python'],
  'age': 99,
}
print(person)

# Modificar valores
person['name'] = 'Alejandro'
person['age'] -= 50
person['langs'].append('Rust')
print(person)

# Eliminar atributos
del person['last_name']
print(person)
person.pop('age')
print(person)

# El método .items() devuelve una lista de tuplas con los atributos del diccionario
print('items')
print(person.items())

# El método .keys() devuelve un lista con los keys del diccionario
print('keys')
print(person.keys())

# El método .values() devuelve un lista con los values del diccionario
print('values')
print(person.values())