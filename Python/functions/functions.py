# Functions
# def name() es la declaración de una función
# La función print() recibe un argumento y lo devuelve en consola
print('Hello')


def my_print(text):
    print('This is my print')
    print('This is my print 2')
    print(text * 2)


my_print('Este es mi texto')
my_print('Holita')

a = 10
b = 90
c = a + b
print(c)


def sum(a, b):
    c = a + b
    print(c)
    my_print(c)


sum(a, b)
sum(1, 5)
sum(10, 4)
