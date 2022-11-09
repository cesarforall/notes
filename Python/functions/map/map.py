# map(lambda, iterable) es una higher order function que devuelve una referencia a un objeto de tipo map

numbers = [1, 2, 3, 4]
numbers_v2 = []

for i in numbers:
  numbers_v2.append(i * 2)

numbers_v3 = list(map(lambda i : i * 2, numbers))

print(numbers)
print(numbers_v2)
print(numbers_v3)

# map() puede iterar dos listas y devuelve una transformación de las mismas
# El tamaño de la lista resultante es igual al tamaño de la lista con menor número de elementos

numbers_01 = [1, 2, 3, 4]
numbers_02 = [5, 6, 7]

result = list(map(lambda x, y: x + y, numbers_01, numbers_02))

print(numbers_01)
print(numbers_02)
print(result)