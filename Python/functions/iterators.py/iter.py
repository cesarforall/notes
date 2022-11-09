for i in range(1, 4):
    print(i)

# La función range() devuelve una secuencia de números ordenados
# range() por sí sola es un objeto iterable
# Crea la secuencia según se va accediendo a ella
my_range = range(1, 4)
print('my_range:', my_range)

# La función iter() devuelve una referencia en memoria con objeto iterable
my_iter = iter(range(1, 4))
print('my_iter:', my_iter)

# La función next() devuelve el siguiente item de un iterable por cada vez que se invoca

print('next: ', next(my_iter))
print('next: ', next(my_iter))
print('next: ', next(my_iter))

# Si se ejecuta una siguiente iteración fuera de la secuencia Python devolverá un error StopIteration
#print('next: ', next(my_iter))
