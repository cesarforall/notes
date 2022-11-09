x = 3.3
print(x)

y = 1.1 + 2.2
print(y)

print(x == y)

# Comparar flotantes como strings
y_str = format(y, ".2g")
print('str:' ,y_str)
print(y_str == str(x))

print('*' * 20)

print(y, x)

# Comparar números flotantes con margen de error (tolerancia)
# abs() es la función para transformar un número a valor absoluto
tolerance = 0.00001
print(abs(x - y) < tolerance)