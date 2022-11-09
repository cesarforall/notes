text = "Ella sabe Python"
print(text[0])
print(text[1])

# El índice de una posición existente responde con IndexError
# print(text[30])

size = len(text)
print('size', size)
print(text[size - 1])

# El índice -1 empieza desde la última posición
print(text[-1])

# Slicing
# [#:#] devuelve un corte de string marcando una posición inicial y una final contando desde 1
print(text[3:6])
print(text[10:16])
print(text[5:-1])

# [:#] devuelve un corte de string marcando la posición inicial como 0
print(text[0:10])

# [#:] devuelve un corte de string marcando una posición inicial hasta el último caracter por defecto
print(text[5:])

# [:] devuelve un corte de string desde el inicio hasta el final
print(text[0:])

# [#:#:#] salta un número de caracteres obiando los espacios
print(text[5:16:2])
print(text[::2])