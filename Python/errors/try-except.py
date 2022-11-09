# try except captura el error y mantiene la ejecución del programa
"""
try:
  print(0/0)
except ZeroDivisionError as error:
  print(error)
"""

#assert 1 != 1, 'Uno sí es igual que uno'
"""
try:
  assert 1 != 1, 'Uno sí es igual que uno'
except AssertionError as error:
  print(error)

print('Hello')
"""

# se pueden capturar varios errores con un solo try y varios except
# cuando la ejecución devuelva un error el bloque try se detiene

try:
    print(0 / 0)
    assert 1 != 1, 'Uno sí es igual que uno'
    age = 10
    if age < 18:
        raise Exception('No se permiten menores de edad')

except ZeroDivisionError as error:
    print(error)
except AssertionError as error:
    print(error)
except Exception as error:
    print('error:', error)
