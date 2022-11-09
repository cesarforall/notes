numbers = []
for element in range(1, 11):
  numbers.append(element)
print(numbers)

# List Comprehension
# [elemento (que va a ir en la lista) for (ciclo) element in (iterable)]
numbers_v2 = [element for element in range(1, 11)]
print(numbers_v2)

# [elemento (que va a ir en la lista) * 2 for (ciclo) element in (iterable)]
numbers_v3 = [element * 2 for element in range(1, 11)]
print(numbers_v3)

# Condición dentro de for
numbers_v4 = []
for i in range(1, 11):
  if i % 2 == 0:
    numbers_v4.append(i * 2)
print(numbers_v4)

# [elemento for element in iterable if condición]
numbers_v5 = [i * 2 for i in range(1, 11) if i % 2 == 0]
print(numbers_v5)