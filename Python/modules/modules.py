# Un módulo es un fichero que contiene funciones, clases o variables.
# Puede ser usado por otros módulos

# La declaración import gana acceso a otros módulos
import sys
import re
import time
import collections

# El módulo sys contiene herramientas para interactuar con el sistema donde se está ejecutando Python
print(sys.path)

# El módulo re contiene herramientas para trabajar con expresiones regulares en Python

text = 'Mi numero de telefono es 311 123 121, el codigo del pais es 57, mi numero de la suerte 3'

result = re.findall('[0-9]+', text)
print(result)

# El módulo time contiene herramientas para trabajar con expresiones regulares en Python

timestamp = time.time()
print(timestamp)

local = time.localtime()
print(local)
result = time.asctime(local)
print(result)

# El módulo collections contiene herramientas para trabajar con listas en Python

# La función Counter() del módulo collections devuelve un objeto con la frecuencia de cada elemento en una lista
numbers = [1, 1, 2, 1, 2, 1, 4, 5, 3, 3, 21]
counter = collections.Counter(numbers)
print(counter)
