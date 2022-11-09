import random
# Dictionary Comprehension
"""
dict = {}
for i in range(1, 5):
  dict[i] = 1 * 2
print(dict)

dict_v2 = {i: i* 2 for i in range(1, 5)}
print(dict_v2)

# Generar un diccionario a partir de una lista
countries = ['col', 'mx', 'bol', 'pe']
population = {}

for i in countries:
  population[i] = random.randint(100000, 2500000)
print(population)

population_v2 = {i: random.randint(100000, 2500000) for i in countries }
print(population_v2)
"""
names = ['César', 'Alejandro', 'Nico']
ages = [12, 56, 98]

"""
persons = list(zip(names, ages))
print(type(persons))
persons_dict = {person[0]: person[1] for person in persons}
print(persons_dict)
"""
persons = {name: age for (name, age) in list(zip(names, ages))}
print(persons)

countries = ['col', 'mx', 'bol', 'pe']
population = {i: random.randint(1, 100) for i in countries }
print(population)

result = {country: population for (country, population) in population.items() if population > 50}
print(result)

text = 'Hola, soy César'
unique = {c: c.upper() for c in text if c in 'aeiou'}
print(unique)