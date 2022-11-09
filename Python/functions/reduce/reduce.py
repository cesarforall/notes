# La función reduce() tiene que ser importada desde functools
import functools

numbers = [1, 2, 3, 4]

# La función reduce tiene un acumulador que es la suma de la iteración anterior
result = functools.reduce(lambda counter, item: counter + item, numbers)


def accum(counter, item):
    print('counter =>', counter)
    print('item =>', item)
    return counter + item


print(result)
