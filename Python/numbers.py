# int - integer - entero
lives = 3
print(type(lives))
age = 32
budget = 100

# float
temperature = 12.12
print(type(temperature))

lives = 2
print(lives)

lives = 1
print(lives)

lives = 12 + 15
print(lives)

lives = lives - 1
print(lives)

lives -= 1
print('-=:', lives)

lives -= 5
print('-=:', lives)

lives += 5
print('+=:', lives)

# Notación científica
number = 450000000000000000.1
print(number)

number_b = 0.000000000000001
print(number_b)

# Challenge

budget_month_1 = int(input('¿Cuál es el presupuesto del primer mes? '))
budget_month_2 = int(input('¿Cuál es el presupuesto del segundo mes? '))
budget_month_3 = int(input('¿Cuál es el presupuesto del tercer mes? '))
average = (budget_month_1 + budget_month_2 + budget_month_3) / 3
print('El promedio de los 3 meses es', average)
