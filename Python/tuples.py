# Las tuplas son inmutables
# No pueden ser modificadas

numbers = (1, 2, 3, 5)
strings = ('cesar', 'alejandro', 'almeida', 'cesar')

print(numbers)
print('0 =>' ,numbers[0])
print('-1 =>' ,numbers[-1])
print(type(numbers))

print(strings)
print(type(strings))

# El método .index() devuelve la posición de un elemento dado
print(strings.index('almeida'))

# El método .count() devuelve el número de veces que aparece un elemento en una tupla
print(strings.count('cesar'))

# La función list() transforma una tupla en una lista
my_list = list(strings)
print(my_list)
print(type(my_list))

my_list[1] = 'alex'
print(my_list)

# La función tuple() transforma una lista en una tupla
my_tuple = tuple(my_list)
print(my_tuple)
print(type(my_tuple))
