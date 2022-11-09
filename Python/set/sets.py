# Un conjunto se declara con llaves
# Tiene solo valores
# Los items son únicos. No se permiten duplicados. Si se repite en la declaración, Python lo elimina en la ejecución
# No importa el orden
set_countries = {'col', 'mex', 'bol', 'esp', 'esp'}

print(set_countries)
print(type(set_countries))

set_numbers = {1, 2, 2, 443, 23}
print(set_numbers)

set_types = {
  1, 'hola', False, 12.12
}
print(set_types)

set_from_string = set('hola')
print(set_from_string)

set_from_tuple = set(('abc', 'cbv', 'as', 'abc'))
print(set_from_tuple)

# set() retorna valores únicos
numbers = [1, 2, 3, 1, 2, 3, 4]
set_numbers = set(numbers)
print(set_numbers)
unique_numbers = list(set_numbers)
print(unique_numbers)