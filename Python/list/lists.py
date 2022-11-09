numbers = [1, 2, 3, 4]
print(numbers)
print(type(numbers))

tasks = ['wash the dishes', 'play videogames']
print(tasks)

types = [1, True, 'hola']
print(types)

print(numbers[0])
print(tasks[0])
text = 'Hola'
# text[0] = 'W'

# Asignar nuevos valores a los elementos
tasks[0] = 'Watch Platzi courses'
print(tasks)

tasks[0] = 'Do the dishes'
print(tasks)

# Slicing
print(numbers[:3])

# in devuelve un booleano
print(True in types)
print('hola' in types)

#La función zip() une dos listas y devuelve una referencia. Esta referencia contiene una lista de tuplas. Las tuplas contienen los elementos con el mismo índice de las listas originales
# La función list() transforma la referencia en una lista para que los datos puedan ser leídos

print(zip(numbers, tasks))
print(zip(numbers, tasks), '=>' ,list(zip(numbers, tasks)))
