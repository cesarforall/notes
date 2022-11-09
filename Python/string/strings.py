# El tipo de dato string es inmutable
# Se accede al valor de un caracter específico mediante índice
# text = 'Hola'
# text[0] = 'W'

name = "César"
last_name = "Almeida"
print(name)
print(last_name)

# Concatenación
full_name = name + ' ' + last_name
print('full_name:', full_name)

# Quote
quote = "I'm César"
print('quote:', quote)

quote2 = 'She said "Hello"'
print('quote2:', quote2)

# Template con concatenación
template = 'Hola, mi nombre es ' + name + ' y mi apellido es ' + last_name
print('template:',template)

# Template con la función .format
template = 'Hola, mi nombre es {} y mi apellido es {}'.format(name, last_name)
print('template con la función format:',template)

# Template con f""
template = f'Hola, mi nombre es {name} y mi apellido es {last_name}'
print('template con f""',template)

# Challenge
age = input("What is your age? ")
template = f'Hola, mi nombre es {name} y mi apellido es {last_name}. Tengo {age} años'
print('challenge con f""',template)
