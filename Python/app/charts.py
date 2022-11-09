"""
- abrir documento
- filtrar pais
- filtrar años
- generar key value
- generar tabla
- imprimir tabla
"""

import csv

with open('./app/world_population.csv') as csvfile:
    reader = csv.reader(csvfile)

    headers = next(reader)
    # print(headers)
    headers = list(map(lambda header: header.lower(), headers))
    # print(headers)

    data = []

    for row in reader:
        iterable = zip(headers, row)
        country = {key: value for key, value in iterable}
        data.append(country)

    population_headers = list(
        filter(lambda header: 'population' in header, headers))
    population_headers = list(
        filter(lambda header: not 'world' in header, population_headers))
    print(population_headers)
    print(data[1])
