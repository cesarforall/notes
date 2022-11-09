# import this importa el Zen de Python, la filosofía con la cual se construye y se utiliza Python
"""
from pkg.mod_01 import func_1, func_2
from pkg.mod_02 import func_3, func_4

print(func_1())
print(func_2())
print(func_3())
print(func_4())
"""

# En versiones anteriores a la 3.3 de Python, para usar paquetes, es obligatorio añadir un archivo __init__.py dentro del paquete
# De esta forma se puede acceder de forma directa a los módulos

import pkg

print(pkg.URL)
print(pkg.mod_01.func_1())
