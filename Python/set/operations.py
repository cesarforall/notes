#.union() añade los conjuntos pasados como parámetros
set_a = {'col', 'mex', 'bol'}
set_b = {'pe', 'bol', 2}
set_c = set_a.union(set_b)
print(set_c)
set_d = {'ecu', 'bol', 2}
set_c = set_a.union(set_b, set_d)
print(set_c)

# | une dos sets
print('| =>' ,set_a | set_b | set_c | set_d)

# .intersection() devuelve un conjunto con los items comunes entre los sets pasados como argumentos
set_e = set_c.intersection(set_d)
print('.intersection() =>' ,set_e)

# & devuelve los elemento comunes entre dos sets
print(set_b & set_d)

# Difference
# .difference() devuelve un set con los elementos del primero sin los elementos que son comunes con el segundo
# - hace la misma función
print(set_a)
print(set_d)
set_f = set_a.difference(set_d)
print(set_f)
print(set_a - set_d)

# Symetric Difference
# .symetric_difference() devuelve un set con los elementos que no son comunes
# ^ (signo de intercalación) hace la misma función

set_g = set_a.symmetric_difference(set_d)
print(set_g)
print(set_a ^ set_d)