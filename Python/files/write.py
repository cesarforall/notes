# La función open() abre los archivos por defento con el modo lectura 'r'
# Para modificar un archivo el modo que llevará la función open es 'w'
# with open('./text.txt', 'w') as file:
# print(file)

# El modo 'r+' permite la lectura y escritura de un archivo. Cada línea que se añad con el método .write() se añadirá a continuación de la anterior
"""
with open('./text.txt', 'r+') as file:
  file.write('writing')
  for line in file:
    print(line)
"""

# \n marca el final de un línea. Si se añade más contenio empieza desde la siguiente línea

"""
with open('./text.txt', 'r+') as file:
  file.write('hello buddy\n')
  for line in file:
    print(line)
"""

# El modo 'w+' sobrescribe el archivo abierto

with open('./text.txt', 'w+') as file:
    file.write('Esto viene del modo w+')
    for line in file:
        print(line)
    print(file.read())
