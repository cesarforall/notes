if True:
    print('Se ejecuta porque es True')

if False:
    print('Nunca se ejecuta porque es False')

pet = input('¿Cuál es tu mascota favorita? ')

if pet == 'perro':
  print('Genial, tienes buen gusto')

elif pet == 'gato':
  print('Espero tengas suerte')
  
elif pet == 'gato':
  print('Not bad')

else:
  print('Interesante, no tienes ninguna mascota')
  
"""
stock = int(input('Escribe el stock: '))

if stock >= 100 and stock <= 1000:
    print('el stock es correcto')
else:
  print('el stock es incorrecto')
"""

# Challenge

numero = int(input('Escribe un número: '))

if numero % 2 == 0:
  print(f"El número {numero} es par")
else:
  print(f"El número {numero} es impar")