# La función open() carga un archivo en la memoria
file = open('./text.txt')
print(file)

# El método read() lee todas las líneas de un archivo cargado con la función open() de una sola vez. Esto ocupa más memoria que si se leyese línea a línea
# print(file.read())

# El método readline() una línea de un archivo. Cada vez que se invoca lee la siguiente línea. De esta forma no se sabe cuando terminar de leer un archivo.
#print('readline(): ', file.readline())

# Otra forma de leer un archivo línea a línea y saber cuando termina es usando un ciclo for
# Si se ha leido el archivo anteriormente con readline() continuará desde la última línea no leída

"""
for line in file:
  print('ciclo for: ', line)
"""

# El método close() cierra el archivo para liberar memoria
# file.close()

# with cierra un archivo automáticamente después de su uso

with open('./text.txt') as file:
    for line in file:
        print(line)
