set_countries = {'col', 'mex', 'bol', 'esp', 'esp'}

# len() devuelve el número de elementos que tiene el conjunto

size = len(set_countries)
print(size)

print('col' in set_countries)
print('usa' in set_countries)

# .add() agrega un elemento en un conjunto
set_countries.add('pe')
print(set_countries)
set_countries.add('pe')
print(set_countries)

# .update() permite enviar un conjunto al conjunto
set_countries.update({'ar', 'ecua', 'pe'})
print(set_countries)

# .remove() elimina un elemento pasado como argumento
# Si se pasa un elemento que no existe Python devuelve un KeyError
set_countries.remove('ecua')
print(set_countries)

# .discard() elimina un elemento pasado como argumento
# Si el elemento pasado como argumento no exist
set_countries.discard('bol')
print(set_countries)

# .clear() elimina todos los datos del conjunto y retorna set()
set_countries.clear()
print(set_countries)
