# CRUD Create, Read, Update & Delete

numbers = [1, 2, 3, 4, 5]
print(numbers[1])

# Update
numbers[-1] = 10
print(numbers)

# .append() agrega un elemento al final de la lista
numbers.append(700)
print(numbers)

# .insert() agrega un elemento en cualquier posición moviendo el resto de elementos
numbers.insert(0, 'hola')
print(numbers)

numbers.insert(3, 'change')
print(numbers)

tasks = ['todo 1', 'todo 2', 'todo 3']

# Juntar listas 
new_list = numbers + tasks
print(new_list)

# El método .index() devuelve la posición de un elemento en la lista

index = new_list.index('todo 2')
new_list[index] = 'todo changed'
print(new_list)

# El método .remove() elimina el elemento dato

new_list.remove('todo 1')
print(new_list)

# El método .pop() elimina el último elemento de la lista
new_list.pop()
print(new_list)

# El método .pop(index) elimina el elemento en la posición del índice
new_list.pop(0)
print(new_list)

# El método .reverse() transforma la lista y la ordena desde el último elemento al primero
new_list.reverse()
print(new_list)

numbers_a = [1, 4, 6, 3]
strings = ['re', 'ab', 'ed']
print(numbers_a)
print(strings)

# El método .sort() ordena la lista de menor a mayor
# No funciona cuando la lista tiene diferentes tipos de datos

numbers_a.sort()
print(numbers_a)

strings.sort()
print(strings)
