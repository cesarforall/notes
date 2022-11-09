def sum_with_range(min, max):
    print(min, max)
    sum = 0
    for x in range(min, max + 1):
        sum += x
    return sum


result = sum_with_range(20, 30)
print(result)
print(sum_with_range(1, result))


def find_volume(length, width, depth):
    return length + width + depth


result = find_volume(10, 20, 30)
print(result)

# Declarar una función con parámetros con valores por defecto


def find_volume(length=1, width=1, depth=1):
    return length * width * depth


result2 = find_volume(10, 20, 30)
print(result2)

# Invocar una función enviando menos argumentos que los parámetros declarados

result3 = find_volume(width=10)
print(result3)

# return puede devolver múltiples valores. Al invocar a la función se devuelve una tupla


def find_volume2(length=1, width=1, depth=1):
    return length * width * depth, width, 'hello'


result4 = find_volume2()
print('result4', result4[1])
result5, width, text = find_volume2(width=10)
print('result4_all', result5, width, text)
