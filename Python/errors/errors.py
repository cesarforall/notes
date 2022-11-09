# Cuando se produce un error el programa se detiene

# SyntaxError: unmatched ')' se produce al escribir mal la sintaxis de Python 
#print(0/0))

# ZeroDivisionError: division by zero se produce al hacer divisiones entre 0
#print(0/0)

# NameError: name 'result' is not defined se produce cuando se hace referencia a una variable que no existe
#print(result)

# NameError: name 'result' is not defined se produce cuando se hace referencia a una variable que no existe
#print(result)
#print('Hello')

# assert hace verificaciones. En el caso de que no sea correcta devuelve un error AssertionError
#sum = lambda x, y: x + y

#sum = lambda x, y: x + (y * 2)
#assert sum(2,2) == 4

# raise Exception() permite devolver nuestros propios errores
age = 10
if age < 18:
  raise Exception('No se permite menores de edad')